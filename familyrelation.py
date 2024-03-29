from fichier import Fichier
from relationship import Relationship
dbRelationship=Relationship()
x=Fichier("./","hey.html").lire()
z=x.split("relationship_id\" class=\"form-control\">")[1].split("</select>")[0]
values=[]
myvalue={}
myval=""
mykey=""
for y in z.split("value=\""):
    try:
        mykey=y.split("\"")[0].split("\"")[0]
        myvalue=y.split(">")[1].split("<")[0]
        dbRelationship.create({"name":myvalue})
        values.append({"key":mykey,"value":myvalue})
    except:
        print("hey")
print(values)
