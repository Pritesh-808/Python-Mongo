import pymongo
from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://admin:admin@cluster0.3vv9r1v.mongodb.net/?retryWrites=true&w=majority')
#above is the link copied from mongodb atlas while connecting cluster to app python

db = cluster["cluster"] #cluster is the name of db
collection = db["collexion"] # collexion is name of collection under db named collexion

# student = {"name":"Pritesh","age":22}

# collection.insert_one(student)

#------------------------------------------------------


# teachers = [{"name":"navghane","subject":"communication"}, {"name":"gauri","subject":"DSA"}]

# collection.insert_many(teachers)

#------------------------------------------------------

# teacher1 = {"name":"Pawar sir ","subject":"Network theory"}
# teacher2 = {"name":"Dandwate sir ","subject":"Machine Learning"}

# collection.insert_many([teacher1,teacher2])
#teacher 1 gets inserted first in db and then teacher 2

#--------------------------------------------------------------------
# results = collection.find({"name":"Pawar sir "})

# for result in results:
#     print(result)

#------------------------------------------------------

# results = collection.find({"name":"Pawar sir "})

# for result in results:
#     print(result["_id"])
# prints only ids 

#----------------------------------------------------------------

#update using pymongo
collection.update_many({"name":"Pawar sir "},{"$set":{"Subject":"Updated network theory"}})