#Importacion de librerias
from datetime import datetime
import os
import basedatos as data

#Validacion de tipo Impuesto ya sea nacional o importado 
def Impuestos(origen, price, IVA_IMPORT, IVA_NACIONAL):
    if origen == 'IMPORTADA':
        iva = price * IVA_IMPORT
    else:
        if origen == 'IMPORTADA':
            iva = price * IVA_NACIONAL
    return iva

#Validacion de Comisiones segun valor total de compra
def ComisionVendedor(VlrCompra):
    if VlrCompra >= 200000 and VlrCompra <= 799999:
        VlrComision = VlrCompra * 0.05
    else:
        if VlrCompra >= 800000 and VlrCompra <= 1499999:
            VlrComision = VlrCompra * 0.10
        else:
            if VlrCompra >= 1500000:
                VlrComision = VlrCompra * 0.15
            else:
                VlrComision = 0
    return VlrComision

#Funcion que valida el codigo del producto cada vez que se solicite.
def validacionProducto(idProducto, VlrVerdad):
    while VlrVerdad:
        if idProducto in data.Productos_id:
            index_product = data.Productos_id.index(idProducto)
            print('Informacion Correcta...')
            input("Presione la tecla Enter para continuar")
            break
        else:
            print('El producto no existe, intente nuevamente')
            VlrVerdad = False
    
    return index_product

def validacionCliente(id_Cliente, VlrVerdad):
    while VlrVerdad:
        if id_Cliente in data.Clientes_id:
            index_client = data.Clientes_id.index(id_Cliente)
            print('Informacion Correcta...')
            input("Presione la tecla Enter para continuar")
            break
        else:
            print('El Cliente no existe, intente nuevamente')
            id_Cliente = input('Digite la Cedula del cliente: ')
            
    
    return index_client

def limpiarPantalla():
    os.system('clear')

def fecha():
    today = datetime.now()
    return today

def data_Validations(entity):
    if entity:
        print('La Base de datos contiene informacion')
        return True
    else:
        print('No  hay informacion en la base de datos')
        return False


def validacionConfirmation(Opcion, VlrVerdad):
    while VlrVerdad:
        if Opcion == 'SI' or Opcion == 'NO':
            VlrVerdad = False
        else:
            print('La opcion seleccionada no es correcta ► SI ► NO ')
            Opcion = input('Esta seguro de eliminar el registro? Si / No ►►: ').upper()
    return Opcion