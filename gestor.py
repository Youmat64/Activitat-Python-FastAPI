import json
import os

# Nom del fitxer JSON
def FILE_NAME(): return "alumnes.json"

# Estructura per emmagatzemar alumnes
alumnes = []
next_id = 1

def carregar_dades():
    """Carrega les dades des del fitxer JSON."""
    global alumnes, next_id
    if os.path.exists(FILE_NAME()):
        with open(FILE_NAME(), "r", encoding="utf-8") as file:
            alumnes = json.load(file)
            if alumnes:
                next_id = max(alumne["id"] for alumne in alumnes) + 1

def desar_dades():
    """Desa les dades al fitxer JSON."""
    with open(FILE_NAME(), "w", encoding="utf-8") as file:
        json.dump(alumnes, file, indent=4, ensure_ascii=False)

def mostrar_llistat():
    """Mostra la llista d'alumnes."""
    for alumne in alumnes:
        print(f"ID: {alumne['id']} | Nom: {alumne['nom']} {alumne['cognom']}")

def afegir_alumne():
    """Afegeix un nou alumne."""
    global next_id
    nom = input("Nom: ")
    cognom = input("Cognom: ")
    dia = int(input("Dia de naixement: "))
    mes = int(input("Mes de naixement: "))
    any = int(input("Any de naixement: "))
    email = input("Email: ")
    feina = input("Treballa? (si/no): ").strip().lower() == "si"
    curs = input("Curs: ")

    alumne = {
        "id": next_id,
        "nom": nom,
        "cognom": cognom,
        "data": {"dia": dia, "mes": mes, "any": any},
        "email": email,
        "feina": feina,
        "curs": curs
    }
    alumnes.append(alumne)
    next_id += 1
    desar_dades()
    print("Alumne afegit correctament!")

def veure_alumne():
    """Mostra les dades d'un alumne pel seu ID."""
    id_cercat = int(input("Introdueix l'ID de l'alumne: "))
    for alumne in alumnes:
        if alumne["id"] == id_cercat:
            print(json.dumps(alumne, indent=4, ensure_ascii=False))
            return
    print("No s'ha trobat cap alumne amb aquest ID.")

def esborrar_alumne():
    """Esborra un alumne pel seu ID."""
    id_esborrar = int(input("Introdueix l'ID de l'alumne a esborrar: "))
    global alumnes
    alumnes = [alumne for alumne in alumnes if alumne["id"] != id_esborrar]
    desar_dades()
    print("Alumne esborrat correctament.")

def menu():
    """Mostra el menú d'opcions."""
    carregar_dades()
    while True:
        print("\nMenú:")
        print("1. Mostrar llistat d'alumnes")
        print("2. Afegir un alumne")
        print("3. Veure un alumne")
        print("4. Esborrar un alumne")
        print("5. Sortir")
        opcio = input("Escull una opció: ")
        if opcio == "1":
            mostrar_llistat()
        elif opcio == "2":
            afegir_alumne()
        elif opcio == "3":
            veure_alumne()
        elif opcio == "4":
            esborrar_alumne()
        elif opcio == "5":
            break
        else:
            print("Opció no vàlida. Torna-ho a intentar.")

if __name__ == "__main__":
    menu()
