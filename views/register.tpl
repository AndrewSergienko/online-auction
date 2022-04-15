%rebase('base.tpl')
    <form action="/register" method="post" class="form">
      <div class="title">Вітаю</div>
      <div class="subtitle">Створіть свій аккаунт.</div>
      <div class="input-container ic1">
        <input id="username" name="username" class="input" type="text" placeholder=" " />
        <div class="cut"></div>
        <label for="username" class="placeholder">Логін</label>
      </div>
      <div class="input-container ic2">
        <input id="password" name="password" class="input" type="password" placeholder=" " />
        <div class="cut"></div>
        <label for="password" class="placeholder">Пароль</label>
      </div>
      <div class="input-container ic2">
        <input id="firstname" name="firstname" class="input" type="text" placeholder=" " />
        <div class="cut"></div>
        <label for="password" class="placeholder">Ім'я</label>
      </div>
      <div class="input-container ic2">
        <input id="lastname" name="lastname" class="input" type="text" placeholder=" " />
        <div class="cut"></div>
        <label for="password" class="placeholder">Фамилія</label>
      </div>
      <div class="input-container ic2">
        <input id="phone_number" name="phone_number" class="input" type="text" placeholder=" " />
        <div class="cut"></div>
        <label for="password" class="placeholder">Телефон</label>
      </div>
      <button type="text" class="submit">Увійти</button>
    </form>
