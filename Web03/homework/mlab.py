import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds251747.mlab.com:51747/movie

host = "ds251747.mlab.com"
port = 51747
db_name = "movie"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)
