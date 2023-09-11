from dbpackage import dbmanage as dbm

dbpath = "db.json"

array= dbm.dbread(dbpath)

def createstr():
    global array
    str = ""
    for i in range(len(array)):
        notasum = 0
        for n in range(len(array[i]["notas"])):
            notasum+=array[i]["notas"][n]/len(array[i]["notas"])
        str+=f"{array[i]['nome']} - {notasum}\n"
    return str

print(createstr())
