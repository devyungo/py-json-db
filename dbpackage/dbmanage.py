import json as j

def dbread(dbpath):
    with open(dbpath, "r") as db:
        return j.load(db)
    
def dbwrite(data,dbpath):
    with open(dbpath, "w") as db:
        j.dump(data, db)