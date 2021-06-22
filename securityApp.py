# Ser crea modulo que controla la seguridad de la APP

#validacion codigo de ingreso a la plataforma si tiene alguno de los parametros errados devolvera falso
def ValidacionCodigo(CodigoAutorizacion):
    if ((len(CodigoAutorizacion)) == 8) and (CodigoAutorizacion[2] == '*') and (CodigoAutorizacion[0] == CodigoAutorizacion[7]) and (not('@' in CodigoAutorizacion))  and (not('+' in CodigoAutorizacion)) and (not('=' in CodigoAutorizacion)) and (not('&' in CodigoAutorizacion)):
        print('El codigo es Correcto! puede registrar la factura')
        return True
    else:
        print('Valide su codigo de empleado! El ingresado no cumple con las caracteristicas')
        return False