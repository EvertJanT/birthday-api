from fastapi import FastAPI, HTTPException
from starlette.responses import Response
from fastapi.openapi.utils import get_openapi

from app.db.models import  NieuwMens
from app.api import api

app = FastAPI()


@app.get("/")
def root():
    return {"message": "De verjaardag API"}

@app.get("/mensen/{geheim}")
def lees_mensen(geheim:int):
    return api.lees_mensen(geheim)

@app.get("/zoekmens")
#http://localhost:8080/zoekmens?voornaam=test&achternaam=test
def zoek_mens(voornaam: str, achternaam:str ):
    return api.zoek_mens(voornaam, achternaam)

@app.post("/voegtoe", status_code=201)
def nieuw_mens(payload: NieuwMens):
    payload = payload.dict()

    return api.nieuw_mens(payload)

@app.get('/gebruikers')
def toon_gebruikers():
    return api.toon_gebruikers()


@app.get('/toonvrienden/{gebruiker_id}')
def toon_vrienden(gebruiker_id: int):
    return api.toon_vrienden(gebruiker_id)


# maak de OpenAPI specificatiebereikbaar via '../doc' of '../redoc'
def custom_openapi():
    openapi_schema = get_openapi(
        title="De verjaardag API",
        version="1.0",
        description="Dit is een eenvoudige API om verjaardagen op te slaan en in te zien",
        routes=app.routes,
    )
    return openapi_schema


app.openapi = custom_openapi

# Run 
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=8080)
