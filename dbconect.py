import pyodbc

class dbworker:
    def __init__(self, database:str):
      SERVER = '192.168.0.5'
      DATABASE = database
      username = 'sa'
      password = 'Pava01))'
      connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={username};PWD={password}'
      self.connection = pyodbc.connect(connectionString) 
      self.cursor = self.connection.cursor()
    def get_serviceman(self):
      with self.connection:
        mySQLQuery = ('SELECT FIO, Date_of_birth, Branch_number, Rank FROM Servicemans')
        res = self.cursor.execute(mySQLQuery).fetchall()
        result = [list(item) for item in res]
        return result
    def get_weapon(self):
      with self.connection:
        mySQLQuery = ('SELECT Type_of_weapon, Quantity, Name FROM Weapon')
        res = self.cursor.execute(mySQLQuery).fetchall()
        result = [list(item) for item in res]
        return result
    def search_serviceman(self, text):
      with self.connection:
        mySQLQuery = ('SELECT FIO, Date_of_birth, Branch_number, Rank FROM Servicemans WHERE FIO = ?')
        res = self.cursor.execute(mySQLQuery, (text,)).fetchall()
        if res == []:
          mySQLQuery = ('SELECT Type_of_weapon, Quantity, Name FROM Weapon WHERE Name = ?')
          res = self.cursor.execute(mySQLQuery, (text,)).fetchall()
        result = [list(item) for item in res]
        return result
    def get_serviceman_weapon(self):
      with self.connection:
        mySQLQuery = ('SELECT Type_of_weapon, Quantity, Name FROM Weapon WHERE Name = ?')
        res = self.cursor.execute(mySQLQuery).fetchall()
        result = [list(item) for item in res]
        return result
         

        
      
     

