import pymongo
import pymongo.errors

MONGO_HOST = "root:example@localhost"
MONGO_PUERTO = "27017"
MONGO_TF = 1000
MONGO_URL = "mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"


#Conexión con la base de datos
try:
    cliente = pymongo.MongoClient(MONGO_URL,serverSelectionTimeoutMS=MONGO_TF)
    cliente.server_info()
    basedatos = cliente["escuela"]
    colection = basedatos["alumnos"]
    print("Conexión a MONGO existosa")
    
except pymongo.errors.ServerSelectionTimeoutError as errortiempo:
    print("Tiempo excedido: " + str(errortiempo))
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Error de conexión: " + str(errorConexion))




def read_mongo(pa):
    """

    This function available read information from MongoDB.

    Parameters:
    db  (str): Database name
    col (str): Collection name
    pa  (str): Parameter name

    Returns:
    inf_mgdb (dict):  information about query
    """
    for documento in colection.find():
        print(documento[pa])



def create_mongo(documento):
    """

    This function available read information from MongoDB.

    Parameters:
    db  (str): Database name
    col (str): Collection name
    pa  (str): Parameter name

    Returns:
    inf_mgdb (dict):  information about query
    """
    try:
        colection.insert_one(documento)
    except pymongo.errors.ConnectionFailure as error:
        print(error)

    
def update_mongo(dato,ninfo):
    """
    Doc string
    """
    
    try:
        resultado = colection.update_one(dato, ninfo)
    except pymongo.errors.ConnectionFailure as error:
        print("La conexión fallo")
        print(error)


nd = {"Nombre":"Naty","Calificaciones":10}
p = "Nombre"
dato = {'Nombre': 'Naty'}  # Cambia esto al criterio de búsqueda que necesites
ninfo = {'$set': {'Calificaciones': 30}}  # Cambia 'edad' y '30' por el campo y el nuevo valor
read_mongo(p)
update_mongo(dato,ninfo)

