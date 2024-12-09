from app import db
from app.models import Product

products = [
    # WOMAN JACKETS 4
    {
        'id': 1,
        'name': 'BROWN FAUX LEATHER BOMBER JACKET',
        'price': '£69.90',
        'description': 'Lapel collar bomber jacket with long sleeves and buttoned cuffs',
        'image_url': '/static/images/woman_jacket1.jpg',
        'category': 'WOMAN/JACKETS',
        'stock_s': 100,
        'stock_m': 100,
        'stock_l': 100
    },
    {
        'id': 2,
        'name': 'BLUE CROPPED SOFT JACKET',
        'price': '£59.90',
        'description': 'Lapel collar jacket with long sleeves with epaulettes',
        'image_url': '/static/images/woman_jacket2.jpg',
        'category': 'WOMAN/JACKETS',
        'stock_s': 100,
        'stock_m': 100,
        'stock_l': 100
    },
        {
        'id': 3,
        'name': 'SKI COLLECTION JACKET',
        'price': '£269.00 ',
        'description': 'Windproof and waterproof technical down jacket with thermal insulation for cold climates',
        'image_url': '/static/images/woman_jacket3.jpg',
        'category': 'WOMAN/JACKETS',
        'stock_s': 100,
        'stock_m': 100,
        'stock_l': 100
    },
    {
        'id': 4,
        'name': 'BLACK WAXED JACKET WITH CORDUROY COLLAR',
        'price': '£59.99',
        'description': 'Padded jacket',
        'image_url': '/static/images/woman_jacket4.jpg',
        'category': 'WOMAN/JACKETS',
        'stock_s': 100,
        'stock_m': 100,
        'stock_l': 100
    },
    # WOMAN SHIRTTS 5
    {
        'id': 5,
        'name': ' BLACK RUFFLED SATIN SHIRT',
        'price': '£25.99',
        'description': 'Shirt featuring a V-neckline with ruffles',
        'image_url': '/static/images/woman_shirt1.jpg',
        'category': 'WOMAN/T-SHIRTS | SHIRTS',
        'stock_s': 100,
        'stock_m': 100,
        'stock_l': 100
    },
    {
        'id': 6,
        'name': 'BLACK LACE TRIM TOP WITH BOW',
        'price': '£15.99',
        'description': 'Top with a square neckline and cap sleeves',
        'image_url': '/static/images/woman_shirt2.jpg',
        'category': 'WOMAN/T-SHIRTS | SHIRTS',
        'stock_s': 100,
        'stock_m': 100,
        'stock_l': 100
    },
    {
        'id': 7,
        'name': 'BROWN STRETCH HALTER TOP',
        'price': '£17.99',
        'description': 'Top made of stretch fabric',
        'image_url': '/static/images/woman_shirt3.jpg',
        'category': 'WOMAN/T-SHIRTS | SHIRTS',
        'stock_s': 100,
        'stock_m': 100,
        'stock_l': 100
    },
    {
        'id': 8,
        'name': 'CROP DENIM SHIRT',
        'price': '£27.99',
        'description': 'Collared shirt with a v-neck and long sleeves. Front patch pockets',
        'image_url': '/static/images/woman_shirt4.jpg',
        'category': 'WOMAN/T-SHIRTS | SHIRTS',
        'stock_s': 100,
        'stock_m': 100,
        'stock_l': 100
    },
    {
        'id': 9,
        'name': 'RED KNIT TOP WITH GOLDEN APPLIQUÉ',
        'price': '£23.90',
        'description': 'Strapless knit top with a turn-up hem and exposed shoulders',
        'image_url': '/static/images/woman_shirt5.jpg',
        'category': 'WOMAN/T-SHIRTS | SHIRTS',
        'stock_s': 100,
        'stock_m': 100,
        'stock_l': 100
    },
    # WOMAN DRESSES 3
    {
        'id': 10,
        'name': 'BLACK GATHERED CORSETRY-INSPIRED ',
        'price': '£40.00',
        'description': 'Short dress with a square neckline and straps',
        'image_url': '/static/images/woman_dress1.jpg',
        'category': 'WOMAN/DRESSES | SKIRTS',
        'stock_s': 100,
        'stock_m': 100,
        'stock_l': 100
    },
    {
        'id': 11,
        'name': 'BROWN SATIN MIDI DRESS',
        'price': '£32.99',
        'description': 'Satin midi dress. V-neck and adjustable thin straps',
        'image_url': '/static/images/woman_dress2.jpg',
        'category': 'WOMAN/DRESSES | SKIRTS',
        'stock_s': 100,
        'stock_m': 100,
        'stock_l': 100
    },
        {
        'id': 12,
        'name': 'SEQUINNED MINISKIRT',
        'price': '£35.99.00 ',
        'description': ' Featuring a rectangular sequin appliqué and a matching lining',
        'image_url': '/static/images/woman_dress3.jpg',
        'category': 'WOMAN/DRESSES | SKIRTS',
        'stock_s': 100,
        'stock_m': 100,
        'stock_l': 100
    },
    # WOMAN TROUSERS 4
    {
        'id': 13,
        'name': 'STRAIGHT-LEG MID-RISE JEANS',
        'price': '£29.90',
        'description': 'Relaxed Fit - Straight Leg - Mid Waist',
        'image_url': '/static/images/woman_trousers1.jpg',
        'category': 'WOMAN/TROUSERS',
        'stock_s': 100,
        'stock_m': 100,
        'stock_l': 100
    },
    {
        'id': 14,
        'name': 'SLIM FIT MID-RISE JEANS',
        'price': '£59.90',
        'description': 'Slim Fit - Slim Leg - Mid-Waist',
        'image_url': '/static/images/woman_trousers2.jpg',
        'category': 'WOMAN/TROUSERS',
        'stock_s': 100,
        'stock_m': 100,
        'stock_l': 100
    },
    {
        'id': 15,
        'name': 'GREY STRAIGHT HIGH WAIST LONG LENGTH JEANS',
        'price': '£25.00 ',
        'description': 'High-waist jeans with five pockets',
        'image_url': '/static/images/woman_trousers3.jpg',
        'category': 'WOMAN/TROUSERS',
        'stock_s': 100,
        'stock_m': 100,
        'stock_l': 100
    },
    {
        'id': 16,
        'name': 'TRF BALLOON FLOCK JEANS',
        'price': '£59.99',
        'description': 'High-waist jeans with belt loops and five pockets',
        'image_url': '/static/images/woman_trousers4.jpg',
        'category': 'WOMAN/TROUSERS',
        'stock_s': 100,
        'stock_m': 100,
        'stock_l': 100
    },

    # WOMAN SHOES 3
    {
        'id': 17,
        'name': 'BLACK BUCKLE STRAP HEELS',
        'price': '£40.00',
        'description': 'Heeled shoes with straps and buckles on the front. Stiletto heel',
        'image_url': '/static/images/woman_shoe1.jpg',
        'category': 'WOMAN/SHOES',
        'stock_s': 100,
        'stock_m': 100,
        'stock_l': 100
    },
    {
        'id': 18,
        'name': 'RED HIGH-HEELED BOOTS',
        'price': '£60.00',
        'description': 'High leg. Pointed toe. Zip fastening',
        'image_url': '/static/images/woman_shoe2.jpg',
        'category': 'WOMAN/SHOES',
        'stock_s': 100,
        'stock_m': 100,
        'stock_l': 100
    },
    {
        'id': 19,
        'name': 'BROWN VELVET BALLERINA FLATS',
        'price': '£35.99',
        'description': 'Bow detail on the front. Square toe',
        'image_url': '/static/images/woman_shoe3.jpg',
        'category': 'WOMAN/SHOES',
        'stock_s': 100,
        'stock_m': 100,
        'stock_l': 100
    },

# MAN JACKETS 4
{
    'id': 20,
    'name': 'BLACK FAUX LEATHER JACKET',
    'price': '£79.90',
    'description': 'Bomber-style jacket with zip fastening and ribbed trims',
    'image_url': '/static/images/man_jacket1.jpg',
    'category': 'MAN/JACKETS',
    'stock_s': 100,
    'stock_m': 100,
    'stock_l': 100
},
{
    'id': 21,
    'name': 'CAMEL WOOL-BLEND COAT',
    'price': '£129.90',
    'description': 'Long coat with a notched lapel collar and button fastening',
    'image_url': '/static/images/man_jacket2.jpg',
    'category': 'MAN/JACKETS',
    'stock_s': 100,
    'stock_m': 100,
    'stock_l': 100
},
{
    'id': 22,
    'name': 'PUFFER JACKET WITH HOOD',
    'price': '£99.90',
    'description': 'Water-resistant puffer jacket with a zip fastening',
    'image_url': '/static/images/man_jacket3.jpg',
    'category': 'MAN/JACKETS',
    'stock_s': 100,
    'stock_m': 100,
    'stock_l': 100
},
{
    'id': 23,
    'name': 'NAVY DOUBLE-BREASTED BLAZER',
    'price': '£149.99',
    'description': 'Blazer with a slim fit and double-breasted button fastening',
    'image_url': '/static/images/man_jacket4.jpg',
    'category': 'MAN/JACKETS',
    'stock_s': 100,
    'stock_m': 100,
    'stock_l': 100
},
# MAN SHIRTS 5
{
    'id': 24,
    'name': 'WHITE OXFORD SHIRT',
    'price': '£29.99',
    'description': 'Long-sleeved shirt with a button-down collar',
    'image_url': '/static/images/man_shirt1.jpg',
    'category': 'MAN/T-SHIRTS | SHIRTS',
    'stock_s': 100,
    'stock_m': 100,
    'stock_l': 100
},
{
    'id': 25,
    'name': 'BLACK SATIN DRESS SHIRT',
    'price': '£39.90',
    'description': 'Slim-fit shirt with a smooth satin finish',
    'image_url': '/static/images/man_shirt2.jpg',
    'category': 'MAN/T-SHIRTS | SHIRTS',
    'stock_s': 100,
    'stock_m': 100,
    'stock_l': 100
},
{
    'id': 26,
    'name': 'CHECKERED FLANNEL SHIRT',
    'price': '£25.90',
    'description': 'Soft flannel shirt with a casual fit and button fastening',
    'image_url': '/static/images/man_shirt3.jpg',
    'category': 'MAN/T-SHIRTS | SHIRTS',
    'stock_s': 100,
    'stock_m': 100,
    'stock_l': 100
},
{
    'id': 27,
    'name': 'BLUE STRIPED LINEN SHIRT',
    'price': '£35.99',
    'description': 'Linen shirt with a relaxed fit and mandarin collar',
    'image_url': '/static/images/man_shirt4.jpg',
    'category': 'MAN/T-SHIRTS | SHIRTS',
    'stock_s': 100,
    'stock_m': 100,
    'stock_l': 100
},
{
    'id': 28,
    'name': 'KHAKI WORKWEAR SHIRT',
    'price': '£27.90',
    'description': 'Utility-style shirt with chest pockets',
    'image_url': '/static/images/man_shirt5.jpg',
    'category': 'MAN/T-SHIRTS | SHIRTS',
    'stock_s': 100,
    'stock_m': 100,
    'stock_l': 100
},
# MAN TROUSERS 4
{
    'id': 29,
    'name': 'BLACK SLIM-FIT TROUSERS',
    'price': '£45.00',
    'description': 'Tailored trousers with a slim fit and zip fastening',
    'image_url': '/static/images/man_trousers1.jpg',
    'category': 'MAN/TROUSERS',
    'stock_s': 100,
    'stock_m': 100,
    'stock_l': 100
},
{
    'id': 30,
    'name': 'GREY CHINOS',
    'price': '£39.90',
    'description': 'Cotton chinos with a straight fit and side pockets',
    'image_url': '/static/images/man_trousers2.jpg',
    'category': 'MAN/TROUSERS',
    'stock_s': 100,
    'stock_m': 100,
    'stock_l': 100
},
{
    'id': 31,
    'name': 'DARK BLUE JEANS',
    'price': '£49.90',
    'description': 'Skinny fit jeans with a mid-rise waist',
    'image_url': '/static/images/man_trousers3.jpg',
    'category': 'MAN/TROUSERS',
    'stock_s': 100,
    'stock_m': 100,
    'stock_l': 100
},
{
    'id': 32,
    'name': 'TAN CARGO TROUSERS',
    'price': '£29.99',
    'description': 'Casual trousers with multiple utility pockets',
    'image_url': '/static/images/man_trousers4.jpg',
    'category': 'MAN/TROUSERS',
    'stock_s': 100,
    'stock_m': 100,
    'stock_l': 100
},
# MAN SHOES 3
{
    'id': 33,
    'name': 'BLACK LEATHER LOAFERS',
    'price': '£75.00',
    'description': 'Classic loafers with a polished finish',
    'image_url': '/static/images/man_shoes1.jpg',
    'category': 'MAN/SHOES',
    'stock_s': 100,
    'stock_m': 100,
    'stock_l': 100
},
{
    'id': 34,
    'name': 'BROWN SUEDE CHELSEA BOOTS',
    'price': '£85.00',
    'description': 'Boots with elastic side panels and pull tab',
    'image_url': '/static/images/man_shoes2.jpg',
    'category': 'MAN/SHOES',
    'stock_s': 100,
    'stock_m': 100,
    'stock_l': 100
},
{
    'id': 35,
    'name': 'WHITE LEATHER TRAINERS',
    'price': '£55.99',
    'description': 'Casual sneakers with a rubber sole',
    'image_url': '/static/images/man_shoes3.jpg',
    'category': 'MAN/SHOES',
    'stock_s': 100,
    'stock_m': 100,
    'stock_l': 100
},
# MAN HOODIES 3
{
    'id': 36,
    'name': 'WASHED BOXY FIT HOODIE',
    'price': '£40.00',
    'description': 'Short hoodie with a square neckline and straps',
    'image_url': '/static/images/man_hoodie1.jpg',
    'category': 'MAN/HOODIES | SWEATSHIRTS',
    'stock_s': 100,
    'stock_m': 100,
    'stock_l': 100
},
{
    'id': 37,
    'name': 'GREY CREW NECK SWEATSHIRT',
    'price': '£30.99',
    'description': 'Long sleeve sweatshirt with a round neck and ribbed trims',
    'image_url': '/static/images/man_hoodie2.jpg',
    'category': 'MAN/HOODIES | SWEATSHIRTS',
    'stock_s': 100,
    'stock_m': 100,
    'stock_l': 100
},
{
    'id': 38,
    'name': 'BLACK HEAVY WEIGHT HOODIE',
    'price': '£89.99',
    'description': 'Relaxed fit hoodie made of compact and heavyweight cotton fabric with a matching lining',
    'image_url': '/static/images/man_hoodie3.jpg',
    'category': 'MAN/HOODIES | SWEATSHIRTS',
    'stock_s': 100,
    'stock_m': 100,
    'stock_l': 100
},
]
   
# Function to populate the database
def populate_products():

    for product in products:
        
        db.session.add(Product(**product))

    db.session.commit()

    print("Products have been added to the database")

if __name__ == "__main__":
    from app import create_app
    app = create_app()
    with app.app_context():
        populate_products()
