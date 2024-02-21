<script>
    import twitterIcon from './images/twitter-x.svg'; // Update the file name as necessary
    import instagramIcon from './images/instagram.svg'; // Update the file name as necessary
    import telegramIcon from './images/telegram.svg';
</script>

<style>

</style>

<main>
    <div class="container">
        <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
          <div class="col-md-4 d-flex align-items-center">
            <a href="/" class="mb-3 me-2 mb-md-0 text-body-secondary text-decoration-none lh-1">
              <svg class="bi" width="30" height="24">
                <use xlink:href="#bootstrap"></use>
              </svg>
            </a>
            <span class="mb-3 mb-md-0 text-body-secondary">© 2023 Company, Inc</span>
          </div>
      
          <ul class="nav col-md-4 justify-content-end list-unstyled d-flex">
            <li class="ms-3">
              <a class="text-body-secondary" href="#">
                <img width="24" height="24" src={twitterIcon} alt="Twitter logo">
              </a>
            </li>
            <li class="ms-3">
              <a class="text-body-secondary" href="#">
                <img width="24" height="24" src={instagramIcon} alt="Instagram logo">
              </a>
            </li>
            <li class="ms-3">
              <a class="text-body-secondary" href="#">
                <img width="24" height="24" src={telegramIcon} alt="Telegram logo">
              </a>
            </li>
          </ul>
        </footer>
      </div>
</main>