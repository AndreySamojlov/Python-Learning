import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')
WEATHER_DEFAULT_CITY = 'Moscow,Russia'
WEATHER_API_KEY = 'a1ce4fc4dde14dd588b132420192509'
WEATHER_URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'


#set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run