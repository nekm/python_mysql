from mysql.connector import MySQLConnection , Error
from python_mysql_dbconfig import read_db_config
 
def insert_query ( employeeNumber, lastName , firstName, extension, email, officeCode, reportsTo, jobTitle ) :
     query = "INSERT INTO employees(employeeNumber,lastName,firstName,extension,email,officeCode,reportsTo,jobTitle) " \
             "VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
     args = ( employeeNumber, lastName , firstName, extension, email, officeCode, reportsTo, jobTitle )
 
     try :
         db_config = read_db_config ( )
         conn = MySQLConnection (**db_config)
 
         cursor = conn.cursor ( )
         cursor.execute ( query , args )
 
         if cursor.lastrowid :
             print ( employeeNumber , cursor.employeeNumber )
         else :
             print ( 'employeeNumber not found' )
 
         conn.commit ( )
     except Error as error :
         print ( error )
 
     finally :
         cursor.close ( )
         conn.close ( )
 
def main ( ) :
   insert_query ( 1709, 'Peritt', 'Pero', 'x2312', 'pperit@classicmodelcars.com', 4, 1102, 'Sales Rep' )
 
if __name__ == '__main__' :
     main ( )