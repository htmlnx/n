from pymongo import MongoClient
client=MongoClient('localhost:27017')
db=client.employeedata
def read():
    try:
        employeedata=db.employees.find()
        print("\n All data from employeedata Database \n")
        for emp in employeedata:
            print(emp)
    except Exception:
        print(str(e))
read() 
