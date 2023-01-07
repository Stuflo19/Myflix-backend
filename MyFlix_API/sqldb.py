from flask import current_app, g, jsonify
from werkzeug.local import LocalProxy
import pymysql
from bson.json_util import dumps
import bcrypt

def get_sqldb():

    if 'sqldb' not in g:
        g.sqldb = pymysql.connect(host=current_app.config.get('MYSQL_DATABASE_HOST'), user=current_app.config.get('MYSQL_DATABASE_USER'), password=current_app.config.get('MYSQL_DATABASE_PASSWORD'), database=current_app.config.get('MYSQL_DATABASE_DB'))
    return g.sqldb

# Use LocalProxy to read the global db instance with just `db`
sqldb = LocalProxy(get_sqldb)

def verify(username, password):
    with sqldb.cursor() as cursor:
        sql = "Select * FROM login WHERE username=%s"
        cursor.execute(sql, (username))
        results = cursor.fetchone()
        
        # Entered password
        enteredPassword = password.encode('utf-8')
        
        if bcrypt.checkpw(enteredPassword, bytes(results[2], 'utf-8')):
            return True
        else:
            return False

def create(username, password):
    with sqldb.cursor() as cursor:
        password = password.encode('utf-8')
        hashedPwd = bcrypt.hashpw(password, bcrypt.gensalt(10)) 
        
        sql = "INSERT INTO login (username, pass) VALUES (%s,%s)"
        values = (username, str(hashedPwd, 'UTF-8'))
        result = cursor.execute(sql, values)

        # Comitting the change to the DB
        sqldb.commit()
        if result:
            return True
        else:   
            return False