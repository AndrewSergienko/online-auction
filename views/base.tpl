<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Онлайн аукціон</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <div class="header">
        <a style="text-decoration: none;"href="/"><div class="logo">Онлайн Аукціон</div></a>
        <ul class="menu">
            % if user:
            <li><a style="text-decoration: none;" href="/lot/add/"><div class="abtn add-lot">Створити лот</div></a></li>
            <li><a style="text-decoration: none;" href="/logout"><div class="abtn out">Вийти</div></a></li>
            % else:
            <li><a style="text-decoration: none;" href="/login"><div class="abtn in">Увійти</div></a></li>
            % end
        </ul>
    </div>
    <div class="main-content">
        {{!base}}
    </div>
</body>
</html>