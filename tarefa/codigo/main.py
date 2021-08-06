import pickle
from fastapi import FastAPI

app = FastAPI()
@app.post('/model')
## Coloque seu codigo na função abaixo
def titanic(Sex:int, Age:float, Lifeboat: int,Pclass:int):
    with open('model/Titanic.pkl', 'rb') as fid: 
        titanic = pickle.load(fid)

    resp = titanic.predict([[Sex, Age, Lifeboat, Pclass]])    

    if( resp):
        return  {"survived": True,	"status": 200,	"message": "The passanger has lived." }
    else: 
        return {"survived": False,	"status": 200,	"message": "The passanger has died." }
    
        

       
        

@app.get('/model')
def get():
    return {'hello':'test'}
