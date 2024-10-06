from pymongo import MongoClient

# Conectar al servidor de MongoDB (puedes ajustar la URI según tu configuración)
client = MongoClient('mongodb://localhost:27017/')

# Seleccionar la base de datos
db = client['Escuela']

# Seleccionar la colección
collection = db['alumnos']

# Leer todos los documentos de la colección
documentos = collection.find()

# Mostrar los documentos encontrados
for documento in documentos:
    print(documento)
