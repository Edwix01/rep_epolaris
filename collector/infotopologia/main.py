import os
import obt_infyam
import bridge_id
import map_int
import stp_blk
import stp_info
import obt_root

import uptime
import cpu
import tplink.filtrarinfo
import tplink.obt_tplink
import tplink.sh_tplink
import tplink.tp_linkssh
import tplink.filtrarinfo
import statusdisp
import sendapi


#Lectura de información de los dispositivs

current_dir = os.path.dirname(__file__)
archivoDispositivos = os.path.join(current_dir, '..','inventarios', 'dispositivos.yaml')
datos = obt_infyam.infyam(archivoDispositivos)
direc =  list(datos.keys())


#Inicio de recolección de datos a través de SNMP
print("-------------------- Inicio de Recolección de datos ---------------------")
activos =[]
inaactivos =[]

activos,inactivos = statusdisp.estado_switch(direc)
b_root,froot,fifroot = obt_root.obtr(datos,activos[0])
b_id,f1,fif1= bridge_id.bri_id(activos,datos)     #Bridge ID
st_inf,f2,fif2 = stp_info.stp_inf(activos,datos) 
info_int,f3,fif3 = map_int.ma_int(activos,datos)  #Información de las interfaces {Nombres ejem:G0/0  }
nodb,f4,fif4=stp_blk.stp_status(activos,datos)    #Información de nodos bloqueados ejemplo: {IP-PuertoBloqueado / 10.0.3.1-5}

#Proceso especial para dispositivos TPLINK
iptp,credenciales = tplink.obt_tplink.filtplink(archivoDispositivos)
try:
    tplink.sh_tplink.epmiko(credenciales[iptp[0]]["usuario"],credenciales[iptp[0]]["contrasena"], iptp)
    tp_d = tplink.filtrarinfo.fil_bid("b_id.txt")
    st_inf = tplink.tp_linkssh.tplink_id(b_root,st_inf,tp_d,iptp) #Información de STP {tabla de bridge designados, lista con identificador del puerco y su direccion mac}
except IndexError as error:
    print("No se identificaron dispositivos TPLINK")
except FileNotFoundError as error:
    print("No se genero archivo b.txt")


#Recolección de métricas
diccionario_resultante = cpu.leer_cpu.crear_diccionario_host_marca(archivoDispositivos)
tiempos,ft,fit = uptime.tiempoactivo(activos,datos)
consumoscpu = cpu.mon_cpu(datos,diccionario_resultante)


data = {
    "bridgeid": b_id,
    "activedevices": activos,
    "infointerfaces": info_int,
    "infostp":st_inf,
    "nodesblocks": nodb,
    "bridgeroot":b_root,
    "timeactive":tiempos,
    "consumoscpu":consumoscpu
}


#Sending Information
#sendapi.send_data(data)

#Visualización de la información
print("\n"+"-"*40+"Dispositivos Activos"+"-"*40+"")
print(activos)
print("-"*100+"\n")

print("\n"+"-"*40+"Bridge ID"+"-"*40+"")
print(b_id)
print("-"*100+"\n")

print("\n"+"-"*40+"Información de interfaces"+"-"*40+"")
print(info_int)
print("-"*100+"\n")

print("\n"+"-"*40+"Información de STP"+"-"*40+"")
print(st_inf)
print("-"*100+"\n")


print("\n"+"-"*40+"Información de Nodos bloqueados"+"-"*40+"")
print(nodb)
print("-"*100+"\n")

print("\n"+"-"*40+"Bridge Root"+"-"*40+"")
print(b_root)
print("-"*100+"\n")

print("\n"+"-"*40+"Tiempos de Actividad"+"-"*40+"")
print(tiempos)
print("-"*100+"\n")

print("\n"+"-"*40+"Consumos de CPU"+"-"*40+"")
print(consumoscpu)
print("-"*100+"\n")
