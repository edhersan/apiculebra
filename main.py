from fastapi import FastAPI
app= FastAPI()

app.title = "prueba api"
app.version = "5.0"

@app.get("/")
def aplica():

    return "KIUBO MANO"