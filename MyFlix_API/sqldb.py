from flask import current_app, g, jsonify
from werkzeug.local import LocalProxy
import pymysql
from bson.json_util import dumps

def get_sqldb():

    if 'sqldb' not in g:
        g.sqldb = pymysql.connect(host=current_app.config.get('MYSQL_DATABASE_HOST'), user=current_app.config.get('MYSQL_DATABASE_USER'), password=current_app.config.get('MYSQL_DATABASE_PASSWORD'), database=current_app.config.get('MYSQL_DATABASE_DB'))
    return g.sqldb

# Use LocalProxy to read the global db instance with just `db`
sqldb = LocalProxy(get_sqldb)

def verify(username, password):
    with sqldb.cursor() as cursor:
        sql = "Select * FROM login WHERE username=%s and pass=%s"
        cursor.execute(sql, (username, password))
        results = cursor.fetchone()

        if results is not None:
            return results
        else:
            return False