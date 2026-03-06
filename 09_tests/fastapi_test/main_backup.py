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

class Item(BaseModel):
    id: int
    name: str = Field(..., min_length=2)
    price: float = Field(..., gt=0)
    description: Optional[str] = None

class User(BaseModel):
    username: str
    age: int = Field(..., ge=0)

# ---------------------------------------------------------
# Fake-Datenbank
# ---------------------------------------------------------

items_db = [
    Item(id=1, name="Apfel", price=1.2),
    Item(id=2, name="Banane", price=0.8),
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
def index():
    return {"message": "Willkommen zu deiner großen Übungssammlung!"}

@api.get("/items", response_model=List[Item])
def get_items():
    return items_db

@api.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item nicht gefunden")

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
# Body-Parameter
# ---------------------------------------------------------

@api.post("/users", response_model=User)
def create_user(user: User):
    return user

# ---------------------------------------------------------
# Background Task
# ---------------------------------------------------------

def write_log(text: str):
    with open("log.txt", "a") as f:
        f.write(text + "\n")

@api.post("/log")
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
