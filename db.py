import pymysql
from config import host, user, password, db_name

products = []

try:
    connection = pymysql.connect(
        host = host,
        port = 3306,
        user = user,
        password = password,
        database = db_name,
        cursorclass = pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    
    try:
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `airports`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()
            for row in rows:
                row['latitude'] = float(row['latitude'])
                row['longitude'] = float(row['longitude'])
                products.append(row)
    finally:
        connection.close()
        
except Exception as ex:
    print(ex)
    print("Connection refused...")