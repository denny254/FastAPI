from fastapi import FastAPI 

app = FastAPI()

@app.get('/')
    
def index():
    
    return {'data':{'name':'Kin'}}

@app.get("/about")

def about():
    return{"name":"About page"}