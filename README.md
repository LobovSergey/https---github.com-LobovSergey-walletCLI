WalletApp (CLI) 1.3.2.1
Электронный кошелек, для работы со своей историей операций: поиск, редактирование, сортировка, списания и пополнения.
Приложение поддерживает несколько аккаунтов, но одновременно может работать только с 1 авторизованным пользователем.
Все опреации будут осуществляться терез терминал
Для того чтобы начать пользоваться:

1. Клонируйте репозитоий https://github.com/LobovSergey/https---github.com-LobovSergey-walletCLI.git
2. Создайте виртуальное окружение с помощью команды python -m venv .venv. Активируйте
3. Установите все зависимости, находясь в корнейвой папке проекта
4. Запустите main_app.py  в корневой папке проекта
5. enjoy!

Для работы с данным приложением вам понадобиться зарегистрироваться в система, после чего у вас будет открыт электронный счет. Все операции с пополнением и снятием доступны в главном меню личного кабинета, а операции с историей (поиск, редактирование, сортировка) доступны из меню "История операций".
Ваш аккаунт будет работать с локальной в БД , созданной автоматически в корневой папке проекта. Данный файл будет актуален только до того момента, когда вы завершите ход работы программы. При новом запуске данные будут перезаписаны и все ваши записи будут утеряны.
