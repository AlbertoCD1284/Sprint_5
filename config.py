class dev():
    DEBUG = True
    SECRET_KEY="BETO1284"
    DATABASE={
        'name':'database/data.db',
        'engine':'peewee.SqliteDatabase'
    }

class prod():
    DEBUG = False
    SECRET_KEY="adgsrt"
    DATABASE={
        'name':'notisaurio.sqlite3',
        'engine':'peewee.MysqlDatabase',
        'host':'url.donde.esta.mi.db.com',
        'user': 'beto',
        'passwd':'asdgsoifgv'
    }