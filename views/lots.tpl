%rebase('base.tpl')
    % for lot in lots:
        % if now < lot.start_object_time:
            <div class="lot didnt-start">
        % elif now < lot.end_object_time:
            <div class="lot began">
        % else:
            <div class="lot over">
        % end

        % if lot.avatar:
            <img style="width: 167px; height: 125px; object-fit: cover;" src="media/lots/{{lot.id}}/{{lot.avatar}}">
        % else:
            <img style="width: 167px; height: 125px; object-fit: cover;" src="media/{{default_picture}}">
        % end

        <div class="lot-info" style="cursor: pointer;" onclick="goto_info({{ lot.id }})">
            <div class="lot-header">
            <h2>{{ lot.title }}</h2>
            </div>
            <div class="lot-footer">
                <div><p class="seller">Продавець: <a id="seller-user">{{ lot.seller.firstname }} {{ lot.seller.lastname }}</a></p></div>
                <div>
                    <p id='start-price' class="price">{{ lot.min_bid }}</p>
                    <p style="font-size: 15px; text-align: center">Cтавка</p>
                </div>
                <div>
                    % if now < lot.start_object_time:
                    % hour, minute = lot.start_object_time.hour, lot.start_object_time.minute
                    % time = f"{hour if hour != 0 else '00'}:{minute if minute != 0 else '00'}"
                    <p id='cur-price' class="price">{{ time }}</p>
                    <p style="font-size: 15px; text-align: center">Початок</p>

                    % elif now < lot.end_object_time:
                    % hour, minute = lot.end_object_time.hour, lot.end_object_time.minute
                    % time = f"{hour if hour != 0 else '00'}:{minute if minute != 0 else '00'}"
                    <p id='cur-price' class="price">{{ time }}</p>
                    <p style="font-size: 15px; text-align: center">Кінець</p>

                    % else:
                    % hour, minute = lot.end_object_time.hour, lot.end_object_time.minute
                    % time = f"{hour if hour != 0 else '00'}:{minute if minute != 0 else '00'}"
                    <p id='cur-price' class="price">{{ time }}</p>
                    <p style="font-size: 15px; text-align: center">Закінчився</p>
                    % end
                </div>
            </div>
        </div>
    </div>
    % end
    <script>
    function goto_info(id){
            window.location = '/lot/' + id
        }
    </script>