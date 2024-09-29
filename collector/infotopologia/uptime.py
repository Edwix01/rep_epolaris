from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

def tiempoactivo(ips,datos):
    a = {}
    f = 0
    fif = {}
    for server_ip in ips:
        comunidad = datos[server_ip]["snmp"]
        errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
            cmdgen.CommunityData(comunidad),
            cmdgen.UdpTransportTarget((server_ip, 161)),
            0,25,
            #Despliegue
            '1.3.6.1.2.1.1.3'

        )
        if errorIndication != None:
            f = 1
            fif[server_ip] = ""

        #Código para despliegue
        for varBindTableRow in varBindTable:
            for name, val in varBindTableRow:
                    a[server_ip] = int(val)/(100*60*60*24*7)
        
    return a,f,fif
