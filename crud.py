import basedatos as data
import validations as val
import menu_app as mu
from prettytable import PrettyTable

#Funciones para crear cualquiera de los elementos del menu principal
def Create(db, codVendedor, nameVendedor):
    val.limpiarPantalla()
    if db == 'Vendedores':
        nuevoVendedor = input('Ingrese la cedula del vendedor: ')
        if nuevoVendedor in data.Vendedores_id:
            print('El Vendedor Existe en la Base de datos!!')
        else:
            data.Vendedores_id.append(nuevoVendedor)
            nuevoVendedor = input('Ingrese la Nombre y Apellido del vendedor: ')
            data.Vendedores_name.append(nuevoVendedor)
            val.limpiarPantalla()
            print('Vendedor Guardado Correctamente!! Los datos ingresados son: ')
            tabla = PrettyTable(['Codigo', 'Nombre y Apellido Vendedor'])
            ltb = [data.Vendedores_id[-1], data.Vendedores_name[-1]]
            tabla.add_row(ltb)
            print(tabla)
            mu.continuar_opcion()
    else:
        if db == 'Productos':
            #Codigo de Venta
            id = input('Ingrese el codigo del producto: ')
            if id in data.Productos_id:
                print('El Producto Existe en la Base de datos!! ')
            else:
                data.Productos_id.append(id)
                #Nombre Producto
                nuevoProducto = input('Ingrese el nombre del Producto: ')
                data.Productos_name.append(nuevoProducto)
                #Tamaño del producto
                tamaño = input('Ingrese el tamaño del producto: ')
                data.Productos_tamaño.append(tamaño)
                #Color del producto
                color = input('Ingrese el color del producto: ')
                data.Productos_color.append(color)
                #Origen del producto
                nacionalidad = input('Nacionalidad del producto: ')
                data.Productos_nacionalidad.append(nacionalidad)
                #Precio del producto
                precio = input('Precio del producto: ')
                data.Productos_precio.append(precio)
                val.limpiarPantalla()
                print('Producto Guardado Correctamente!!')
                tabla = PrettyTable(['Codigo', 'Producto', 'Color', 'Tipo', 'Tamaño', 'Precio'])
                ltb = [data.Productos_id[-1], data.Productos_name[-1], data.Productos_color[-1], data.Productos_nacionalidad[-1], data.Productos_tamaño[-1], data.Productos_precio[-1]]
                tabla.add_row(ltb)
                print(tabla)
                mu.continuar_opcion()
        else:
            if db == 'Clientes':
                nuevoCliente = input('Ingrese la cedula de Cliente: ')
                if nuevoCliente in data.Clientes_id:
                    print('El Cliente Existe en la Base de Datos!!')
                else:
                    data.Clientes_id.append(nuevoCliente)
                    nuevoCliente = input('Ingrese el nombre y apellidos del Cliente: ')
                    data.Clientes_name.append(nuevoCliente)
                    val.limpiarPantalla()
                    print('Valor Guardado Correctamente!!')
                    tabla = PrettyTable(['Codigo', 'Nombre y Apellido Cliente'])
                    ltb = [data.Clientes_id[-1], data.Clientes_name[-1]]
                    tabla.add_row(ltb)
                    print(tabla)
                    mu.continuar_opcion()
            else:
                if db == 'Ventas':
                    idVenta = 1003
                    #Consecutivo de la factura
                    idVenta = idVenta + 1
                    data.venta_id.append(idVenta)
                    #Digitar el codigo del producto
                    customer = input('Digite la Cedula del cliente: ')
                    indexClient = val.validacionCliente(customer, True)
                    vlr_id_customer = data.Clientes_id[indexClient]
                    data.venta_cliente_id.append(vlr_id_customer)
                    vlr_name_cliente = data.Clientes_name[indexClient]
                    data.venta_cliente_name.append(vlr_name_cliente)
                    idProducto = input('Digite el codigo del producto: ')
                    index_prod = val.validacionProducto(idProducto, True)
                    qty = int(input('Digite la cantidad: '), )
                    data.ventas_product_qty.append(qty)
                    vlr_Prod = data.Productos_id[index_prod]
                    data.ventas_product_id.append(vlr_Prod)
                    #Llamar los otros componentes del producto para calculo
                    vlr_name = data.Productos_name[index_prod]
                    data.ventas_product_name.append(vlr_name)
                    vlr_origen = data.Productos_nacionalidad[index_prod]
                    data.ventas_product_origen.append(vlr_origen)
                    vlr_tamaño = data.Productos_tamaño[index_prod]
                    data.ventas_product_tamaño.append(vlr_tamaño)
                    vlr_Color = data.Productos_color[index_prod]
                    data.ventas_product_color.append(vlr_Color)
                    vlr_Precio = data.Productos_precio[index_prod]
                    data.ventas_product_price.append(vlr_Precio)
                    totalFactura = vlr_Precio * qty
                    data.ventas_product_total.append(totalFactura)
                    comission = val.ComisionVendedor(totalFactura)
                    impuesto = val.Impuestos(vlr_origen, totalFactura, 0.20, 0.10)
                    totalPagar = totalFactura + impuesto
                    mu.facturaImprimir(codVendedor, nameVendedor,vlr_name,qty,val.fecha(), comission, vlr_origen, vlr_Precio, impuesto, totalPagar, vlr_name_cliente, vlr_id_customer)

                print('Factura Guardada Correctamente!! El numero de su factura es: ', idVenta)
                mu.continuar_opcion()

#Funciones para llamar un id especifico de las opciones del crud en cada opcion del menu principal
def readID(db):
    val.limpiarPantalla()
    if db == 'Vendedores':
        vdb = data.Vendedores_id
        #Funcion para validar si la base de datos tiene elementos.
        value = val.data_Validations(vdb)
        if value:
            idElement = input('Ingrese el id del Vendedor a Buscar: ')
            if idElement in data.Vendedores_id:
                x = data.Vendedores_id.index(idElement)
                val.limpiarPantalla()
                print('Vendedor encontrado satisfactoriamente!! los datos son: ')
                tabla = PrettyTable(['Codigo', 'Nombre y Apellido Vendedor'])
                ltb = [data.Vendedores_id[x], data.Vendedores_name[x]]
                tabla.add_row(ltb)
                print(tabla)
                mu.continuar_opcion()
            else:
                print('la cedula del vendedor no existe!!')
                mu.continuar_opcion()
        else:
            mu.continuar_opcion()
    else:
        if db == 'Productos':
                vdb = data.Productos_id
                value = val.data_Validations(vdb)
                if value:
                    idElement = input('Ingrese el id del Producto a Buscar: ')
                    if idElement in data.Productos_id:
                        x = data.Productos_id.index(idElement)
                        print('Producto encontrado satisfactoriamente!! los datos son: ')
                        tabla = PrettyTable(['Codigo', 'Producto', 'Color', 'Tipo', 'Tamaño', 'Precio'])
                        ltb = [data.Productos_id[x], data.Productos_name[x], data.Productos_color[x], data.Productos_nacionalidad[x], data.Productos_tamaño[x], data.Productos_precio[x]]
                        tabla.add_row(ltb)
                        print(tabla)
                        mu.continuar_opcion()
                    else:
                        print('El Elemento no Existe en la base de datos!!')
                        mu.continuar_opcion()
                else:
                    mu.continuar_opcion()
        else:
            if db == 'Clientes':
                vdb = data.Clientes_id
                value = val.data_Validations(vdb)
                if value:
                    idElement = input('Ingrese el id del Cliente a Buscar: ')
                    if idElement in data.Clientes_id:
                        x = data.Clientes_id.index(idElement)
                        print('Clientes encontrado satisfactoriamente!! los datos son: ')
                        tabla = PrettyTable(['Codigo', 'Nombre y Apellido Cliente'])
                        ltb = [data.Clientes_id[x], data.Clientes_name[x]]
                        tabla.add_row(ltb)
                        print(tabla)
                        mu.continuar_opcion()
                    else:
                        print('El Elemento no Existe en la base de datos!!')
                        mu.continuar_opcion()
                else:
                    mu.continuar_opcion()
            else:
                if db == 'Ventas':
                    vdb = data.venta_id
                    value = val.data_Validations(vdb)
                    if value:
                        idElement = input('Ingrese el id de la Factura a Buscar: ')
                        if idElement in data.venta_id:
                            x = data.venta_id.index(idElement)
                            print('Ventas encontrado satisfactoriamente!! los datos son: ')
                            tabla = PrettyTable(['Factura', 'Cedula', 'Cliente', 'Cod. Producto', 'Nombre Producto', 'Color', 'Origen', 'Precio', 'Cantidad', 'Valor Total'])
                            ltb = [data.venta_id[x], data.venta_cliente_id[x], data.venta_cliente_name[x], data.ventas_product_id[x], data.ventas_product_name[x], data.ventas_product_color[x], data.ventas_product_origen[x], data.ventas_product_price[x], data.ventas_product_qty[x], data.ventas_product_total[x]]
                            tabla.add_row(ltb)
                            print(tabla)
                            mu.continuar_opcion()
                        else:
                            print('El Elemento no Existe en la base de datos!!')
                            mu.continuar_opcion()
                    else:
                        mu.continuar_opcion()

#Funciones para listar cualquiera de los elementos del menu principal
def readAll(db):
    val.limpiarPantalla()
    if db == 'Vendedores':
        vdb = data.Vendedores_id
        value = val.data_Validations(vdb)
        if value:
            lineas = []
            tabla = PrettyTable(['Codigo', 'Nombre y Apellido Vendedor'])
            for a, b in zip(data.Vendedores_id, data.Vendedores_name):
                ltb = [a, b]
                lineas.append(ltb)
                tabla.add_row(ltb)  
            print(tabla)
            mu.continuar_opcion()
    else:
        if db == 'Productos':
            vdb = data.Productos_id
            value = val.data_Validations(vdb)
            if value:
                lineas = []
                tabla = PrettyTable(['Codigo', 'Producto', 'Color', 'Tipo', 'Tamaño', 'Precio'])
                for a, b, c, d, e, f in zip(data.Productos_id, data.Productos_name, data.Productos_color, data.Productos_nacionalidad, data.Productos_tamaño, data.Productos_precio):
                    ltb = [a, b, c, d, e, f]
                    lineas.append(ltb)
                    tabla.add_row(ltb)                
                print(tabla)
                mu.continuar_opcion()
            else:
                mu.continuar_opcion()
        else:
            if db == 'Clientes':
                vdb = data.Clientes_id
                value = val.data_Validations(vdb)
                if value:
                    lineas = []
                    tabla = PrettyTable(['Codigo', 'Nombre y Apellido Cliente'])
                    for a, b in zip(data.Clientes_id, data.Clientes_name):
                        ltb = [a, b]
                        lineas.append(ltb)
                        tabla.add_row(ltb)
                    print(tabla)
                    mu.continuar_opcion()
                else:
                    mu.continuar_opcion()
            else:
                if db == 'Ventas':
                    vdb = data.venta_id
                    value = val.data_Validations(vdb)
                    if value:
                        lineas = []
                        tabla = PrettyTable(['Factura', 'Codigo Producto', 'Nombre Producto', 'Color', 'Origen', 'Precio', 'Cantidad', 'Valor Total'])
                        for a, b, c, d, e, f, g, h in zip(data.venta_id, data.ventas_product_id, data.ventas_product_name, data.ventas_product_color, data.ventas_product_origen, data.ventas_product_price, data.ventas_product_qty, data.ventas_product_total):
                            ltb = [a, b, c, d, e, f, g, h]
                            lineas.append(ltb)
                            tabla.add_row(ltb)
                        print(tabla)
                        mu.continuar_opcion()
                    else:
                        mu.continuar_opcion()

#Funciones para actualizar cualquiera de los elementos del menu principal
def update(db):
    val.limpiarPantalla()
    if db == 'Vendedores':
        eliminarElement = input('Ingrese el id del vendedor para actualizar: ')
        if eliminarElement in data.Vendedores_id:
            x = data.Vendedores_id.index(eliminarElement)
            tabla = PrettyTable(['Codigo', 'Nombre y Apellido Vendedor'])
            ltb = [data.Vendedores_id[x], data.Vendedores_name[x]]
            tabla.add_row(ltb)
            print(tabla)
            nuevoElemento = input('confirme nuevemente el numero de cedula del vendedor: ')
            data.Vendedores_id[x] = nuevoElemento
            nuevoElemento = input('confirme nuevemente el nombre del vendedor: ')
            data.Vendedores_name[x] = nuevoElemento
            val.limpiarPantalla()
            tabla = PrettyTable(['Codigo', 'Nombre y Apellido Vendedor'])
            ltb = [data.Vendedores_id[x], data.Vendedores_name[x]]
            tabla.add_row(ltb)
            print(tabla)
            mu.continuar_opcion()
        else:
            print('El Elemento no Existe en la base de datos!!')
            mu.continuar_opcion()
    else:
        if db == 'Productos':
            eliminarElement = input('Ingrese el id del producto para actualizar: ')
            if eliminarElement in data.Productos_id:
                x = data.Productos_id.index(eliminarElement)
                tabla = PrettyTable(['Codigo', 'Producto', 'Color', 'Tipo', 'Tamaño', 'Precio'])
                ltb = [data.Productos_id[x], data.Productos_name[x], data.Productos_color[x], data.Productos_nacionalidad[x], data.Productos_tamaño[x], data.Productos_precio[x]]
                tabla.add_row(ltb)
                print(tabla)
                id = input('Confirme el codigo del producto: ')
                data.Productos_id[x] = id
                name = input('Confirme el nombre del Producto: ')
                data.Productos_name[x] = name
                tamaño = input('Confirme el tamaño del producto: ')
                data.Productos_tamaño[x] = tamaño
                color = input('Confirme el color del producto: ')
                data.Productos_color[x] = color
                nacionalidad = input('Conforme Nacionalidad del producto: ')
                data.Productos_nacionalidad[x] = nacionalidad
                precio = input('Confirme el Precio del producto: ')
                data.Productos_precio[x] = precio
                print('Valor Actualizado Correctamente!!')
                val.limpiarPantalla()
                tabla = PrettyTable(['Codigo', 'Producto', 'Color', 'Tipo', 'Tamaño', 'Precio'])
                ltb = [data.Productos_id[x], data.Productos_name[x], data.Productos_color[x], data.Productos_nacionalidad[x], data.Productos_tamaño[x], data.Productos_precio[x]]
                tabla.add_row(ltb)
                print(tabla)
                mu.continuar_opcion()
            else:
                print('El Elemento no Existe en la base de datos!!')
                mu.continuar_opcion()
        else:
            if db == 'Clientes':
                eliminarElement = input('Ingrese el id del Cliente para actualizar: ')
                if eliminarElement in data.Clientes_id:
                    x = data.Clientes_id.index(eliminarElement)
                    tabla = PrettyTable(['Codigo', 'Nombre y Apellido Cliente'])
                    ltb = [data.Clientes_id[x], data.Clientes_name[x]]
                    tabla.add_row(ltb)
                    print(tabla)
                    Client = input('Confirme el numero de documento del cliente: ')
                    data.Clientes_id[x] = Client
                    Client = input('Confirme el nombre y apellido del cliente: ')
                    data.Clientes_name[x] = Client
                    print('Valor Actualizado Correctamente!!')
                    val.limpiarPantalla()
                    tabla = PrettyTable(['Codigo', 'Nombre y Apellido Cliente'])
                    ltb = [data.Clientes_id[x], data.Clientes_name[x]]
                    tabla.add_row(ltb)
                    print(tabla)
                    mu.continuar_opcion()
                else:
                    print('El Elemento no Existe en la base de datos!!')
                    mu.continuar_opcion()
            else:
                if db == 'Ventas':
                    eliminarElement = input('Ingrese el numero de factura para actualizar: ')
                    if eliminarElement in data.venta_id:
                        x = data.venta_id.index(eliminarElement)
                        tabla = PrettyTable(['Factura', 'Cedula', 'Cliente', 'Cod. Producto', 'Nombre Producto', 'Color', 'Origen', 'Precio', 'Cantidad', 'Valor Total'])
                        ltb = [data.venta_id[x], data.venta_cliente_id[x], data.venta_cliente_name[x], data.ventas_product_id[x], data.ventas_product_name[x], data.ventas_product_color[x], data.ventas_product_origen[x], data.ventas_product_price[x], data.ventas_product_qty[x], data.ventas_product_total[x]]
                        tabla.add_row(ltb)
                        print(tabla)
                        fact = input('Confirme el id del producto actualizar: ')
                        y = data.Productos_id.index(fact)
                        a1 = data.Productos_name[y]
                        data.ventas_product_id[x] = a1
                        a2 = data.Productos_nacionalidad[y]
                        data.ventas_product_origen[x] = a2
                        a3 = data.Productos_tamaño[y]
                        data.ventas_product_tamaño[x] = a3
                        a4 = data.Productos_precio[y]
                        data.ventas_product_price[x] = a4
                        a5 = data.Productos_color[y]
                        data.ventas_product_color[x] = a5
                        qty = int(input('Confirme la cantidad del producto: '), )
                        data.ventas_product_qty[x] = qty
                        data.ventas_product_total[x]
                        totalFactura = a4* qty
                        impuesto = val.Impuestos(a2, totalFactura, 0.20, 0.10)
                        totalPagar = totalFactura + impuesto
                        data.ventas_product_total = totalPagar
                        print('Valor Actualizado Correctamente!!')
                        tabla = PrettyTable(['Factura', 'Cedula', 'Cliente', 'Cod. Producto', 'Nombre Producto', 'Color', 'Origen', 'Precio', 'Cantidad', 'Valor Total'])
                        ltb = [data.venta_id[x], data.venta_cliente_id[x], data.venta_cliente_name[x], data.ventas_product_id[x], data.ventas_product_name[x], data.ventas_product_color[x], data.ventas_product_origen[x], data.ventas_product_price[x], data.ventas_product_qty[x], data.ventas_product_total[x]]
                        tabla.add_row(ltb)
                        print(tabla)
                        mu.continuar_opcion()
                    else:
                        print('El Elemento no Existe en la base de datos!!')
                        mu.continuar_opcion()


def delete(db):
    val.limpiarPantalla()
    eliminarElement = input(f'Ingrese el id del {db} a Eliminar: ')    
    if db == 'Vendedores':
        if eliminarElement in data.Vendedores_id:
            x = data.Vendedores_id.index(eliminarElement)
            tabla = PrettyTable(['Codigo', 'Nombre y Apellido Vendedor'])
            ltb = [data.Vendedores_id[x], data.Vendedores_name[x]]
            tabla.add_row(ltb)
            print(tabla)
            desicion = input('Esta seguro de eliminar el registro? Si / No ►►: ').upper()
            desicion = val.validacionConfirmation(desicion, True)
            if desicion == 'SI':
                data.Vendedores_id.pop(x)
                data.Vendedores_name.pop(x)
                val.limpiarPantalla()
                print('Vendedor Eliminado Correctamente !!')
                mu.continuar_opcion()
            else:
                print('Solicitud Cancelada!!')
                mu.continuar_opcion()
        else:
            print('El id no Existe en la base de datos!!')
            mu.continuar_opcion()
    else:
        if db == 'Productos':
            if eliminarElement in data.Productos_id:
                x = data.Productos_id.index(eliminarElement)
                tabla = PrettyTable(['Codigo', 'Producto', 'Color', 'Tipo', 'Tamaño', 'Precio'])
                ltb = [data.Productos_id[x], data.Productos_name[x], data.Productos_color[x], data.Productos_nacionalidad[x], data.Productos_tamaño[x], data.Productos_precio[x]]
                tabla.add_row(ltb)
                print(tabla)
                desicion = input('Esta seguro de eliminar el registro? Si / No ►►: ').upper()
                desicion = val.validacionConfirmation(desicion, True)
                if desicion == 'SI':
                    data.Productos_id.pop(x)
                    data.Productos_name.pop(x)
                    data.Productos_precio.pop(x)
                    data.Productos_color.pop(x)
                    data.Productos_nacionalidad.pop(x)
                    data.Productos_color.pop(x)
                    print('Valor Eliminado Correctamente!!')
                    mu.continuar_opcion()
                else:
                    print('Solicitud Cancelada!!')
                    mu.continuar_opcion()
            else:
                print('El id no Existe en la base de datos!!')
                mu.continuar_opcion()
        else:
            if db == 'Clientes':
                if eliminarElement in data.Clientes_id:
                    x = data.Clientes_id.index(eliminarElement)
                    tabla = PrettyTable(['Codigo', 'Nombre y Apellido Cliente'])
                    ltb = [data.Clientes_id[x], data.Clientes_name[x]]
                    tabla.add_row(ltb)
                    print(tabla)
                    desicion = input('Esta seguro de eliminar el registro? Si / No ►►: ').upper()
                    desicion = val.validacionConfirmation(desicion, True)
                    if desicion == 'SI':
                        data.Clientes_id.pop(x)
                        data.Clientes_name.pop(x)
                        print('Valor Eliminado Correctamente!!')
                        mu.continuar_opcion()
                    else:
                        mu.continuar_opcion()
                else:
                    print('El id no Existe en la base de datos!!')
                    mu.continuar_opcion()
            else:
                if db == 'Ventas':
                    if eliminarElement in data.venta_id:
                        x = data.venta_id.index(eliminarElement)
                        tabla = PrettyTable(['Factura', 'Cedula', 'Cliente', 'Cod. Producto', 'Nombre Producto', 'Color', 'Origen', 'Precio', 'Cantidad', 'Valor Total'])
                        ltb = [data.venta_id[x], data.venta_cliente_id[x], data.venta_cliente_name[x], data.ventas_product_id[x], data.ventas_product_name[x], data.ventas_product_color[x], data.ventas_product_origen[x], data.ventas_product_price[x], data.ventas_product_qty[x], data.ventas_product_total[x]]
                        tabla.add_row(ltb)
                        print(tabla)
                        desicion = input('Esta seguro de eliminar el registro? Si / No ►►: ').upper()
                        desicion = val.validacionConfirmation(desicion, True)
                        if desicion == 'SI':
                            data.venta_id.pop(x)
                            data.ventas_product_id.pop(x)
                            data.ventas_product_name.pop(x)
                            data.ventas_product_tamaño.pop(x)
                            data.ventas_product_color.pop(x)
                            data.ventas_product_origen.pop(x)
                            data.ventas_product_price.pop(x)
                            data.ventas_product_qty.pop(x)
                            data.ventas_product_total.pop(x)
                            print('Valor Eliminado Correctamente!!')
                            mu.continuar_opcion()
                        else:
                            mu.continuar_opcion()
                    else:
                        print('El id no Existe en la base de datos!!')
                        mu.continuar_opcion()
