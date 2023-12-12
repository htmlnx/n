from pymongo import MongoClient
client=MongoClient('localhost:27017')
db=client.employeedata
def update():
    try:
        name=input("\n Enter name to update\n ")
        age=input("\n Enter age to update\n ")
        country=input("\n Enter country to update \n")
        db.employees.update_one(
            {"ename":name},
            {"$set":{
            "eage":age,
            "ecountry":country
        }
        }
        )
        print("\n Records updated successfully\n")
    except Exception:
        print(str(e))
update()
