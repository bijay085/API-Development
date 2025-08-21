from fastapi import FastAPI

# create the app
app = FastAPI()

# simple route
@app.get("/") #if we didnt provide routing then it will say details not found so routing necessary
def home():
    return {"message": "API is working!"}
