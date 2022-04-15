%rebase('base.tpl')
    <link rel="stylesheet" href="/static/css/splide-default.min.css">
    <script defer src="/static/js/splide.min.js"></script>
    <div class="lot-info">
        <h2 class="lot-title">{{lot.title}}</h2>
          <section class="splide" style="background: #00000038; border-radius: 15px; padding: 10px;" aria-label="Splide Basic HTML Example">
              <div class="splide__track">
                    <ul class="splide__list">
                    % for picture in pictures:
                        <li class="splide__slide">
                            <div style="display:flex; justify-content:center;">
                                <img style="height: 500px; border-radius: 5px;"src="/media/lots/{{lot.id}}/{{picture}}">
                            </div>
                        </li>
                    % end
                    </ul>
              </div>
            </section>
        <br>
        % if lot.cur_bid != "None":
            <p style="text-align: center;" class="lot-price">{{lot.cur_bid}}</p>
            <p style="text-align: center;" >{{lot.cur_buyer}}</p>
        % else:
            <p style="text-align: center;" class="lot-price">{{lot.min_bid}}</p>
            <p style="text-align: center;" >Початкова ставка:</p>
        % end
        <br>
        % if lot.end_object_time > now > lot.start_object_time:
        % if user:
        <form action="/login" method="post" class="form">
        <div class="input-container">
        <input id="bid_num" name="bid" class="input" type="number" placeholder=" " />
        <div class="cut"></div>
        <label for="bid_num" class="placeholder">Cтавка</label>
        </div>
         <button style="margin: 15px 0;" type="text" class="submit">Зробити ставку</button>
        </form>
        % else:
        <p style="text-align: center; font-size: 15px;">Щоб зробити ставку, вам потрібно <a href="/login" style="text-decoration: none; color: #39a147;">залогінитись</a></p>
        % end
        % else:
        <p style="text-align: center; font-size: 15px;">На даний момент ви не можете робити ставку. Аукціон уже закінчився або ще не почався.</p>
        %end
        <div class="info" style="margin-top:50px;">
        <p>Опис: {{lot.description}}</p>
        <p>Продавець: {{lot.seller}}</p>
        </div>

    </div>
    <script>
    document.addEventListener('DOMContentLoaded', function() {
    var splide = new Splide( '.splide' );
    splide.mount();});
    </script>