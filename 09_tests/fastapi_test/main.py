from fastapi import FastAPI, HTTPException, BackgroundTasks, Depends
from pydantic import BaseModel, Field
from typing import Optional, List

api = FastAPI(
    title="FastAPI Übungssammlung",
    description="Alle Übungen aus deinem Textfile in einer einzigen Datei.",
    version="1.0"
    )

# ---------------------------------------------------------
# Datenmodelle
# ---------------------------------------------------------


from pydantic import BaseModel
from typing import Optional
class Item(BaseModel):
    itemid: int
    description: str
    owner: Optional[str] = None


class User(BaseModel):
    username: str
    age: int = Field(..., ge=0)

# ---------------------------------------------------------
# Fake-Datenbank
# ---------------------------------------------------------

items_db = [
    Item(itemid=1, name="Apfel", description="Frisches Obst", price=1.2),
    Item(itemid=2, name="Banane", description="Frisches Obst", price=0.8),
]


users_db = [
    {
        'user_id': 1,
        'name': 'Alice',
        'subscription': 'free tier'
    },
    {
        'user_id': 2,
        'name': 'Bob',
        'subscription': 'premium tier'
    },
    {
        'user_id': 3,
        'name': 'Clementine',
        'subscription': 'free tier'
    }
]



# ---------------------------------------------------------
# Dependencies
# ---------------------------------------------------------

def verify_token(token: str):
    if token != "secret123":
        raise HTTPException(status_code=401, detail="Ungültiger Token")
    return token

# ---------------------------------------------------------
# Basic Routes
# ---------------------------------------------------------

@api.get("/")
def get_index(argument1):
    return {
        'data': argument1
    }

# new
from typing import Optional
@api.get('/addition')
def get_addition(a: int, b: Optional[int]=None):
    if b:
        result = a + b
    else:
        result = a + 1
    return {
        'addition_result': result
    }


@api.post("/item")
def post_item(item : Item):
	return {"item_id" : item.itemid}



# ends


@api.get("/items", response_model=List[Item])
def get_items():
    return items_db

@api.get('/item/{item_id:int}')
def get_item(item_id):
	return {'route' : 'dynamic',
		'itemid' : item_id,
		'source' : "int"}


@api.get('/item/{itemid:float}')
def get_item_float(itemid):
    return {
        'route': 'dynamic',
        'itemid': itemid,
        'source': 'float'
    }
@api.get('/item/{itemid}')
def get_item_default(itemid):
    return {
        'route': 'dynamic',
        'itemid': itemid,
        'source': 'string'
    }
@api.get("/users")
def get_users():
	return users_db


# new

@api.get("/users/{user_id:int}")
def get_user(user_id):
	try:
	   user = list(filter(lambda x : x.get("user_id") == user_id, users_db))[0]
	   return user
	except IndexError:
	   return {}




@api.get("/users/{user_id:int}/name")
def get_user(user_id):
        try:
           user = list(filter(lambda x : x.get("user_id") == user_id, users_db))[0]
           return user['name']
        except IndexError:
           return {}


@api.get("/users/{user_id:int}/subscription")
def get_user_subscription(user_id):
	try:
	   user = list(filter(lambda x : x.get('user_id')==user_id, users_db))[0]
	   return {"subsciption" : user["subscription"]}
	except IndexError:
           return {}

# end

@api.post("/items", response_model=Item)
def create_item(item: Item):
    items_db.append(item)
    return item

# ---------------------------------------------------------
# Query-Parameter
# ---------------------------------------------------------

@api.get("/search")
def search_items(q: Optional[str] = None):
    if not q:
        return items_db
    return [item for item in items_db if q.lower() in item.name.lower()]



# ---------------------------------------------------------
# Background Task
# ---------------------------------------------------------

def write_log(text: str):
    with open("log.txt", "a") as f:
        f.write(text + "\n")

@api.api_route("/log", methods=["GET", "POST"])
def log_action(action: str, background: BackgroundTasks):
    background.add_task(write_log, action)
    return {"status": "Aktion wird im Hintergrund geloggt"}

# ---------------------------------------------------------
# Fehlerbehandlung
# ---------------------------------------------------------

@api.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Division durch 0 nicht erlaubt")
    return {"result": a / b}

# ---------------------------------------------------------
# Dependency-geschützte Route
# ---------------------------------------------------------

@api.get("/protected")
def protected(token: str = Depends(verify_token)):
    return {"message": "Zugriff erlaubt"}

# ---------------------------------------------------------
# Event Handler
# ---------------------------------------------------------

@api.on_event("startup")
def on_startup():
    print("Server startet...")

@api.on_event("shutdown")
def on_shutdown():
    print("Server wird beendet...")
