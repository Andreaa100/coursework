from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, login_user, logout_user, current_user
from app import app, db, admin
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user
from werkzeug.security import generate_password_hash 
from flask_admin.contrib.sqla import ModelView
from app.forms import AddToCartForm, AddToFavoriteForm
from werkzeug.security import check_password_hash
from app.models import User, CartItem, Product, Favorite, Order, OrderItem

@app.route('/accept_cookies', methods=['POST'])
def accept_cookies():
    response = make_response(redirect(url_for('home')))
    
    response.set_cookie('cookies_accepted', 'true', max_age=60*60*24*30)
    
    return response

@app.route('/favoritesearch', methods=['GET'])
def favoritesearch():
    query = request.args.get('query', '')
    
    if query:
        products = Product.query.join(Favorite).filter(
            Favorite.user_id == current_user.id,
            (Product.name.ilike(f'%{query}%') | 
             Product.description.ilike(f'%{query}%') | 
             Product.category.ilike(f'%{query}%') | 
             Product.gender.ilike(f'%{query}%'))
        ).all()
    else:
        products = Product.query.join(Favorite).filter(Favorite.user_id == current_user.id).all()

    return render_template('favorite_search.html', products=products, query=query)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.password.data != form.confirm_password.data:
        flash("Passwords do not match.", "danger")
        return redirect(url_for('register'))
    
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash("An account with this email already exists. Please log in or use another email address.", "danger")
            return redirect(url_for('register')) 
        
        hashed_password = generate_password_hash(form.password.data)
        user = User(
            email=form.email.data,
            password_hash=hashed_password,
            name=form.name.data,
            surname=form.surname.data,
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('home'))

    return render_template('register.html', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if user.check_password(form.password.data):
                login_user(user)
                return redirect(url_for('home'))
            else:
                flash("Incorrect password. Please try again.", "danger")
        if not current_user.is_authenticated:
            flash("An account with this email address doesn't exist. Please register before logging in.", "danger")
    return render_template('login.html', form=form)


@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)


@app.route('/current_user')
def current_user_info():
    if current_user.is_authenticated:
        return f"Logged in as: {current_user.email}"
    return "No user is logged in."


@app.route('/change_password', methods=['POST'])
@login_required
def change_password():
    current_password = request.form['current_password']
    new_password = request.form['new_password']
    confirm_password = request.form['confirm_password']

    if not current_user.check_password(current_password):
        flash("Incorrect current password.", "danger")
        return redirect(url_for('profile'))

    if new_password != confirm_password:
        flash("New passwords do not match.", "danger")
        return redirect(url_for('profile'))

    current_user.password_hash = generate_password_hash(new_password)
    db.session.commit()
    flash("Password updated successfully!", "success")
    return redirect(url_for('profile'))


@app.route('/delete_account', methods=['POST'])
@login_required
def delete_account():
    user = current_user
    CartItem.query.filter_by(user_id=current_user.id).delete()
    Favorite.query.filter_by(user_id=current_user.id).delete()
    
    Order.query.filter_by(user_id=current_user.id).delete()
    orders = Order.query.filter_by(user_id=current_user.id).all()
    for order in orders:
        OrderItem.query.filter_by(order_id=order.id).delete()

    db.session.delete(user)
    db.session.commit()
    
    logout_user()

    flash("Your account has been deleted successfully.", "success")
    return redirect(url_for('home'))


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    if query:
        products = Product.query.filter(
            Product.name.ilike(f'%{query}%') | 
            Product.description.ilike(f'%{query}%') | 
            Product.category.ilike(f'%{query}%') | 
            Product.gender.ilike(f'%{query}%')
        ).all()
    else:
        products = []

    return render_template('search_results.html', products=products, query=query)


@app.route('/category/<string:gender>/<string:category>', methods=['GET', 'POST'])
def category_page(gender, category):
    category_filter = f"{gender}/{category}"
    products = Product.query.filter_by(category=category_filter).all()

    cart_form = AddToCartForm()
    favorite_form = AddToFavoriteForm()

    if cart_form.validate_on_submit():
        product_id = cart_form.product_id.data
        quantity = cart_form.quantity.data
        if current_user.is_authenticated:
            cart_item = CartItem(user_id=current_user.id, product_id=product_id, quantity=quantity)
            db.session.add(cart_item)
            db.session.commit()
            flash("Added to cart!", "success")
        else:
            flash("Please log in to add items to your cart.", "danger")
        return redirect(request.referrer)

    if favorite_form.validate_on_submit():
        product_id = favorite_form.product_id.data
        if current_user.is_authenticated:
            favorite = Favorite(user_id=current_user.id, product_id=product_id)
            db.session.add(favorite)
            db.session.commit()
            flash("Added to favorites!", "success")
        else:
            flash("Please log in to add items to favorites.", "danger")
        return redirect(request.referrer)

    return render_template('category.html', products=products, cart_form=cart_form, favorite_form=favorite_form)


@app.route('/product/<int:product_id>', methods=['GET', 'POST'])
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    cart_form = AddToCartForm()
    favorite_form = AddToFavoriteForm()

    if not current_user.is_authenticated:
        flash("Please log in to add items to the cart or to favorites.", "danger")

    if cart_form.validate_on_submit():
        size = cart_form.size.data
        quantity = cart_form.quantity.data
        if current_user.is_authenticated:
            cart_item = CartItem(user_id=current_user.id, product_id=product.id, quantity=quantity)
            db.session.add(cart_item)
            db.session.commit()
            flash("Added to cart!", "success")
        else:
            flash("Please log in to add items to your cart.", "danger")
        return redirect(request.referrer)

    if favorite_form.validate_on_submit():
        if current_user.is_authenticated:
            favorite = Favorite(user_id=current_user.id, product_id=product.id)
            db.session.add(favorite)
            db.session.commit()
            flash("Added to favorites!", "success")
        else:
            flash("Please log in to add items to favorites.", "danger")
        return redirect(request.referrer)

    return render_template('product_detail.html', product=product, cart_form=cart_form, favorite_form=favorite_form)


@app.route('/cart')
def cart():
    if not current_user.is_authenticated:
        flash("Please log in to view your cart.", "danger")
        return redirect(url_for('login'))

    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    total_price = 0
    insufficient_stock = False

    for item in cart_items:
        if item.product:
            item_price = float(item.product.price.replace('£', '').replace(',', '') 
                if item.product.price else 0.0)
            
            total_price += item_price * item.quantity

            if item.size == 'S':
                if item.quantity > item.product.stock_s:
                    insufficient_stock = True
            elif item.size == 'M':
                if item.quantity > item.product.stock_m:
                    insufficient_stock = True
            elif item.size == 'L':
                if item.quantity > item.product.stock_l:
                    insufficient_stock = True

    return render_template('cart.html', cart_items=cart_items, total_price=total_price, 
        insufficient_stock=insufficient_stock)


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if not current_user.is_authenticated:
        flash("Please log in to add items to your cart.", "danger")
        return redirect(url_for('login'))

    try:
        product_id = request.form.get('product_id')
        size = request.form.get('size')
        quantity = int(request.form.get('quantity', 1))

        product = Product.query.get(product_id)
        if not product:
            flash("Product not found.", "danger")
            return redirect(url_for('home'))

        valid_sizes = ['S', 'M', 'L']
        if size not in valid_sizes:
            return redirect(url_for('product_detail', product_id=product_id))

        if quantity <= 0:
            flash("Quantity must be at least 1.", "danger")
            return redirect(url_for('product_detail', product_id=product_id))

        if size == 'S' and product.stock_s < quantity:
            flash(f"Not enough stock for size {size}.", "danger")
            return redirect(url_for('product_detail', product_id=product_id))
        elif size == 'M' and product.stock_m < quantity:
            flash(f"Not enough stock for size {size}.", "danger")
            return redirect(url_for('product_detail', product_id=product_id))
        elif size == 'L' and product.stock_l < quantity:
            flash(f"Not enough stock for size {size}.", "danger")
            return redirect(url_for('product_detail', product_id=product_id))

        cart_item = CartItem.query.filter_by(user_id=current_user.id, product_id=product_id, size=size).first()
        if cart_item:
            cart_item.quantity += quantity
        else:
            cart_item = CartItem(user_id=current_user.id, product_id=product_id, quantity=quantity, size=size)
            db.session.add(cart_item)

        db.session.commit()
        flash(f"Added {product.name} (Size {size}) to your cart.", "success")
        return redirect(url_for('product_detail', product_id=product_id))

    except Exception as e:
        flash("An error occurred while adding the item to the cart.", "danger")
        return redirect(url_for('product_detail', product_id=request.form.get('product_id')))


@app.route('/update_cart_quantity/<int:item_id>', methods=['POST'])
@login_required
def update_cart_quantity(item_id):
    item = CartItem.query.get_or_404(item_id)

    if item.user_id == current_user.id:
        action = request.form.get('action')
        
        if action == 'increase':
            item.quantity += 1 
        elif action == 'decrease' and item.quantity > 1:
            item.quantity -= 1
        
        db.session.commit()
    
    return redirect(url_for('cart'))


@app.route('/remove_from_cart/<int:item_id>', methods=['POST'])
@login_required
def remove_from_cart(item_id):
    item = CartItem.query.get_or_404(item_id)
    if item.user_id == current_user.id:
        db.session.delete(item)
        db.session.commit()
        flash("Item removed from cart", "success")
    return redirect(url_for('cart'))


@app.route('/favorites')
def favorites():
    if not current_user.is_authenticated:
        flash("Please log in to view your favorites.", "danger")
        return redirect(url_for('login'))

    favorite_products = Product.query.join(Favorite).filter(Favorite.user_id == current_user.id).all()

    cart_form = AddToCartForm()

    return render_template('favorites.html', products=favorite_products, cart_form=cart_form)


@app.route('/add_to_favorites/<int:product_id>', methods=['POST'])
def add_to_favorites(product_id):
    if current_user.is_authenticated:
        product = Product.query.get_or_404(product_id)

        existing_favorite = Favorite.query.filter_by(user_id=current_user.id, product_id=product.id).first()
        if not existing_favorite:
            new_favorite = Favorite(user_id=current_user.id, product_id=product.id)
            db.session.add(new_favorite)
            db.session.commit()
            flash("Added to favorites!", "success")
        else:
            flash("This product is already in your favorites.", "info")
    else:
        flash("Please log in to add items to favorites.", "danger")

    return redirect(request.referrer)


@app.route('/remove_from_favorites/<int:product_id>', methods=['POST'])
@login_required
def remove_from_favorites(product_id):
    favorite = Favorite.query.filter_by(user_id=current_user.id, product_id=product_id).first()

    if favorite:
        db.session.delete(favorite)
        db.session.commit()
        flash("Product removed from favorites.", "success")
    else:
        flash("Product not found in your favorites.", "danger")

    return redirect(url_for('favorites'))


@app.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    if request.method == 'POST':
        address = request.form.get('address')

        cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
        if not cart_items:
            flash("Your cart is empty.", "danger")
            return redirect(url_for('cart'))

        for item in cart_items:
            total = 0

        for item in cart_items:
            item_price = float(item.product.price.replace('£', '').replace(',', ''))
            total += item_price * item.quantity

        order = Order(user_id=current_user.id, total_price=total)
        db.session.add(order)
        db.session.flush()

        for item in cart_items:
            if item.size == 'S' and item.quantity <= item.product.stock_s:
                item.product.stock_s -= item.quantity
            elif item.size == 'M' and item.quantity <= item.product.stock_m:
                item.product.stock_m -= item.quantity
            elif item.size == 'L' and item.quantity <= item.product.stock_l:
                item.product.stock_l -= item.quantity
            else:
                flash(f"Product {item.product.name} in size {item.size} is out of stock.", "danger")
                db.session.rollback()
                return redirect(url_for('cart'))

            order_item = OrderItem(
                order_id=order.id,
                product_id=item.product_id,
                quantity=item.quantity,
                price=item_price,
                size=item.size
            )
            db.session.add(order_item)

        db.session.commit()
        CartItem.query.filter_by(user_id=current_user.id).delete()
        db.session.commit()

        return redirect(url_for('order_confirmation'))

    return render_template('checkout.html')


@app.route('/order_confirmation')
@login_required
def order_confirmation():
    return render_template('order_confirmation.html')


@app.route('/order_history')
@login_required
def order_history():
    orders = Order.query.filter_by(user_id=current_user.id).order_by(Order.created_at.desc()).all()
    return render_template('order_history.html', orders=orders)
