from pysnmp.entity.rfc3413.oneliner import cmdgen
import re
cmdGen = cmdgen.CommandGenerator()

def ma_int(direc,datos):
    """
    Funcion para obtener los nombres de las interfaces de un Switch

    Parameters:
    direc(list):    Lista con direcciones IP 
    datos(dict):    Informacion de los dispositivos

    Return:
    info_interfaces(dict): Diccionario con las interfaces de cada uno de los swithches
    """
    
    info_interfaces = {}
    f=0
    fif=[]
    for server_ip in direc:
        comunidad = datos[server_ip]["snmp"]
        errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
            cmdgen.CommunityData(comunidad),
            cmdgen.UdpTransportTarget((server_ip, 161)),
            0,25,
            '1.3.6.1.2.1.2.2.1.2'
        )
        c=1
        d1 = {}
        if errorIndication != None:
            f = 1
            fif.append(server_ip)

        for varBindTableRow in varBindTable:
            for name, val in varBindTableRow:
                if "Ethernet" in val.prettyPrint() :
                    # Utilizar una expresión regular para extraer la primera letra y los números
                    cadena = val.prettyPrint()
                    # Utilizar una expresión regular para encontrar solo los números y barras
                    numeros = re.sub(r'[^\d/]', '', cadena)
                    if datos[server_ip]["marca"] == "TPLINK-JetStream":
                        d1[str(name).split(".")[-1]] = cadena[0] + numeros
                    else:
                        d1[str(c)] = cadena[0] + numeros
                    c+=1
        info_interfaces[str(server_ip)] = d1
    return info_interfaces,f,fif

def ma_in_complete(direc,datos):
    """
    Funcion para obtener los nombres de las interfaces de un Switch

    Parameters:
    direc(list):    Lista con direcciones IP 
    datos(dict):    Informacion de los dispositivos

    Return:
    info_interfaces(dict): Diccionario con las interfaces de cada uno de los swithches
    """
    
    info_interfaces = {}
    f=0
    fif=[]
    for server_ip in direc:
        comunidad = datos[server_ip]["snmp"]
        errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
            cmdgen.CommunityData(comunidad),
            cmdgen.UdpTransportTarget((server_ip, 161)),
            0,25,
            '1.3.6.1.2.1.2.2.1.2'
        )
        c=1
        d1 = {}
        if errorIndication != None:
            f = 1
            fif.append(server_ip)

        for varBindTableRow in varBindTable:
            for name, val in varBindTableRow:
                if "Ethernet" in val.prettyPrint() and  not("0/0" in val.prettyPrint() ) :
                    # Utilizar una expresión regular para extraer la primera letra y los números
                    cadena = val.prettyPrint()
                    # Utilizar una expresión regular para encontrar solo los números y barras
                    numeros = re.sub(r'[^\d/]', '', cadena)
                    if datos[server_ip]["marca"] == "TPLINK-JetStream":
                        d1[str(name).split(".")[-1]] = cadena
                    else:
                        d1[str(c)] = cadena
                    c+=1
        info_interfaces[str(server_ip)] = d1
    return info_interfaces,f,fif
