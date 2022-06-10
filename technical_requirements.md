# 1. Цель проекта  

Цель проекта - разработать web-приложение для отслеживания динамики цен на популярные товары повседневного спроса в различных онлайн магазинах. Так же будет реализованна возможность пользователям добавлять свои товары для отслеживания цен из поддерживаемых магазинов. Так же будет реализована интеграция с телеграм, для отслеживания сильного изменения цены и быстрого добавления или удаления товаров из пользовательского списка.  

# 2. Описание системы

Система состоит из следующих функциональных блоков: 

1. Регистрация, аутентификация и авторизация пользователей
2. Парсер цен онлайн магазинов
3. Вывод информации о изменении цены на товары первой необходимости
4. Вывод информации об изменении цены на товары добавленные пользователем
5. Вывод графиков с изменением цен на товары за весь приод 
6. Функционал интегации с телеграм
7. Уведомление о сильном изменении цены для тех кто подписался 

## 2.1 Типы пользователей  

В системе находится три типа пользователей: администратор, зарегистрированный пользователь, гость. Администратор может изменять и добавлять товары для отслеживания. Пользователь может добавлять собственные товары для отслеживания и смотреть изменения цен. Гость может только смотреть изменения цен на товары первой необходимости. 

## 2.2 Регистрация

Регистрация пользователей выполняется через web-форму. Для регистрации запрашиваются следующие поля:

- email
- пароль
- номер телефона для интеграции с телеграм

После ригистрации пользователю приходит email со ссылкой на активацию. Так же пользователи имеют возможность сменить и восстановить пароль. 

## 2.3 Функционал пользователей

- Восстановление и смена пароля
- Добавление товаров из поддерживаемых источников для отслеживания 
- Изменения пользовательского названия товара для лучшей идентификации его в списке 
- Удаление товаров из отслеживания 
- Подписка в телеграм боте на рассылку на сильное изменении цены (сделать выбор того сколько процентов разницы имеет значение)

## 2.4 Функционал интеграции с телеграм 

- Добавление новых товаров для отслеживания.
- Уведомление о сильном изменении цены. 

## 2.5 Список поддерживаемых магазинов 

- Перекресток 
- Ozon 
- Вайлдберрис 

## 2.6 Список собираемых данных о товарах 

- Название 
- Категория 
- Маркетплейс 
- Минимальная цена
- Максимальная цена 
- Процент изменения цены по сравнению с прошлой проверкой 

# 3. Предлагаемый стек технологий

- Бэкенд: 
    * Язык Python 
    * Фреймворк Django 
    * Фреймворк Django Fast Api
    * БД PostgresSQL
    * Django Orm 
    * Aiogram для интеграции с Telegram 
    * Docker для контейнеризации 
- Фронтенд: 
    * Bootstrap 4
    * React

# 4. Требования к дизайну

Минимализм, лаконичность. Чем то похоже на приложение отслеживания котировок акций. Только вместо акций товары. В мобильном режиме краткая информация стопкой, по тапу на товар открывается информация за период и кнопки управления для пользовательских товаров. В десктопном режиме вся информация доступна на одном экране. Подарожавшие товары с красной обводкой, подешевевшие с зеленой, не изменившиеся с серой.   
Возможность установки темной и светлой темы. Наверху логотип и кнопка сменты темы.  
Ниже кнопки сортировки списка товаров, самый подорожавший товар (%), самый подешевевший (%), алфавит возрастание и убывание. 
В нижней части кнопка перехода на страницу своих товаров.  
В подвале данные об авторах и ссылка на Github проекта. 