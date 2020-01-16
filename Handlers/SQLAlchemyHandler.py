import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table,Column,Integer,String
import glob
import os
from sqlalchemy import MetaData
from sqlalchemy.orm import mapper

user = 'root'
passw = 'mysqltest'
host =  '127.0.0.1'  # either localhost or ip e.g. '172.17.0.2' or hostname address
port = 3306
database = 'employee'

engine=create_engine('mysql+pymysql://' + user + ':' + passw + '@' + host + ':' + str(port) + '/' + database , echo=False)

Session=sessionmaker(bind=engine)
session=Session()

#Map which table in database will be related to each class
Base=declarative_base()

metadata=MetaData(engine)

#Define structure of table
class product_table(object):
    def __init__(self,EMPLOYEE_ID,FIRST_NAME,MIDDLE_NAME,LAST_NAME,GENDER,DATE_OF_BIRTH,DATE_OF_JOINING,WORK_EMAIL,PERSONAL_EMAIL,PERSONAL_ADDRESS,WORK_ADDRESS,EMERGENCY_CONTACT_NAME,EMERGENCY_CONTACT_NUMBER,FATHER_NAME,MOTHER_NAME,SPOUSE_NAME,PAN,HAS_PF,PF_NUMBER,UAN,HAS_ESI,ESI_NUMBER,HAS_LWF,LWF_NUMBER,AADHAR_NUMBER,HAS_PT,PT_NUMBER,MOBILE_NUMBER,PAYMENT_MODE,BANK_NAME,ACCOUNT_NUMBER,IFSC_CODE,DEPT,DESIG,LATEST_ANNUAL_CTC,SALARY_VALID_FROM_DATE,BASIC,HRA,MEDICAL_ALLOWANCE,BONUS,COMMISSION,SPECIAL_ALLOWANCE,EMPLOYER_CONTRI_PF,LTA):
        self.EMPLOYEE_ID=EMPLOYEE_ID
        self.FIRST_NAME=FIRST_NAME
        self.MIDDLE_NAME=MIDDLE_NAME
        self.LAST_NAME=LAST_NAME
        self.GENDER=GENDER
        self.DATE_OF_BIRTH=DATE_OF_BIRTH
        self.DATE_OF_JOINING=DATE_OF_JOINING
        self.WORK_EMAIL=WORK_EMAIL
        self.PERSONAL_EMAIL=PERSONAL_EMAIL
        self.PERSONAL_ADDRESS=PERSONAL_ADDRESS
        self.WORK_ADDRESS=WORK_ADDRESS
        self.EMERGENCY_CONTACT_NAME=EMERGENCY_CONTACT_NAME
        self.EMERGENCY_CONTACT_NUMBER=EMERGENCY_CONTACT_NUMBER
        self.FATHER_NAME=FATHER_NAME
        self.MOTHER_NAME=MOTHER_NAME
        self.SPOUSE_NAME=SPOUSE_NAME
        self.PAN=PAN
        self.HAS_PF=HAS_PF
        self.PF_NUMBER=PF_NUMBER
        self.UAN=UAN
        self.HAS_ESI=HAS_ESI
        self.ESI_NUMBER=ESI_NUMBER
        self.HAS_LWF=HAS_LWF
        self.LWF_NUMBER=LWF_NUMBER
        self.AADHAR_NUMBER=AADHAR_NUMBER
        self.HAS_PT=HAS_PT
        self.PT_NUMBER=PT_NUMBER
        self.MOBILE_NUMBER=MOBILE_NUMBER
        self.PAYMENT_MODE=PAYMENT_MODE
        self.BANK_NAME=BANK_NAME
        self.ACCOUNT_NUMBER=ACCOUNT_NUMBER
        self.IFSC_CODE=IFSC_CODE
        self.DEPT=DEPT
        self.DESIG=DESIG
        self.LATEST_ANNUAL_CTC=LATEST_ANNUAL_CTC
        self.SALARY_VALID_FROM_DATE=SALARY_VALID_FROM_DATE
        self.BASIC=BASIC
        self.HRA=HRA
        self.MEDICAL_ALLOWANCE=MEDICAL_ALLOWANCE
        self.BONUS=BONUS
        self.COMMISSION=COMMISSION
        self.SPECIAL_ALLOWANCE=SPECIAL_ALLOWANCE
        self.EMPLOYER_CONTRI_PF=EMPLOYER_CONTRI_PF
        self.LTA=LTA

    def __repr__(self):
        return f'{self.EMPLOYEE_ID,self.FIRST_NAME,self.MIDDLE_NAME,self.LAST_NAME,self.GENDER,self.DATE_OF_BIRTH,self.DATE_OF_JOINING,self.WORK_EMAIL,self.PERSONAL_EMAIL,self.PERSONAL_ADDRESS,self.WORK_ADDRESS,self.EMERGENCY_CONTACT_NAME,self.EMERGENCY_CONTACT_NUMBER,self.FATHER_NAME,self.MOTHER_NAME,self.SPOUSE_NAME,self.PAN,self.HAS_PF,self.PF_NUMBER,self.UAN,self.HAS_ESI,self.ESI_NUMBER,self.HAS_LWF,self.LWF_NUMBER,self.AADHAR_NUMBER,self.HAS_PT,self.PT_NUMBER,self.MOBILE_NUMBER,self.PAYMENT_MODE,self.BANK_NAME,self.ACCOUNT_NUMBER,self.IFSC_CODE,self.DEPT,self.DESIG,self.LATEST_ANNUAL_CTC,self.SALARY_VALID_FROM_DATE,self.BASIC,self.HRA,self.MEDICAL_ALLOWANCE,self.BONUS,self.COMMISSION,self.SPECIAL_ALLOWANCE,self.EMPLOYER_CONTRI_PF,self.LTA}'


def table_definition(table_name):
    table_definition.table_define=Table(table_name,metadata,
                                        Column('EMPLOYEE_ID',Integer,primary_key=True),
                                        Column('FIRST_NAME',String),
                                        Column('MIDDLE_NAME',String),
                                        Column('LAST_NAME',String),
                                        Column('GENDER',String),
                                        Column('DATE_OF_BIRTH',String),
                                        Column('DATE_OF_JOINING',String),
                                        Column('WORK_EMAIL',String),
                                        Column('PERSONAL_EMAIL',String),
                                        Column('PERSONAL_ADDRESS',String),
                                        Column('WORK_ADDRESS',String),
                                        Column('EMERGENCY_CONTACT_NAME',String),
                                        Column('EMERGENCY_CONTACT_NUMBER',Integer),
                                        Column('FATHER_NAME',String),
                                        Column('MOTHER_NAME',String),
                                        Column('SPOUSE_NAME',String),
                                        Column('PAN',String),
                                        Column('HAS_PF',BOOL),
                                        Column('PF_NUMBER',String),
                                        Column('UAN',String),
                                        Column('HAS_ESI',BOOL),
                                        Column('ESI_NUMBER',String),
                                        Column('HAS_LWF',BOOL),
                                        Column('LWF_NUMBER',String),
                                        Column('AADHAR_NUMBER',String),
                                        Column('HAS_PT',BOOL),
                                        Column('PT_NUMBER',String),
                                        Column('MOBILE_NUMBER',Integer),
                                        Column('PAYMENT_MODE',String),
                                        Column('BANK_NAME',String),
                                        Column('ACCOUNT_NUMBER',String),
                                        Column('IFSC_CODE',String),
                                        Column('DEPT',String),
                                        Column('DESIG',String),
                                        Column('LATEST_ANNUAL_CTC',Integer),
                                        Column('SALARY_VALID_FROM_DATE',String),
                                        Column('BASIC',Integer),
                                        Column('HRA',Integer),
                                        Column('MEDICAL_ALLOWANCE',Integer),
                                        Column('BONUS',Integer),
                                        Column('COMMISSION',Integer),
                                        Column('SPECIAL_ALLOWANCE',Integer),
                                        Column('EMPLOYER_CONTRI_PF',Integer),
                                        Column('LTA',Integer)
                                        )

    metadata.create_all(engine)

    #Use mapper to define components of class as well as table definition together at once
    mapper(product_table,table_definition.table_define,non_primary=True)



#CREATING A DUMMY BLANK TABLE FOR PRIMARY MAPPER
#This avoids error: Class already has a primary mapper defined
#We made non_primary=True in table_definition function mapper
#This is the work around I could use, maybe there is another way

#Define table structure, here table_name varies
table_define_dummy=Table('dummy_table',metadata,
                         Column('EMPLOYEE_ID',Integer,primary_key=True),
                         Column('FIRST_NAME',String),
                         Column('MIDDLE_NAME',String),
                         Column('LAST_NAME',String),
                         Column('GENDER',String),
                         Column('DATE_OF_BIRTH',String),
                         Column('DATE_OF_JOINING',String),
                         Column('WORK_EMAIL',String),
                         Column('PERSONAL_EMAIL',String),
                         Column('PERSONAL_ADDRESS',String),
                         Column('WORK_ADDRESS',String),
                         Column('EMERGENCY_CONTACT_NAME',String),
                         Column('EMERGENCY_CONTACT_NUMBER',Integer),
                         Column('FATHER_NAME',String),
                         Column('MOTHER_NAME',String),
                         Column('SPOUSE_NAME',String),
                         Column('PAN',String),
                         Column('HAS_PF',BOOL),
                         Column('PF_NUMBER',String),
                         Column('UAN',String),
                         Column('HAS_ESI',BOOL),
                         Column('ESI_NUMBER',String),
                         Column('HAS_LWF',BOOL),
                         Column('LWF_NUMBER',String),
                         Column('AADHAR_NUMBER',String),
                         Column('HAS_PT',BOOL),
                         Column('PT_NUMBER',String),
                         Column('MOBILE_NUMBER',Integer),
                         Column('PAYMENT_MODE',String),
                         Column('BANK_NAME',String),
                         Column('ACCOUNT_NUMBER',String),
                         Column('IFSC_CODE',String),
                         Column('DEPT',String),
                         Column('DESIG',String),
                         Column('LATEST_ANNUAL_CTC',Integer),
                         Column('SALARY_VALID_FROM_DATE',String),
                         Column('BASIC',Integer),
                         Column('HRA',Integer),
                         Column('MEDICAL_ALLOWANCE',Integer),
                         Column('BONUS',Integer),
                         Column('COMMISSION',Integer),
                         Column('SPECIAL_ALLOWANCE',Integer),
                         Column('EMPLOYER_CONTRI_PF',Integer),
                         Column('LTA',Integer)
                         )

#Create table
metadata.create_all(engine)

#Use mapper to define components of class as well as table definition together at once
mapper(product_table,table_define_dummy)

def create_table(upload_dir):

    files=glob.glob(os.path.join(upload_dir,"*.csv"))

    for file_name in files:

        csv_data=pd.read_csv(file_name)

        csv_data=csv_data.values.tolist()

        table_name_from_file=file_name.split('/')[8][:-4]

        table_definition(table_name_from_file)

        #Loop through list of lists, each list in create_bom_table.xls_data is a row
        for row in csv_data:

            ins=table_definition.table_define.insert().values(
                EMPLOYEE_ID=row[0],FIRST_NAME=row[1],MIDDLE_NAME=row[2],LAST_NAME=row[3],GENDER=row[4],
                DATE_OF_BIRTH=row[5],DATE_OF_JOINING=row[6],WORK_EMAIL=row[7],PERSONAL_EMAIL=row[8],
                PERSONAL_ADDRESS=row[9],WORK_ADDRESS=row[10],EMERGENCY_CONTACT_NAME=row[11],EMERGENCY_CONTACT_NUMBER=row[12],
                FATHER_NAME=row[13],MOTHER_NAME=row[14],SPOUSE_NAME=row[15],PAN=row[16],HAS_PF=row[17],PF_NUMBER=row[18],UAN=row[19],
                HAS_ESI=row[20],ESI_NUMBER=row[21],HAS_LWF=row[22],LWF_NUMBER=row[23],AADHAR_NUMBER=row[24],HAS_PT=row[25],
                PT_NUMBER=row[26],MOBILE_NUMBER=row[27],PAYMENT_MODE=row[28],BANK_NAME=row[29],ACCOUNT_NUMBER=row[30],
                IFSC_CODE=row[31],DEPT=row[32],DESIG=row[33],LATEST_ANNUAL_CTC=row[34],SALARY_VALID_FROM_DATE=row[35],
                BASIC=row[36],HRA=row[37],MEDICAL_ALLOWANCE=row[38],BONUS=row[39],COMMISSION=row[40],SPECIAL_ALLOWANCE=row[41],
                EMPLOYER_CONTRI_PF=row[42],LTA=row[43]
            )
            conn=engine.connect()
            conn.execute(ins)

