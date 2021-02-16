import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DATABASES = {
    'default': {
        #=====Enable Only Making Project Live on Heroku====
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'ENGINE':'django.db.backends.mysql',
        # 'NAME':'student_management_system',
        # 'USER':'student_mgmt',
        # 'PASSWORD':'Owuradarko11*',
        # 'HOST':'localhost',
        # 'PORT':'3306'
    }
}