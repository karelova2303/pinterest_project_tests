<h1> Проект по тестированию web-приложения <a target="_blank" href="https://ru.pinterest.com/">"Pinterest"</a>
</h1>

![This is an image](/resources/images/pin_logo.png)


<h3> Список UI проверок:</h3>

### Проверки, реализованные в автоматизированных тестах
- [x] Проверка авторизации пользователя
  - Успешная авторизация пользователя через email
  - Разлогинивание пользователя
- [x] Проверка профиля пользователя
  - Проверка кликабельнсти иконок общего доступа
  - Проверка перехода на вкладку "Доски"
  - Проверка перехода на вкладку "Пины"
  - Открытие страницы публичного профиля
  - Редактирование профиля
- [x] Проверка строки поиска
  - Поиск контента по введенному значению
  - Поиск контента при выборе из меню "Идеи для вас"
  - Поиск с установленным фильтром

### Проверки, реализованные в ручных тестах
- [x] Проверка авторизации пользователя через Facebook
- [x] Проверка авторизации пользователя через Google
- [x] Проверка неуспешной авторизации с пустыми полями логин / пароль
- [x] Изменение персональных данных

----
### Проект реализован с использованием:
<div align="center">
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/python-original-wordmark.svg" 
    title="Python" alt="Python" width="40" height="40"/>&nbsp;
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/pytest-original-wordmark.svg" 
    title="Pytest" alt="Pytest" width="45" height="45"/>&nbsp; 
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/selenium-original1.svg" 
    title="Selenium" alt="Selenium" width="40" height="40"/>&nbsp;  
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/selene.png" 
    title="Selene" alt="Selene" width="50" height="50"/>&nbsp;
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/selenoid1.png" 
    title="Selenoid" alt="Selenoid" width="40" height="40"/>&nbsp; 
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/pycharm-original.svg" 
    title="PyCharm" alt="PyCharm" width="40" height="40"/>&nbsp;    
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/jenkins-original.svg" 
    title="Jenkins" alt="Jenkins" width="40" height="40"/>&nbsp;
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/Allure.svg" 
    title="Allure Report" alt="Allure Report" width="40" height="40"/>&nbsp;
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/AllureTestOps.png" 
    title="Allure TestOps" alt="Allure TestOps" width="40" height="40"/>&nbsp;
  <img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/telegram1.png" 
    title="Telegram" alt="Telegram" width="40" height="40"/>&nbsp;
<img src="https://github.com/karelova2303/karelova2303/blob/main/media/icons/Jira.png" 
    title="Jira" alt="Jira" width="40" height="40"/>&nbsp;
</div>

----
### Локальный запуск

1. Склонировать репозиторий
2. Установить зависимости командой `pip install -r requirements.txt`
3. Открыть проект в PyCharm, установить интерпретатор
4. Создать `.env` файл, пример файла - `.env.example`, находится в корне проекта
5. Запустить тесты в командной строке:
```bash
pytest --browser_version={BROWSER_VERSION} 
```

> [!IMPORTANT]
> 
> Параметр `--browser_version` - версия браузера Chrome (128.0, 127.0), по умолчанию 128.0

----
### Удаленный запуск автотестов выполняется на сервере Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/019-karelova2303-ui_pinterest_tests/">_**Ссылка на сборку в Jenkins**_</a>


#### Для запуска автотестов в Jenkins

1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/019-karelova2303-ui_pinterest_tests/">проект</a>
2. Выбрать пункт `Build with Parameters`
3. Выбрать параметры - `BROWSER_VERSION`
3. Нажать кнопку `Build`

![jenkins job main page](/resources/images/Jenkins_job_main_page.png)


----
### Allure отчет

#### Формирование отчета:
>-  локальный запуск: ввести в командной строке `allure serve allure-results`
>-  запуск через Jenkins: кликнуть кнопку `Allure Report` в боковом меню 

#### Результаты запусков
![This is an image](/resources/images/allure_report_overview.png)
![This is an image](resources/images/allure_report_graphs.png)



----
### Интеграция с Allure TestOps

> <a target="_blank" href="https://allure.autotests.cloud/project/4777/dashboards">_**Ссылка на проект в Allure TestOps**_</a>

#### Пример dashboard с общими результатами тестирования
![This is an image](/resources/images/allure_TestOps_test_dashboard_all.png)

#### Общий список всех тест-кейсов
![This is an image](/resources/images/allure_TestOps_test_cases.png)

#### Автоматизированные и ручные тесты хранятся в одной директории 
![This is an image](/resources/images/allure_TestOps_test_manual_and_auto.png)

#### Пример отчёта выполнения одного из автотестов
![This is an image](/resources/images/example_autotests_allure_TestOps.png)

#### Пример dashboard с результатами запуска
![This is an image](/resources/images/allure_TestOps_dashboard_ex.png)

#### История запуска тестовых наборов
![This is an image](/resources/images/allure_TestOps_launches.png)

----
### Интеграция с Jira
> <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-1463">_**Ссылка на задачу в Jira**_</a>

![This is an image](/resources/images/jira.png)

----
### Оповещение о результатах прогона тестов в Telegram
![This is an image](/resources/images/tg_notification.png)

----

### Пример видео прохождения ui-автотеста
<p align="center">
    <img title="Video" src="/resources/video/autotest_ui.gif">
</p>