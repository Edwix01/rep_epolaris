import os
import obt_infyam
import bridge_id
import map_int
import stp_blk
import stp_info

import tplink.filtrarinfo
import tplink.obt_tplink
import tplink.sh_tplink
import tplink.tp_linkssh
import tplink.filtrarinfo


#Lectura de información de los dispositivos
current_dir = os.path.dirname(__file__)
archivoDispositivos = os.path.join(current_dir, '..','inventarios', 'dispositivos2.yaml')
datos = obt_infyam.infyam(archivoDispositivos)
direc =  ["10.0.1.13","10.0.1.14"]


#Identificar dispositivos TPLINK
iptp,credenciales = tplink.obt_tplink.filtplink(archivoDispositivos)
#Proceso extra para conmutadores TPLINK
tplink.sh_tplink.epmiko(credenciales[iptp[0]]["usuario"],credenciales[iptp[0]]["contrasena"], iptp)
tp_d = tplink.filtrarinfo.fil_bid("b_id.txt")
print(tp_d)



#Inicio de recolección de datos a través de SNMP
print("-------------------- Inicio de Recolección de datos ---------------------")
b_id,f1,fif1= bridge_id.bri_id(direc,datos)     #Bridge I
st_inf,f2,fif2 = stp_info.stp_inf(direc,datos)  #Información de STP {tabla de bridge designados, lista con identificador del puerco y su direccion mac}
print(st_inf)
"""
info_int,f3,fif3 = map_int.ma_int(direc,datos)  #Información de las interfaces {Nombres ejem:G0/0  }
nodb,f4,fif4=stp_blk.stp_status(direc,datos)    #Información de nodos bloqueados ejemplo: {IP-PuertoBloqueado / 10.0.3.1-5}

"""
#Utilizar para visualizar alguna variable
"""
print("\n"+"-"*40+"Bridge ID"+"-"*40+"")
print(b_id)
print("-"*100+"\n")
"""
