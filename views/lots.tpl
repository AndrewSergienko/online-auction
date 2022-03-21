%rebase('base.tpl')
    % for lot in lots:
        % if now < lot.start_object_time:
            <div class="lot didnt-start">
        % elif now < lot.end_object_time:
            <div class="lot began">
        % else:
            <div class="lot over">
        % end

        % if lot.picture_path:
            <img src="media/{{lot.picture_path}}">
        % else:
            <img src="media/{{default_picture}}">
        % end

        <div class="lot-info">
            <div class="lot-header">
                <h2>{{ lot.title }}</h2>
            </div>
            <div class="lot-footer">
                <p class="seller">Продавець: <a id="seller-user">{{ lot.seller.firstname }} {{ lot.seller.lastname }}</a></p>
                <div>
                    <p id='start-price' class="price">{{ lot.min_bid }}</p>
                    <p style="font-size: 15px; text-align: center">Cтавка</p>
                </div>
                <div>
                    <p id='cur-price' class="price">10:00</p>
                    <p style="font-size: 15px; text-align: center">До кінця</p>
                </div>
            </div>
        </div>
    </div>