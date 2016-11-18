from Persistencia import MiZODB
import Controladores
import Modelos
from abc import ABCMeta, abstractmethod


def cargar_cliente():
    cli=ControladorCliente()
    cli.cargar_cliente(cl1)
    
def listar_cliente():
    ctrl_cli=ControladorCliente()
    cli=ctrl_cli.listar_clientes(usu)
	
def eliminar_cliente():
    eliminar_cliente(usu)
    cli=ControladorCliente()
	
def cargar_operador():
    ope=ControladorOperador()
    ope.cargar_operador( str(cedula.get()),str(nombre.get()), str(apellido.get()), str(usr.get()), str(contrasenha.get()))
def listar_operador():
    ctrl_ope=ControladorOperador()
    ope=ctrl_ope.listar_operadores(usu)
	
def eliminar_operador():
    eliminar_operador(usu)
    ope=ControladorOperador()


def cargar_automovil():
    auto=ControladorAutomovil()
    auto.cargar_automovil( str(chapa.get()),str(modelo.get()), str(color.get()))
def listar_automoviles():
    ctrl_auto=ControladorAutomovil()
    auto=ctrl_auto.listar_automoviles(usu)
	
def eliminar_automovil():
    eliminar_automovil(usu)
    auto=ControladorAutomovil()

def cargar_motocicleta():
    moto=ControladorMotocicleta()
    moto.cargar_motocicleta( str(chapa.get()),str(modelo.get()), str(color.get()))
def listar_motocicleta():
    ctrl_moto=ControladorMotocicleta()
    moto=ctrl_moto.listar_motocicleta(usu)
	
def eliminar_motocicleta():
    eliminar_motocicleta(usu)
    moto=ControladorMotocicleta()


if __name__=='__main__':
    #c1=Modelos.Cliente("Sofi","Monges",111,4444)
    #c1.cargar_cliente()
    #print("hola"+str(c1.nombre))
    #c1.listar_cliente()
    eliminar_cliente(111)
     
  
    
"""
def obtener_disponibilidad():




def asignar_estacionacionamiento():




def obtener_totalhoras():



def buscar_vehiculo():
"""




