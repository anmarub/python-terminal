import menu_app as mu
import securityApp as seg
import validations as val
import crud as trans
import basedatos as data

# Defino constantes para el proyecto
LOOP = True
EMPLEADOS = ['T3*9ZRLT', 'Vx*jt#NV', 'U0*yMAdU']
IVA_IMPORT = 0.20
IVA_NACIONAL = 0.10
Opcion = ""


# Solicitar el codigo de venta para el ingreso a la aplicacion
CodigoVenta = input('Digite su codigo de Empleado: ')

# Modulo de seguridad valida con el parametro codigo de venta si es correcto 
# (Tru) Ingresa (False) Sale

while not seg.ValidacionCodigo(CodigoVenta):
    CodigoVenta = input('Digite su codigo de Empleado: ')
nombreVendedor = input('Ingrese su Nombre y Apellidos: ')

val.limpiarPantalla()

# Modulo de Menu valida las opciones que tiene el usuario para acceder
mu.inicio()
mu.menuPrincipal()

#En la Opcion seleccionada, Valida el Menu principal del programa
def MenuIni(Opcion):
    while Opcion != '5':
        Opcion = input('Opcion >>>> ')
        if Opcion == '1':
            db = 'Vendedores'
            val.limpiarPantalla()
            mu.inicio()     
            mu.menuSecundario()
            MenuSec(db, Opcion)
        else:
            if Opcion == '2':
                db = 'Productos'
                val.limpiarPantalla()
                mu.inicio()
                mu.menuSecundario()
                MenuSec(db, Opcion)
            else:
                if Opcion == '3':
                    db = 'Clientes'
                    val.limpiarPantalla()
                    mu.inicio()
                    mu.menuSecundario()
                    MenuSec(db, Opcion)
                else:
                    if Opcion == '4':
                        db = 'Ventas'
                        val.limpiarPantalla()
                        mu.inicio()
                        mu.menuSecundario()
                        MenuSec(db, Opcion)
                    else:
                        if Opcion == '5':
                            val.limpiarPantalla()
                            data.Save_Data(data.Clientes, data.Vendedores, data.Productos, data.Ventas)
                            print('Has Salido del Programa!!')
                        else:
                            input('Intente de Nuevo.. Eliga una de las Opciones')
    



#Validacion del Menu Secundario del programa
def MenuSec(db, Opcion2):
    while Opcion2 != '6':
        Opcion2 = input('Opcion >>>> ')
        if Opcion2 == '1':     
            trans.Create(db, CodigoVenta, nombreVendedor)
            val.limpiarPantalla()
            mu.inicio()
            mu.menuPrincipal()
            break
        else:
            if Opcion2 == '2':
                trans.readAll(db)
                val.limpiarPantalla()
                mu.inicio()
                mu.menuPrincipal()
                break
            else:
                if Opcion2 == '3':
                    trans.readID(db)
                    val.limpiarPantalla()
                    mu.inicio()
                    mu.menuPrincipal()
                    break
                else:
                    if Opcion2 == '4':
                        trans.update(db)
                        val.limpiarPantalla()
                        mu.inicio()
                        mu.menuPrincipal()
                        break
                    else:
                        if Opcion2 == '5':
                            trans.delete(db)
                            val.limpiarPantalla()
                            mu.inicio()
                            mu.menuPrincipal()
                            break
                        else:
                            if Opcion2 == '6':
                                val.limpiarPantalla()
                                mu.inicio()
                                mu.menuPrincipal()
                                break
                            else:
                                input('Intente de Nuevo.. Eliga una de las Opciones')

# Ejecutamos la funcion de validacion del menu
MenuIni(Opcion)
