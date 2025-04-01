from fastapi import FastAPI, HTTPException
import json
import os

app = FastAPI()

FILE_NAME = "alumnes.json"

def carregar_dades():
    """Carrega les dades des del fitxer JSON."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

def desar_dades(alumnes):
    """Desa les dades al fitxer JSON."""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(alumnes, file, indent=4, ensure_ascii=False)

@app.get("/")
def llegenda():
    return "Institut TIC de Barcelona"

@app.get("/alumnes/")
def nombre_alumnes():
    alumnes = carregar_dades()
    return {"total_alumnes": len(alumnes)}

@app.get("/id/{numero}")
def obtenir_alumne(numero: int):
    alumnes = carregar_dades()
    for alumne in alumnes:
        if alumne["id"] == numero:
            return alumne
    raise HTTPException(status_code=404, detail="Alumne no trobat")

@app.delete("/del/{numero}")
def esborrar_alumne(numero: int):
    alumnes = carregar_dades()
    alumnes_actualitzats = [alumne for alumne in alumnes if alumne["id"] != numero]
    if len(alumnes) == len(alumnes_actualitzats):
        raise HTTPException(status_code=404, detail="Alumne no trobat")
    desar_dades(alumnes_actualitzats)
    return {"message": "Alumne esborrat correctament"}

@app.post("/alumne/")
def afegir_alumne(alumne: dict):
    alumnes = carregar_dades()
    nou_id = max([a["id"] for a in alumnes], default=0) + 1
    alumne["id"] = nou_id
    alumnes.append(alumne)
    desar_dades(alumnes)
    return {"message": "Alumne afegit correctament", "id": nou_id}
