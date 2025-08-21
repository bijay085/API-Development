from fastapi import FastAPI, HTTPException

# create the app
app = FastAPI()

# simple route
@app.get("/") #if we didnt provide routing then it will say details not found so routing necessary
def home():
    return {"message": "API HOME is working!"}

books = ["The Great Gatsby", "To Kill a Mockingbird", "Pride and Prejudice", "Moby Dick", "War and Peace", "The Catcher in the Rye", "Brave New World", "Fahrenheit 451", "The Picture of Dorian Gray"]

@app.get("/books")
def getbooks():
    return books

@app.get("/books/{number}")
# def getbook(number) -> it will give internal error cuz it will take as default string
def getbook(number:int):
    return books[number]

students = [
    {"id":10, "name":"Bijay"},
    {"id":13, "name":"Kaushal"},
    {"id":71, "name":"Game"}
]

@app.get("/students/{index}")
def getstudents(index:int):
    return students[index]

@app.get("/students")
def getstudents():
    return students

#now from student id not from index
@app.get("/students/id/{id}")
def getstudentid(id:int):
    for st in students:
        if st["id"] == id:
            return st
    raise HTTPException(status_code=404, detail="Student not found")