from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def index():
    return"hola a todos, ¿quieres saber sobre recetas para cocinar?"

@app.get("/Pokemon/{num}")
def pokemon(num):
    pokemons={
        "1":"Bulbasaur",
        "2":"Ivysaur",
        "3":"Venasaur",
        "4":"Charmander",
        
         }
        
    return pokemons[num]

@app.get("/Conversor_Caf/{C}")
def conversorCaf(C):
    try:
           C=float(C)
           TF=C*(9/5)+32
           return f"la temperatura es de {TF} grados farenheit"
    except:
           return "entrada invalida"
        
               
            
            
            
@app.get("/recetas/{num}")
def recet(num):
     receta={
         "1":"Caldo_de_Pollo"
         "300 gramos de pechuga de pollo sin piel"
         "2 ½ litros de agua"
         "50 gramos (o ¼) de cebolla en trozo"
         "2 dientes de ajo"
         "2 cubitos de Cubo(s) de Knorr® Caldo de Pollo"
         "1 zanahoria pelada rebanada y cocida"
         "1 calabaza rebanada"
         "1 taza de ejotes verdes cocidos y cortados en tercios"
         "1 elote blanco cocido y en trozos"
         "4 ramitas de cilantro fresco",
         "2":"Pozole",
         "3":"Mole_de_res",
         "4":"Mole_de_panza",
         "5":"Mole_Polano",
            
                        }
     return receta[num] 
