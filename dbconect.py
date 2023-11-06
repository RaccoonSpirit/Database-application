import pyodbc

class dbworker:
    def __init__(self, database):
      SERVER = '192.168.0.5'
      DATABASE = database
      username = 'sa'
      password = 'Pava01))'
      connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={username};PWD={password}'
      self.connection = pyodbc.connect(connectionString) 
      self.cursor = self.connection.cursor()
    def get(self):
      with self.connection:
        mySQLQuery = ("""SELECT TOP (1000) [Id_Weapon],[Type_of_weapon],[Quantity],[Name] FROM [Military_unit].[dbo].[Weapon]""")
        result = self.cursor.execute(mySQLQuery).fetchall()
        return result
db = dbworker('Military_unit')
print(db.get())