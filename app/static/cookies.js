window.addEventListener('DOMContentLoaded', function () {
  const cookiePopup = document.getElementById('cookie-consent-popup');
  const acceptAllButton = document.querySelector('.accept-all');
  const acceptNecessaryButton = document.querySelector('.accept-necessary');

  if (!cookiePopup || !acceptAllButton || !acceptNecessaryButton) {
    console.error("Cookie popup or buttons not found! Check your HTML.");
    return;
  }

  if (localStorage.getItem('cookies_accepted')) {
    console.log("Cookies already accepted. Hiding popup.");
    cookiePopup.style.display = 'none';
    return;
  }

  const hideCookiePopup = () => {
    cookiePopup.style.display = 'none';
    console.log('Cookie popup hidden');
  };

  acceptAllButton.addEventListener('click', () => {
    console.log("User clicked 'Accept All Cookies'");
    localStorage.setItem('cookies_accepted', 'all');
    hideCookiePopup();
  });

  acceptNecessaryButton.addEventListener('click', () => {
    console.log("User clicked 'Accept Only Necessary Cookies'");
    localStorage.setItem('cookies_accepted', 'necessary');
    hideCookiePopup();
  });
});
