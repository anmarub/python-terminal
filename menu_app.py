#Funciones Menu de la app
def inicio():
    print('=' * 50)
    print('|', 'Empresa: Market cicle', '-' ,'Sistema Principal', '|')
    print('=' * 50)

def menuPrincipal():
    print('[1]. Vendedores')
    print('[2]. Productos')
    print('[3]. Clientes')
    print('[4]. Ventas')
    print('[5]. Salir')
    print('=' * 50)

def menuSecundario():
    print('[1]. Crear')
    print('[2]. Listar')
    print('[3]. Consultar')
    print('[4]. Actualizar')
    print('[5]. Eliminar')
    print('[6]. Salir')
    print('=' * 50)

def marca():
    print(30 * '-' , 'Marca de Bicicletas' , 30 * '-')
    print('Selecciones una Opcion: Specialized [1] treck [2] BMC [3] Salir[4]')
    print(67 * '-')

def color():
    print(30 * '-' , 'Colores de Bicicletas' , 30 * '-')
    print('Selecciones una Opcion: roja [1] negra [2] roja-negra [3] Salir[4]')
    print(67 * '-')

def tamaño():
    print(30 * '-' , 'Tamaño de Bicicletas' , 30 * '-')
    print('Selecciones una Opcion: S [1] M [2] L [3] XL [4] Salir[5]')
    print(67 * '-')

def facturaImprimir(codigoVendedor, nameVendedor, marca, cantidad, fecha, comision, origen, price, iva_product, valorTotal, nombreCliente, identificacion):
    print('=' * 120)
    print('|',  ' ' * 32, 'Empresa: Market cicle', '-' ,'Gestion de Ventas', ' ' * 41, '|')
    print('=' * 120)
    print('|', 'Código vendedor','|', 'Nombre vendedor                     ', '|', 'Marca           ', '|', 'Cantidad', '|', 'Fecha Venta', '|', 'Total Comision ', '|', )
    print('-' * 120)
    print('|', codigoVendedor, '       ','|', nameVendedor, ' ' * 25, '|', marca , '|', cantidad, '|', fecha, '|', comision, '|', )
    print('-' * 120)
    print(' ')

    print('=' * 120)
    print('|',  ' ' * 34, 'Detalle de Venta para el Cliente', ' ' * 48, '|')
    print('=' * 120)
    print('Nombre Cliente: ', nombreCliente, 'Identificacion: ', identificacion)
    print('=' * 120)
    print('|', 'Fecha venta    ','|', 'Marca Bicicleta         ', '|', 'Tipo            ', '|', 'Cantidad', '|', 'Valor unidad', '|', 'Valor Iva ', '|', 'Total a pagar', '|')
    print('-' * 120)
    print('|', fecha,'|', marca, '|', origen, '|', cantidad, '|', price, '|', iva_product, '|', valorTotal, '|')
    print('-' * 120)

def continuar_opcion():
    print('=' * 60)
    print('')
    input('Presion ◄◄ Enter ╝ ►► para continuar')


