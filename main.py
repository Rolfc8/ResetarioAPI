from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def index():
    return"hola a todos, ¿quieres saber sobre recetas para cocinar?"
@app.get("/recetas/(num)")
def recetas(num):
    recetas={
        "1":"receta para pan de muerto",
        "2":"receta para pan de elote",
        "3":"receta para pan de zanahoria",
        "4":"receta para empanadas"
           }
    return (recetas[num])
    print("coloca numeros del 1 al 5 con comillas");
