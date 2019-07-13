import sqlalchemy.dialects.mysql as MySQLdb

db = MySQLdb.connect(host="rc1b-3pcr6ef885dd1gr2.mdb.yandexcloud.net",  port=3306, user="hooszydevops", passwd="<password>",
                     db="diplom_schema", ssl={'ca': '~/.mysql/root.crt'})
cursor=db.cursor()
# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")
# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Database version : %s " % data)
print('what the fox say')
# disconnect from server
db.close()