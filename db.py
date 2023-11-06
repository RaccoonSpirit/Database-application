import pyodbc



SERVER = 'DESKTOP-GT00LT4'
DATABASE = 'Military_unit'
username = 'sa'
password = 'Pava01))'


connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={username};PWD={password}'
print(connectionString )
connection = pyodbc.connect(connectionString) 


cursor = connection.cursor()
def user():
  mySQLQuery = (
    """SELECT TOP (1000) [Id_Weapon]
      ,[Type_of_weapon]
      ,[Quantity]
      ,[Name]
  FROM [Military_unit].[dbo].[Weapon]""")
  
  res  = cursor.execute(mySQLQuery).fetchall()
  return res
print(user())


