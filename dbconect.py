import pyodbc

class dbworker:
    def __init__(self, database:str, server:str, username:str, password:str):
      connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
      self.connection = pyodbc.connect(connectionString) 
      self.cursor = self.connection.cursor()
    def get_serviceman(self) -> list:
      with self.connection:
        mySQLQuery = ('SELECT FIO, Date_of_birth, Branch_number, Rank FROM Serviceman')
        res = self.cursor.execute(mySQLQuery).fetchall()
        result = [list(item) for item in res]
        return result
    def get_weapon(self) -> list:
      with self.connection:
        mySQLQuery = ('SELECT Type_of_weapon, Quantity, Name FROM Weapon')
        res = self.cursor.execute(mySQLQuery).fetchall()
        result = [list(item) for item in res]
        return result
    def search(self, text:str) -> list:
      with self.connection:
        mySQLQuery = ('SELECT FIO, Date_of_birth, Branch_number, Rank FROM Serviceman WHERE FIO = ?')
        res = self.cursor.execute(mySQLQuery, (text,)).fetchall()
        if res == []:
          mySQLQuery = ('SELECT Type_of_weapon, Quantity, Name FROM Weapon WHERE Name = ?')
          res2 = self.cursor.execute(mySQLQuery, (text,)).fetchall()
          result = [list(item) for item in res2]
          return result, 'Weapon'
        else: 
          result = [list(item) for item in res]
          return result, 'Serviceman' 
    def get_columns(self, name:str) -> list:
      with self.connection:
        mySQLQuery = ('SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = ? AND COLUMN_NAME NOT IN (SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE WHERE TABLE_NAME = ?);')
        res = self.cursor.execute(mySQLQuery, (name,name)).fetchall()
        result = [item[0] for item in res]
        return result
    def get_weapon_and_serviceman(self) -> list:
      with self.connection:
        mySQLQuery = ('SELECT Serviceman.FIO,Serviceman.Rank , Weapon.Type_of_weapon, Weapon.Name FROM Weapon_and_serviceman JOIN Serviceman ON Serviceman.id_Serviceman = Weapon_and_serviceman.id_Serviceman JOIN Weapon ON Weapon.id_Weapon = Weapon_and_serviceman.id_Weapon;')
        res = self.cursor.execute(mySQLQuery).fetchall()
        result = [list(item) for item in res]
        return result

        
      
     

