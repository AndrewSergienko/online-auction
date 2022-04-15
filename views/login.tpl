%rebase('base.tpl')
    <form action="/login" method="post" class="form">
      <div class="title">Вітаю</div>
      <div class="subtitle">Увійдіть у ваш акаунт.</div>
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
      <button type="text" class="submit">Увійти</button>
    </form>