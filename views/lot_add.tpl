%rebase('base.tpl')
    <form action="/lot/add/" method="post" class="form" enctype="multipart/form-data">
      <div class="title">Лот</div>
      <div class="subtitle">Створити новий лот.</div>
      <div class="input-container ic1">
        <input id="lot-title" name="title" class="input" type="text" placeholder=" " />
        <div class="cut"></div>
        <label for="lot-title" class="placeholder">Заголовок</label>
      </div>
      <div class="input-container ic3">
        <textarea id="description" name="description" class="input" placeholder=" "></textarea>
        <div class="cut"></div>
        <label for="description" class="placeholder">Опис</label>
      </div>
      <div class="input-container ic2">
        <input id="min_bid" name="min_bid" class="input" type="number" placeholder=" " />
        <div class="cut" style="width: 130px;"></div>
        <label for="title" class="placeholder">Мінімальна ставка</label>
      </div>
      <div class="input-container ic2">
        <input id="start_date" name="start_date" class="input" type="datetime-local"/>
        <div class="cut"></div>
        <label for="start_date" class="placeholder">Початок</label>
      </div>
      <div class="input-container ic2">
        <input id="end_date" name="end_date" class="input" type="datetime-local"/>
        <div class="cut"></div>
        <label for="end_date" class="placeholder">Кінець</label>
      </div>
      <div class="input-container ic2">
        <input id="files" name="files" class="input" type="file" multiple="multiple"/>
        <div class="cut"></div>
        <label for="files" class="placeholder">Фотографії</label>
      </div>
      <button type="text" class="submit">Створити</button>
    </form>