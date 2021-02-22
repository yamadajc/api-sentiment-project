from helpers.mongoConnection import *
from helpers.checking import *
from bson import ObjectId
from helpers.settings import *

def setup(typ):
    if typ == "masterchef":
        return masterchef_set
    elif typ == "character":
        return character_set
    elif typ == "twitter":
        return twitter_set

def insert(obj,typ):
    settings = setup(typ)

    if not check_params(obj,settings['obligatory']):
        return {"response":400, "message": f"Bad Request: {settings['obligatory']} are obligatory parameters"}

    q = {settings['core']:obj[settings['core']]}

    if check_exists(q,typ):
        return {"response":400,"message": f"Bad Request: there is already a {settings['sing']} with that name"}

    res = write_coll(typ,obj)
    return {"response":200,"message": f"{settings['sing']}  successfully added"}
    

def list_all(typ):
    settings = setup(typ)

    res = read_coll(typ,{})
    response = {c[settings['core']]:str(c['_id']) for c in res}
    
    return response 

def get(obj,typ):
    settings = setup(typ)

    if not check_params(obj,['id']):
        return {"response":400,"message":"Bad Request: 'id' is an obligatory parameter"}

    q = {"_id":ObjectId(obj['id'])}

    if not check_exists(q,typ):
        return {"response":400,"message": f"Bad Request: {settings['sing']} with given id does not exist"}
    
    return read_coll(typ,q)

def delete(obj,typ):
    settings = setup(typ)

    if not check_params(obj,['id']):
        return {"response":400,"message":"Bad Request: 'id' is an obligatory parameter"}

    q = {"_id":ObjectId(obj['id'])}
    if not check_exists(q,typ):
        return {"response":400,"message": f"Bad Request: {settings['sing']} with given id does not exist"}

    delete_coll(typ,q)
    return {"response":200,"message": f"{settings['sing']}  successfully deleted"}

def update(obj,typ):
    settings = setup(typ)

    if not check_params(obj,['id'],settings['at_least_one']):
        return {"response":400,"message": f"Bad Request: 'id' and at least one of {settings['at_least_one']} are obligatory parameters"}
    
    q = {"_id":ObjectId(obj['id'])}
    if not check_exists(q,typ):
        return {"response":400,"message": f"Bad Request: {settings['sing']} with given id does not exist"}
    
    obj.pop("id")
    update_coll(typ,q,obj)
    return {"response":200, "message": f"{settings['sing']} successfully updated"}

