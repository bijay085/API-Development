# You are making an API for a café with this menu:

menu = [
    {"id": 1, "item": "Coffee", "price": 2.5},
    {"id": 42, "item": "Tea", "price": 1.8},
    {"id": 332, "item": "Sandwich", "price": 4.0},
    {"id": 423, "item": "Cake", "price": 3.2}
]

# ✅ Requirements:

# GET /menu
# → Return the full menu.

# GET /menu/{id}
# → Return one item by its id.
# → If not found, return 404.

# POST /menu
# → Accept a new menu item (JSON body with id, item, price).
# → Add it to the list and return "message": "Item added!".
# → If id already exists, return 400 error "Item already exists".

from fastapi import FastAPI, HTTPException

app = FastAPI()

#Using get to get data from server or list

@app.get("/")
def home():
    return{"message": "Api Homage Bijay Koirala"} or ("Api hompage index page")

@app.get("/menu")
def getmenus():
    return menu

#id not index ok
@app.get("/menu/{id}")
def getmenu(id:int):
    for item in menu:
        if item["id"] == id:
            return item 
    raise HTTPException(status_code=404, detail="Menu item not found")

#now using post to create or insert data to list 
@app.post("/menu/insert")
def adddata(item: dict):
    # check if id already exists
    for m in menu:
        if m["id"] == item["id"]:   # ✅ compare id with id
            raise HTTPException(status_code=400, detail="Item already exists. Try another")

    menu.append(item)
    return {"message": "Item added"}
