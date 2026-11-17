
import requests

# Función que busca pacientes por su DNI
def buscar_paciente_por_dni(dni):

    url = "https://hapi.fhir.org/baseR4/Patient"

    # Indicamos el sistema y el DNI que buscamos
    parametros = {
        "identifier": f"https://www.argentina.gob.ar/dni|{dni}"
    }

    # Realizamos la petición al servidor
    respuesta = requests.get(url, params=parametros, timeout=30)
    respuesta.raise_for_status()

    datos = respuesta.json()

    # Obtenemos los pacientes encontrados
    pacientes = datos.get("entry", [])

    return pacientes


# Probamos la función con el paciente creado
dni = "99472861"

resultados = buscar_paciente_por_dni(dni)

if resultados:
    for resultado in resultados:
        paciente = resultado["resource"]

        print("¡Paciente encontrado!")
        print("ID:", paciente["id"])
        print("DNI:", dni)
        print("Nombre:", paciente["name"][0]["given"][0])
        print("Apellido:", paciente["name"][0]["family"])
else:
    print("No se encontró ningún paciente con ese DNI.")
