# Описание
Созданный своими руками исключительный говнокод.

А так же заметки, полезные команды и всё что может пригодится в коддинге.

## Команды

### Git

git rm -r --cached example_folder   - удаляет репозиторий из отслеживания в git после добавления папки в gitignore

### Docker

docker-compose up --build   - сборка оркестра с перебилдом всех образов

docker container exec -it container_name bash   - открыть терминал запушенного контейнера

psql -d database_name -U username   - открыть интерфейс psql в контейнере БД