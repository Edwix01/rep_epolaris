import os
import obt_infyam
import bridge_id
import map_int
import stp_blk
import stp_info

#Definición de una lista de direcciónes Ip de prueba.
direc = ["10.0.2.1","10.0.2.2","10.0.2.3","10.0.2.4","10.0.2.5"]


print("-------------------- EMPIEZA EL DESCUBRIMIENTO DE LA TOPOLOGIA ---------------------")
print("-------------- EJECUTANDO FASE 1 (RECOLECCION DE DATOS DEL YAML) -------------------")
#Fase 1
#Lectura de Archivo Yaml - Configuraciones
current_dir = os.path.dirname(__file__)
archivoDispositivos = os.path.join(current_dir, 'inventarios', 'dispositivos.yaml')
datos = obt_infyam.infyam(archivoDispositivos)
print(datos)


print("------------------- EJECUTANDO FASE 2 (INFORMACION DE STP) --------------------------")
#Fase 2

#Informacion STP
# Bridge ID, Designed Bridge   
b_id,f1,fif1= bridge_id.bri_id(direc,datos)     #Bridge ID
print("\n"+"-"*40+"Bridge ID"+"-"*40+"")
print(b_id)
print("-"*100+"\n")
st_inf,f2,fif2 = stp_info.stp_inf(direc,datos)  #Información de STP {tabla de bridge designados, lista con identificador del puerco y su direccion mac}
print("\n"+"-"*40+"Info STP"+"-"*40+"")
print(st_inf)
print("-"*100+"\n")
info_int,f3,fif3 = map_int.ma_int(direc,datos)  #Información de las interfaces {Nombres ejem:G0/0  }
print("\n"+"-"*40+"Info interfaces"+"-"*40+"")
print(info_int)
print("-"*100+"\n")
nodb,f4,fif4=stp_blk.stp_status(direc,datos)
print("\n"+"-"*40+"nobd"+"-"*40+"")
print(nodb)
print("-"*100+"\n")
