
import requests
import json
# Direccion del servidor HAPI FHIR
url = "https://hapi.fhir.org/baseR4/CareTeam"

# Crear el equipo medico
careteam = {
    "resourceType": "CareTeam",
    "status": "active",
    "name": "Equipo medico de John Doe",
    "subject": {
        "reference": "Patient/831051"
    },
    "participant": [
        {
            "role": [{"text": "Medica responsable"}],
            "member": {
                "display": "Dra. Laura Gomez"
            }
        },
        {
            "role": [{"text": "Enfermero"}],
            "member": {
                "display": "Pablo Ruiz"
            }
        }
    ]
}
# Enviar el equipo al servidor
respuesta = requests.post(
    url,
    json=careteam,
    headers={
        "Content-Type": "application/fhir+json",
        "Accept": "application/fhir+json"
    },
    timeout=30
)
# Comprobar si se creo correctamente
if respuesta.status_code == 201:
    equipo_creado = respuesta.json()
    equipo_id = equipo_creado["id"]

    print("CareTeam creado exitosamente")
    print("ID del equipo:", equipo_id)

    # Recuperar el equipo del servidor
    consulta = requests.get(
        url + "/" + equipo_id,
        headers={"Accept": "application/fhir+json"},
        timeout=30
    )
    consulta.raise_for_status()
    print("CareTeam recuperado del servidor:")
    print(json.dumps(
        consulta.json(),
        indent=2,
        ensure_ascii=False
    ))
else:
    print("Error al crear CareTeam:", respuesta.status_code)
    print(respuesta.text)
