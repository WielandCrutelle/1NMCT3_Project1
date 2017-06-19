class DbClass:
    def __init__(self):
        import mysql.connector as connector

        self.__dsn = {
            "host": "localhost",
            "user": "root",
            "passwd": "root",
            "db": "project1"
        }

        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()

    def gettemp(self):
        sqlQuery = "SELECT avg(Data) FROM project1.meting where SensorID = 1 group by date(DatumTijd)"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def gettempdate(self):
        sqlQuery = "SELECT DatumTijd, Data FROM project1.meting where SensorID = 1"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getdruk(self):
        sqlQuery = "SELECT avg(Data) FROM project1.meting where SensorID = 2 GROUP by date(DatumTijd)"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getdrukdate(self):
        sqlQuery = "SELECT DatumTijd, Data FROM project1.meting where SensorID = 2"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getvocht(self):
        sqlQuery = "SELECT avg(Data) FROM project1.meting where SensorID = 3 GROUP by date(DatumTijd)"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    def getvochtdate(self):
        sqlQuery = "SELECT DatumTijd, Data FROM project1.meting where SensorID = 3"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result
