# WEB-API


# Installation


# Development


# Linters


# Migrations

* Обонвление базы до последней версии. Вместо `head` можно указать любой `revision` из `src/beta/infrastructure/data_access/migrations/versions`
  * ```shell
    alembic upgrade head 
    alembic upgrade c3da229ef15e
    ```

* Создание новой миграции после изменения схемы базы данных
  * ```shell
    alembic revision --autogenerate -m "Migration comment"`
    ```

---


