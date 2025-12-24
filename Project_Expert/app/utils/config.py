import os

class Config:
    SECRET_KEY = 'dev_secret_key' # អាចដាក់អក្សរអ្វីក៏បានសម្រាប់ការពារ Form
    
    # កំណត់ទីតាំង Database (rice_db.sqlite)
    # យើងកំណត់ឱ្យវាបង្កើតនៅក្នុង folder 'instance'
    basedir = os.path.abspath(os.path.dirname(__file__))
    
    # ថយក្រោយ ២ ដំណាក់ (ពី utils -> app -> root folder)
    root_path = os.path.abspath(os.path.join(basedir, '../../'))
    
    # បង្កើត Database ឈ្មោះ rice_db.sqlite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(root_path, 'instance', 'rice_db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False