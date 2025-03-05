# Описание
Созданный своими руками исключительный <del>говнокод</del> суперкод

А так же заметки, полезные команды и всё что может пригодится в коддинге.

## Команды

### FastAPI

**pip install fastapi==0.78.0** - *установка фреймвора(версия опционально, на ней учил яндекс)*
**pip install "uvicorn[standard]==0.17.6"** - *установка веб сервера uvicorn*
**pip install python-multipart==0.0.5** - *библиотека  python-multipart для работы с формами*

**uvicorn form:app** - *запустить приложение app из файла form.py*
**uvicorn form:app --reload --port 8001** - *запустить приложение в режиме "обновления" и на порте 8001*

### Git

**git rm -r --cached example_folder**   *удаляет репозиторий из отслеживания в git после добавления папки в gitignore*

### Docker

**docker-compose up --build**   *сборка оркестра с перебилдом всех образов*

**docker container exec -it container_name bash**   *открыть терминал запушенного контейнера*

**psql -d database_name -U username**   *открыть интерфейс psql в контейнере БД*

### Gunicorn

**pip install gunicorn==20.1.0**  *установка WSGI*

**gunicorn --bind 0.0.0.0:8000 backend.wsgi**  *запуск WSGI сервера*

**which gunicorn**   *узнать путь до gunicorn*

**sudo systemctl start/stop/restart gunicorn** *команды для запуска процессов gunicorn*

### Nginx

**sudo ufw allow 'Nginx Full'** *активирует разрешение принимать запросы на порты 80 и 443.*

**sudo ufw allow OpenSSH** *активирует разрешение для порта 22*

**sudo ufw enable**  *включить фаервол*

**sudo ufw status** *проверить статус фаервол*

**sudo nano /etc/nginx/sites-enabled/default** *открыть файл конфигурации сервера*

**sudo nginx -t** *проверка конфигурации Nginx*

**sudo systemctl reload nginx** *перезагрузка конфигурации Nginx*

**/var/log/nginx/access.log** *логи всех запросов*

**/var/log/nginx/error.log** *логи ошибочных запросов*

**sudo tail /var/log/nginx/access.log** *просмотр лога последних запросов*

**cd /etc/nginx/sites-enabled/** *файл конфигурации nginx*

**sudo snap install --classic certbot** *установка пакета certbot*
*При успешной установке пакета в терминале выведется:
certbot 2.3.0 from Certbot Project (certbot-eff✓) installed*

*Создание ссылки на certbot в системной директории,
чтобы у пользователя с правами администратора был доступ к этому пакету.*
**sudo ln -s /snap/bin/certbot /usr/bin/certbot**

**sudo certbot certificates** *узнать актуальный статус сертификата*

**sudo certbot renew --dry-run**     *убедиться что сертификат будет обновляться автоматически*

**sudo certbot renew --pre-hook "service nginx stop" --post-hook "service nginx start"**    *ручное обновление сертификата*

### Scrapy

**scrapy startproject my_project** *создать scrapy проект*

**scrapy genspider название_паука url_адрес** *сгенерировать нового паука*

**scrapy crawl my_spider** *запуск паука*

**scrapy crawl my_spider -O название_файла.формат** *запуск паука и перезапись(заглавное -O) данных в файл (csv, json, xml)*


