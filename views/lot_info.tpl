%rebase('base.tpl')
    <link rel="stylesheet" href="/static/css/splide-default.min.css">
    <script defer src="/static/js/splide.min.js"></script>
    <div class="lot-info">
        <h2 class="lot-title">{{lot.title}}</h2>
          <section class="splide" aria-label="Splide Basic HTML Example">
              <div class="splide__track">
                    <ul class="splide__list">
                    % for picture in pictures:
                        <li class="splide__slide">
                            <div style="display:flex; justify-content:center;">
                                <img src="/media/lots/{{lot.picture_path}}/{{picture}}">
                            </div>
                        </li>
                    % end
                    </ul>
              </div>
            </section>
        <p>Опис: {{lot.description}}</p>
        <p>Продавець: {{lot.seller}}</p>
        <p style="margin-top:20px;">Поточна ставка:</p>
        <p class="lot-price">{{lot.cur_bid}}</p>

    </div>
    <script>
    document.addEventListener('DOMContentLoaded', function() {
    var splide = new Splide( '.splide' );
    splide.mount();});
    </script>