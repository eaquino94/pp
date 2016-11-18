from Persistencia import MiZODB,transaction
import Persistencia
import Vistas
import Modelos
class ControladorPersistence():
    """Clase Controlador de la clase MiZODB"""
    def persistir(self,obj,clave):
        db=MiZODB()
        dbroot=db.raiz
        dbroot[clave]= obj
        transaction.commit()
        db.close()
        
    def leer(self,clave):
        try:
            db=MiZODB()
            dbroot=db.raiz
            obj=dbroot[clave]
            db.close()
        except:
            db.close()
            raise Exception('El objeto no existe')
        return obj
        
    def eliminar(self,clave):
        db=MiZODB()
        dbroot=db.raiz
        del dbroot[clave]
        transaction.commit()
        db.close()

	
class ControladorCliente():
    """Clase Controlador de Clientes"""
    def cargar_cliente(self,cedula,nombre, apellido,nro_telefonico):
        if ( cliente=='' or cliente == None):
            raise Exception('Cliente vacio')
        else:
            persistence = ControladorPersistence()
            try:
                persistence.leer(cliente)
            except:
                c1.cargar_cliente()
                transaction.commit()
            else:
                raise Exception('El cliente ya existe')
    def eliminar_cliente(self,cliente, cedula):
        cliente.eliminar_cliente(cedula)
    def listar_cliente(self,cliente):
        return cliente.listar_clientes()


class ControladorOperador():
    """Clase Controlador de usuarios operadores"""
    def cargar_operador(self,cedula,nombre,apellido,usr,contrasenha):
        if ( operador=='' or operador == None):
            raise Exception('Operador vacio')
        else:
            persistence = ControladorPersistence()
            try:
                persistence.leer(operador)
            except:
                a1.cargar_operador()
            else:
                raise Exception('El operador ya existe')
    def eliminar_operador(self,operador, cedula):
        operador.eliminar_operador(cedula)
    def listar_operador(self,operador):
        return usuario.listar_operador()

class ControladorAutomovil():
    """Clase Controlador de la clase Automovil"""
    def cargar_automovil(self,chapa, modelo, color):
        if ( automovil=='' or automovil == None):
            raise Exception('automovil vacio')
        else:
            persistence = ControladorPersistence()
            try:
                persistence.leer(automovil)
            except:
                a1.cargar_automovil()
            else:
                raise Exception('El automovil ya existe')
    def eliminar_automovil(self,automovil, chapa):
        automovil.eliminar_automovil(chapa)
    def listar_automovil(self,automovil):
         return automovil.listar_automoviles()



class ControladorMotocicleta():
    "Clase Controlador de la clase Motocicleta"
    def cargar_motocicleta(self,chapa, modelo, color):
        if (motocicleta=='' or motocicleta == None):
            raise Exception('motocicleta vacia')
        else:
            persistence = ControladorPersistence()
            try:
                persistence.leer(motocicleta)
            except:
                a1.cargar_motocicleta()
            else:
                raise Exception('La motocicleta ya existe')
    def eliminar_motocicleta(self,motocicleta, chapa):
        motocicleta.eliminar_motocicleta(chapa)
    def listar_motocicleta(self,motocicleta):
        return motocicleta.listar_motocicleta()
	
class ControladorEstacionamiento():
	def cargar_estacionamiento(self, denominacion, direccion, propietario, secciones):
		if ( estacionamiento=='' or estacionamiento == None):
		    raise Exception('estacionamiento vacio')
		else:
		    persistence = ControladorPersistence()
		    try:
		        persistence.leer(estacionamiento)
		    except:
		        e1.listar_estacionamiento()
		    else:
		        raise Exception('El estacionamiento ya existe')
	def listar_estacionamiento(self,estacionamiento):
		 return estacionamiento.listar_estacionamiento()
     
class ControladorSeccion():
	def cargar_seccion(self,capacidad):
		if(seccion=="" or seccion==None):
		    raise Exception('Seccion vacia')
		else:
		    persistence= ControladorPersistence()
		    try:
		        persistence.leer(seccion)
		    except:
		        s1.cargar_seccion
		    else:
		         raise Exception('La seccion ya existe')
