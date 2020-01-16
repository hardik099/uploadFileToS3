import sqlalchemy as create_engine
from sqlalchemy.ext.declarative import declarative_base
from numpy import genfromtxt

user = 'root'
passw = 'mysqltest'
host =  '127.0.0.1'  # either localhost or ip e.g. '172.17.0.2' or hostname address
port = 3306
database = 'employee'

mysql_engine = create_engine('mysql+pymysql://' + user + ':' + passw + '@' + host + ':' + str(port) + '/' + database , echo=False)

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employee_tables'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    employee_id = sqlalchemy.Column(sqlalchemy.Integer)
    firstname = sqlalchemy.Column(sqlalchemy.String(length=50))
    middlename = sqlalchemy.Column(sqlalchemy.String(length=50))
    lastname = sqlalchemy.Column(sqlalchemy.String(length=50))

    def __repr__(self):
        return "<User(employee_id='{0}',firstname='{1}', middlename='{2}', lastname='{3}')>".format(
            self.firstname, self.middlename, self.lastname)



def createEmployeeTable():
    Base.metadata.create_all(mysql_engine)
    Session = sqlalchemy.orm.sessionmaker()
    Session.configure(bind=mysql_engine)
    session = Session()
    return session

def saveInDB(upload_dir,file_name):



def saveDbtest(upload_dir,file_name):
    data = Load_Data(upload_dir,file_name) #Get data from CSV

    session = createEmployeeTable()

    for i in data:
        employee = {
            'employee_id': i[0],
            'firstname' : i[1],
            'middlename' : i[2],
            'lastname' : i[3]
        }
        Add_Record(session, employee)

def readAllFromDB():


def readBasedOnIdFromDB(employee_id):



def Add_Record(session, employee):
    record = Employee(firstname=employee.firstname, middlename=employee.middlename, lastname=employee.lastnames)
    session.add(recordw)
    session.commit()


def Load_Data(upload_dir,file_name):
    data = genfromtxt(upload_dir+file_name, delimiter=',', skiprows=1, converters={0: lambda s: str(s)})
    return data.tolist()



