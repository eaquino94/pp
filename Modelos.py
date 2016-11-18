
from Persistencia import MiZODB
from abc import ABCMeta, abstractmethod
import Controladores



class Persona(metaclass=ABCMeta):

    """Clase abstracta que modela a una persona"""

    def __init__ (self, nombre, apellido, cedula):

        self.nombre=nombre
        self.apellido=apellido
        self.cedula=cedula	

class Cliente(Persona):
    """Clase que modela los atibutos y las funciones de  los clientes descendientes de persona"""
    def __init__ (self,nombre,apellido, cedula,nro_telefonico):

        Persona.__init__(self,nombre, apellido, cedula )

        self.nro_telefonico=nro_telefonico

    def cargar_cliente(self):

        persistence= Controladores.ControladorPersistence()

        persistence.persistir(self, self.cedula)


    def eliminar_cliente(self,clave):

        persistence= ControladorPersistence()

        persistence.eliminar(clave)

    def listar_cliente(self):

        db = MiZODB()

        dbroot = db.raiz
        lista=[[],[]]
        
        for key in dbroot.keys():
            
            obj = dbroot[key]
            
            if isinstance(obj, Cliente):
                
                lista[0].append(key)
                
                
                lista[1].append("Cliente: "+ obj.nombre+" Apellido"+obj.apellido+ ", N° Telefonico: "+str(obj.nro_telefonico))

                db.close()		
               
            return lista


class Operador(Persona):

    """Clase que modela los atibutos y las funciones de un operador descendiente de la clase Persona"""

    def __init__ (self, nombre, apellido, cedula,usr, contrasenha):

        Persona.__init__(self, nombre, apellido, cedula)

        self.usr=usr

        self.contrasenha=contrasenha
        
    def cargar_operador(self):

        persistence= ControladorPersistence()

        persistence.persistir(self, self.cedula)

    def eliminar_operador(self,clave):

        persistence= ControladorPersistence()

        persistence.eliminar(clave)



    def listar_operador(self):
        db = MiZODB()
        dbroot = db.raiz
        lista=[[],[]]
        for key in dbroot.keys():
            obj = dbroot[key]
            if isinstance(obj, operador):
                lista[0].append(key)
                lista[1].append("Nombre: "+ obj.nombre+"Apellido:"+obj.apellido+"Usuario "+obj.usr)
            db.close()		
            return lista

class Vehiculo(metaclass=ABCMeta):

    #Clase abstracta que modela basicamente un vehiculo

    def __init__(self, chapa, modelo, color):
        self.chapa=chapa

        self.modelo=modelo

        self.color=color
	

class Automovil(Vehiculo):

    #Clase que modela los atributos y funciones de la clase automovil descendiente de vehiculo

    def __init__(self, chapa, modelo, color, tarifa):

        Vehiculo.__init__(self, chapa, modelo, color)

        self.tarifa=3000

    def cargar_automovil(self):

        persistence= ControladorPersistence()

        persistence.persistir(self, self.automovil)



    def eliminar_automovil(self,clave):

        persistence= ControladorPersistence()

        persistence.eliminar(clave)



    def listar_automovil(self):
        db = MiZODB()
        dbroot = db.raiz
        lista=[[],[]]
        for key in dbroot.keys():
           obj = dbroot[key]
           if isinstance(obj, automovil):
                lista[0].append(key)
                lista[1].append("Chapa: "+ obj.chapa+"Modelo:"+obj.modelo+"Color: "+obj.color)
                db.close()
           return lista

	
class Motocicleta(Vehiculo):
    def __init__(self, chapa, modelo, color, tarifa):
        Vehiculo.__init__(self, chapa, modelo, color)
        self.tarifa=3000
        
    def cargar_motocicleta(self):
        persistence= ControladorPersistence()
        persistence.persistir(self, self.motocicleta)
        
    def eliminar_motocicleta(self,clave):
        persistence= ControladorPersistence()
        persistence.eliminar(clave)


    def listar_motocicleta(self):
        db = MiZODB()
        dbroot = db.raiz
        lista=[[],[]]
        for key in dbroot.keys():
           obj = dbroot[key]
           if isinstance(obj, motocicleta):
               lista[0].append(key)
               lista[1].append("Chapa: "+ obj.chapa+"Modelo:"+obj.modelo+"Color: "+obj.color)
               db.close()		
           return lista


class Ticket():

    def __init__(self, vehiculo, fecha, hora_entrada, hora_salida):

        self.estacionamiento=Estacionamiento()

        self.vehiculo=Vehiculo()

        self.fecha=fecha

        self.hora_entrada=hora_entrada

        self.hora_salida=hora_salida


class Reservable():

    def __init__(self,cliente,intervalo_tiempo,espacio):

        pass

    def reservar_estacionamiento():

        pass
"""
class Seccion():

    def __init__(self, espacio):

        self.espacio=espacio[]

    def crear_seccion():

        self.espacio=espacio

        for i in espacio.len

            espacio[i]=None


class Estacionamiento():

    def _init__(self,denominacion,direccion,seccion):

        self.denominacion

        self.direccion=direccion

        self.seccion=Seccion()

	

		

########################################################################		

		

secciondisc=crearseccion()

seccionautos=crearseccion()

seccionmotos=crearseccion()





	
"""
