from pydantic import BaseModel
from typing import List



class NieuwMens(BaseModel):
    id: int
    voornaam : str
    achternaam : str
    geboortedatum : str

class GebruikerVrienden(BaseModel):
    gebruiker_id: int
    vrienden: List[NieuwMens]

 