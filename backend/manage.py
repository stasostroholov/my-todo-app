import os
from todo.app import create_app
from todo.extensions import db
from flask_migrate import Migrate

# Створюємо екземпляр додатка
app = create_app()

# Ініціалізуємо міграції для цього додатка
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()