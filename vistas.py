from Persistencia import MiZODB,transaction
import Controladores
import modelos
from abc import ABCMeta, abstractmethod
import os
import subprocess
import sys
import datetime
def limpiar():
   subprocess.call("clear")
 
    
"""
def buscar_vehiculo(seccion, vehiculo): 
    for i in  seccion.len

        if seccion.index(vehiculo)!=None
            ocupa_lugar=i
        else
            ocupa_lugar= 0
   
    return oscupa_lugar

def obtener_disponibilidad(seccion):

    for i in seccion.len:
        if seccion[i]==None
            espacio_disponible=i
        elif seccion[i]!=None and i=seccion.len
            espacio_disponible=0
       
        return espacio_disponible
       
def  asignar_estacionamiento(vehiculo, espacio):
        seccion.insert(espacio, vehiculo)
        hora_entrada=datetime.datetime.now()


def   dar_salida(vehiculo,espacio):
        seccion.remove(vehiculo)
        hora_salida=datetime.datetime.now()

def obtener_total_horas(vehiculo):
        total_horas= vehiculo.hora_salida-vehiculo.hora_entrada
        return total_horas

def obtener_costo(vehiculo, horas):
        costo=vehiculo.tarifa * total_horas
        return costo
       
def imprimir_ticket(vehiculo)
     print( )

"""
     
   
def menu():
    os.system('clear')
    """funcion que limpiara la pantalla cada vez que deba mostrar nuevamente el menu"""
    print("-1) Consultar disponbilidad    ")
    print("-2) Asignar Estacionamiento    ")
    print("-3) Consultar tiempo de estadia")
    print("-4) Dar salida  vehiculo por posicion")
    print("-5) Dar salida  vehiculo por chapa")
    print("-5) Generar ticket    ")
    print("-6) Registrar nuevo vehiculo")
    print("-7) Cargar Seccion")
    print("-8) Listar Secciones")
    print("-9) Salir")
    tarea = input('Ingrese número de tarea: ')
    if(tarea=='1'):
        consultar_disponibilidad()
    elif(tarea=='2'):
    	asignar_estacionamiento()
    elif(tarea=='3'):
        limpiar()
        cargar_reserva(codigo)
    elif(tarea=='4'):
        liberar_estacionamiento_por_posicion()
    elif(tarea=='5'):
        liberar_estacionamiento_por_chapa()
    elif(tarea=='6'):
        cargar_seccion()
        login()
    elif(tarea=='7'):
        cargar_seccion()
    elif(tarea=='8'):
    	listar_secciones()
    elif(tarea=='9'):
        sys.exit()
    else:
        print('Tarea no es valida')

def cargar_cliente():
    cli=ControladorCliente()
    cli.cargar_cliente(cl1)
    
def listar_cliente():
    ctrl_cli=ControladorCliente()
    cli=ctrl_cli.listar_clientes(cc)
	
def eliminar_cliente():
    eliminar_cliente(cc)
    cli=ControladorCliente()
	
def cargar_operador():
    ope=ControladorOperador()
    ope.cargar_operador(op1)
def listar_operador():
    ctrl_ope=ControladorOperador()
    ope=ctrl_ope.listar_operadores(usu)
	
def eliminar_operador():
    eliminar_operador(usu)
    ope=ControladorOperador()


def cargar_automovil():
    auto=ControladorAutomovil()
    auto.cargar_automovil(auto1)
def listar_automoviles():
    ctrl_auto=ControladorAutomovil()
    auto=ctrl_auto.listar_automoviles(au)
	
def eliminar_automovil():
    eliminar_automovil(au)
    auto=ControladorAutomovil()

def cargar_motocicleta():
    moto=ControladorMotocicleta()
    moto.cargar_motocicleta(moto1)
def listar_motocicleta():
    ctrl_moto=ControladorMotocicleta()
    moto=ctrl_moto.listar_motocicleta(mot)
	
def eliminar_motocicleta():
    eliminar_motocicleta(mot)
    moto=ControladorMotocicleta()
def consultar_disponibilidad():
	print("Ingrese tipo de Seccion: ") 
	tipo = input('Normal, Motocicleta o Discapacitado: ')
	db = MiZODB()
	dbroot = db.raiz
	respuesta= False  
	for key in dbroot.keys():        
		obj = dbroot[key]        
		if isinstance(obj, modelos.Seccion):
			if(obj.tipo==tipo):
				if(obj.Vehiculo == None):
					respuesta=True        
					break
	if(respuesta):
		print("Seccion para: "+ obj.tipo+", posicion: "+str(obj.posicion)+" posicion libre")
	else:
		print("Seccion para: "+ obj.tipo+", posicion: "+str(obj.posicion)+" ocupado por")
	db.close()
	continuar=input("Presione enter para continuar.")
	menu()
def asignar_estacionamiento():
	print("Ingrese datos del Vehiculo\n")
	tipo = input('Automovil ó Motocicleta: ')
	#aca debe ir el while que controla que no sea burro el usuario
	chapa=input("Ingrese numero de chapa: ")
	modelo= input("Ingrese modelo: ")
	color=input("Ingrese color: ")
	if(tipo=="Automovil"):
		vehiculo=modelos.Automovil(chapa,modelo,color)
	else:
		vehiculo=modelos.Motocicleta(chapa,modelo,color)
	posicion=input("Ingrese posicion a estacionar: ")
	persistence= Controladores.ControladorPersistence()
	seccion=persistence.leer(posicion)
	seccion.Vehiculo=vehiculo
	seccion.hora=datetime.datetime.now()
	persistence.persistir(seccion, seccion.posicion)
	print("Seccion creada con exito")
	continuar=input("Presione enter para continuar.")
	menu()
	
def liberar_estacionamiento_por_posicion():
	posicion=input("Ingrese posicion a liberar: ")
	persistence= Controladores.ControladorPersistence()
	seccion=persistence.leer(posicion)
	seccion.Vehiculo=None
	seccion.hora=None
	persistence.persistir(seccion, seccion.posicion)
	print("Estacionamiento Liberado con exito")
	continuar=input("Presione enter para continuar.")
	menu()
	
def liberar_estacionamiento_por_chapa():
	chapa=input("Ingrese numero de chapa a liberar: ")
	db = MiZODB()
	dbroot = db.raiz  
	for key in dbroot.keys():        
		obj = dbroot[key]        
		if isinstance(obj, modelos.Seccion):
			if(obj.Vehiculo!=None):
				if(obj.Vehiculo.chapa == chapa):
					obj.Vehiculo=None
					obj.hora=None
					dbroot[obj.posicion]= obj
					transaction.commit()
	db.close()
	print("Estacionamiento Liberado con exito")
	continuar=input("Presione enter para continuar.")
	menu()
	
    
def cargar_seccion():
	print("Ingrese tipo de Seccion: ") 
	tipo = input('Normal, Motocicleta o Discapacitado: ')
	posicion= input("Ingrese posicion del estacionamiento a crear: ")
	seccion = modelos.Seccion(tipo,posicion)    
	persistence= Controladores.ControladorPersistence()
	persistence.persistir(seccion, seccion.posicion)
	print("Seccion creada con exito")
	continuar=input("Presione enter para continuar.")
	menu()
    
def listar_secciones():
	db = MiZODB()
	dbroot = db.raiz  
	for key in dbroot.keys():        
		obj = dbroot[key]        
		if isinstance(obj, modelos.Seccion):
			if(obj.Vehiculo == None):        
				print("Seccion para: "+ obj.tipo+", posicion: "+str(obj.posicion)+" posicion libre")
			else:
				print("Seccion para: "+ obj.tipo+", posicion: "+str(obj.posicion)+"\nLugar ocupado por el vehiculo modelo: "+obj.Vehiculo.modelo+", color: "+obj.Vehiculo.color+"  con chapa: "+str(obj.Vehiculo.chapa) )
	db.close()
	continuar=input("Presione enter para continuar.")
	menu()
    
def login():
    print('******** BIENVENIDOS AL SISTEMA DE RESERVAS ********')
    print('INICIAR SESION')
    print('FAVOR INGRESE: ')
    login= True
    existe= True
    while(existe):
        usuario= input('Usuario: ')
        existe=existe_usu(usuario)
    contrasenha=input('Contraseña: ')
    db=MiZODB()
    dbroot=db.raiz
    codigo = dbroot[usuario]
    while(login):
        if(contrasenha == codigo.password):
            print('ACCESO CORRECTO')
            login= False
        else:
            print('Lo sentimos, la contraseña ingresada es incorrecta.')
            contrasenha=input('Vuelva a ingresar la contraseña: ')
    db.close()
    menu()
#login()
menu()
"""
if __name__=='__main__':
    #c1=Modelos.Cliente("Sofi","Monges",111,4444)
    #c1.cargar_cliente()
    #print("hola"+str(c1.nombre))
    #c1.listar_cliente()
    eliminar_cliente(111)"""
