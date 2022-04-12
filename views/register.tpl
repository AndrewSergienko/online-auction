%rebase('base.tpl')
    <form action="/register" method="post">
        <label>Username:<input name="username"></label><br>
        <label>Password:<input name="password" type="password"></label><br>
        <label>First name:<input name="firstname"></label><br>
        <label>Last name:<input name="lastname"></label><br>
        <label>Phone:<input name="phone_number"></label><br>
        <input type="submit" value="Register">
    </form>
