import requests

def send_data(data):
    """
    This function allows to send information to the server through the API
    
    Parameters:
    data (dict):    Dictionary with information from the collector
    
    Returns:
    none:   The information is sent
    """       
    # Cabeceras HTTP que incluyen el token de autenticación
    headers = {
        'Authorization': 'Bearer tu_token_aqui',
        'Content-Type': 'application/json'
    }

    # URL de la API
    url = 'https://api.ejemplo.com/users'

    # Realizar la solicitud POST
    response = requests.post(url, json=data, headers=headers)

    # Verificar el estado de la solicitud
    if response.status_code == 201:
        print("Usuario creado correctamente:", response.json())
    else:
        print(f"Error: {response.status_code}, {response.text}")
