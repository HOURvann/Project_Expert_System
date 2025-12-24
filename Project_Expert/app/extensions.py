from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# បង្កើតជើង Database (SQLAlchemy)
db = SQLAlchemy()

# បង្កើតជើង Migrate (សម្រាប់កែប្រែ Database ថ្ងៃក្រោយ)
migrate = Migrate()