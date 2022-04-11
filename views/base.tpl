<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Онлайн аукціон</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <div class="header">
        <div class="logo">Онлайн Аукціон</div>
        <ul class="menu">
            <li>Увійти</li>
            <li>{{request.auth}}</li>
        </ul>
    </div>
    <div class="main-content">
        {{!base}}

    </div>
</body>
</html>