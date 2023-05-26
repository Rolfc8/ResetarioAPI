from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def index():
    return"hola a todos, ¿quieres saber sobre recetas para cocinar?"
@app.get("/recetas/(num)")
def recetas(num):
    
   return ([num])
