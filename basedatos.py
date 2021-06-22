import pickle

# base de datos relacionados con el Clientes, todas deben tener la
# misma longitud de datos
#                   0       1
Clientes_id = []
Clientes_name = []
Clientes = [Clientes_id, Clientes_name]

# base de datos relacionados con el Vendedores, todas deben tener la
# misma longitud de datos
#                   0           1
Vendedores_id = []
Vendedores_name = []
Vendedores = [Vendedores_id, Vendedores_name]

# base de datos relacionados con el producto, todas deben tener la
# misma longitud de datos
#                   0       1       2
Productos_id = []
Productos_name = []
Productos_nacionalidad = []
Productos_tamaño = []
Productos_precio = []
Productos_color = []
Productos = [Productos_id, Productos_name, Productos_nacionalidad, Productos_tamaño, Productos_precio, Productos_color]

# base de datos relacionados con las ventas, todas deben tener la
# misma longitud de datos
#                   0       1       2
venta_id = []
venta_cliente_id = []
venta_cliente_name = []
ventas_product_id = []
ventas_product_name = []
ventas_product_tamaño = []
ventas_product_color = []
ventas_product_origen = []
ventas_product_price = []
ventas_product_qty = []
ventas_product_total = []
Ventas = [venta_id, venta_cliente_id, venta_cliente_name, ventas_product_id, ventas_product_name, ventas_product_tamaño, ventas_product_color, ventas_product_origen, ventas_product_price, ventas_product_qty, ventas_product_total]

# Guardar datos en archivos binarios
def Save_Data(Clientes, Vendedores, Productos, Ventas):
    #print(Clientes_id, Clientes_name)
    try:
        archivo = open('Clientes', 'rb')
        Clientes = pickle.load(archivo)
        archivo.close()
    except:
        print('El Archivo no Existe... Se crea uno')
        archivo = open('Clientes', 'wb')
        pickle.dump(Clientes, archivo)
    try:
        archivo = open('Vendedores', 'rb')
        Vendedores = pickle.load(archivo)
        archivo.close()
    except:
        print('El Archivo no Existe... Se crea uno')
        archivo = open('Vendedores', 'wb')
        pickle.dump(Vendedores, archivo)
    try:
        archivo = open('Productos', 'rb')
        Productos = pickle.load(archivo)
        archivo.close()
    except:
        print('El Archivo no Existe... Se crea uno')
        archivo = open('Productos', 'wb')
        pickle.dump(Productos, archivo)
    try:
        archivo = open('Ventas', 'rb')
        Ventas = pickle.load(archivo)
        archivo.close()
    except:
        print('El Archivo no Existe... Se crea uno')
        archivo = open('Ventas', 'wb')
        pickle.dump(Ventas, archivo)

# Cargar datos en archivos binarios
try:
    Clientes = pickle.load(open('Clientes', 'rb'))
    for c_id in range(len(Clientes)):
        cid = Clientes[0][c_id]
        Clientes_id.append(cid)
    
    for c_name in range(len(Clientes)):
        cn = Clientes[1][c_name]
        Clientes_name.append(cn)
except:
    print('El Archivo no Existe... Establezca uno')
try:
    Vendedores = pickle.load(open('Vendedores', 'rb'))
    for v_id in range(len(Vendedores)):
        vid = Vendedores[0][v_id]
        Vendedores_id.append(vid)
    
    for v_name in range(len(Vendedores)):
        vn = Vendedores[1][v_name]
        Vendedores_name.append(vn)
except:
    print('El Archivo no Existe... Establezca uno')
try:
    Productos = pickle.load(open('Productos', 'rb'))
    for p_id in range(len(Productos[0])):
        pid = Productos[0][p_id]
        Productos_id.append(pid)
    
    for p_name in range(len(Productos[1])):
        pn = Productos[1][p_name]
        Productos_name.append(pn)
    
    for p_org in range(len(Productos[2])):
        po = Productos[2][p_org]
        Productos_nacionalidad.append(po)
    
    for p_tam in range(len(Productos[3])):
        pt = Productos[3][p_tam]
        Productos_tamaño.append(pt)
    
    for p_pre in range(len(Productos[4])):
        pp = Productos[4][p_pre]
        Productos_precio.append(pp)

    for p_co in range(len(Productos[5])):
        pc = Productos[5][p_co]
        Productos_color.append(pc)
except:
    print('El Archivo no Existe... Establezca uno')
try:
    Ventas = pickle.load(open('Ventas', 'rb'))
    for v_id in range(len(Ventas[0])):
        vid = Ventas[0][v_id]
        venta_id.append(vid)
    
    for v_cid in range(len(Ventas[1])):
        vci = Ventas[1][v_cid]
        venta_cliente_id.append(vci)
    
    for v_cna in range(len(Ventas[2])):
        vcn = Ventas[2][v_cna]
        venta_cliente_name.append(vcn)
    
    for v_pid in range(len(Ventas[3])):
        vpi = Ventas[3][v_pid]
        ventas_product_id.append(vpi)
    
    for v_pna in range(len(Ventas[4])):
        vpn = Ventas[4][v_pna]
        ventas_product_name.append(vpn)

    for v_pt in range(len(Ventas[5])):
        vpt = Ventas[5][v_pt]
        ventas_product_tamaño.append(vpt)
    
    for v_pc in range(len(Ventas[6])):
        vpc = Ventas[6][v_pc]
        ventas_product_color.append(vpc)
    
    for v_po in range(len(Ventas[7])):
        vpo = Ventas[7][v_po]
        ventas_product_origen.append(vpo)
    
    for v_pp in range(len(Ventas[8])):
        vpp = Ventas[8][v_pp]
        ventas_product_price.append(vpp)
    
    for v_pq in range(len(Ventas[9])):
        vpq = Ventas[9][v_pq]
        ventas_product_qty.append(vpq)
    
    for v_pt in range(len(Ventas[10])):
        vpt = Ventas[10][v_pt]
        ventas_product_total.append(vpt)
except:
    print('El Archivo no Existe... Establezca uno')


    