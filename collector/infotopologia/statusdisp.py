import time
from ping3 import ping

def estado_switch(ips, intentos=3, timeout=4):
    """
    Verifica si un switch está activo mediante múltiples pings.

    Parámetros:
    ips (list): list of ip address
    intentos (int): Número de intentos de ping.
    timeout (int): Tiempo en segundos para esperar entre intentos.

    Retorna:
    estado (dict): IP Address how main key and sta:true/flase and bi:1/0 (bi -> bandera de incidentes en el dispositivo) 
    """
    activos = []
    inactivos =[]
    states = {}


    for ip_switch in ips:
        exitosos = 0

        for i in range(intentos):
            respuesta = ping(ip_switch, timeout=timeout)  # Realiza un ping
            if respuesta is not None:
                print(f"Ping {i + 1}: El switch {ip_switch} está activo. Tiempo de respuesta: {respuesta:.2f} ms")
                exitosos += 1
            else:
                print(f"Ping {i + 1}: El switch {ip_switch} no respondió.")
            
            time.sleep(1)  # Esperar 1 segundo entre pings

        # Calcular el porcentaje de pings exitosos
        porcentaje_exitosos = (exitosos / intentos) * 100
        print(f"Porcentaje de pings exitosos: {porcentaje_exitosos:.2f}%")

        # Definir un umbral para decidir si el switch está fuera de servicio
        umbral = 50  # 50% de pings exitosos
        if porcentaje_exitosos == 0:
            print("El switch está  fuera de servicio.")
            inactivos.append(ip_switch)
            bi = 1    
        elif porcentaje_exitosos < umbral and porcentaje_exitosos>0:
            print("El switch está teniendo intermitencias en su conectividad.")
            bi = 1
            inactivos.append(ip_switch)
        else:
            print("El switch está activo.")
            bi = 0
            activos.append(ip_switch)
        
        states[ip_switch] = bi
    return activos,inactivos,states
