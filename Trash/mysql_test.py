import pymysql as db

connection = db.connect(host="172.22.2.66", db="SMIDDLE2", user="developer", password="Smidle098adm!",
                        cursorclass=db.cursors.DictCursor)

try:

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT ID,DATE_CREATED_UTL  FROM QOS_RESULTS WHERE DELETED = FALSE"
        cursor.execute(sql)
        results = cursor.fetchall()

    with connection.cursor() as cursor:
        # Read a single record
        count = 1
        for result in results:
            id = result['ID']
            new_date =result['DATE_CREATED_UTL'] - (int(86400000/3)*count)
            print(new_date)
            sql = "UPDATE QOS_RESULTS SET DATE_CREATED_UTL = %s WHERE ID = %s"
            cursor.execute(sql, (new_date, id,))
            count +=1
    connection.commit()
finally:
    connection.close()

