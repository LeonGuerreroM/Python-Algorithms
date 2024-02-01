
from decimal import Decimal, ROUND_HALF_UP, getcontext

def numero_a_texto(numero):
    """
    Convierte un número a letras.
    
    Param:
        numero: Número a convertir
    Devuelve:
        Número convertido en texto (str).
    Excepción:
        -1 cuando el número es mayor o igual a un sextillón (int).
    
    """
    
    unidades = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis',
                'siete', 'ocho', 'nueve']
    decenas1 = ['diez', 'once', 'doce', 'trece', 'catorce', 'quince',
                'dieciséis', 'diecisiete', 'dieciocho', 'diecinueve']
    decenas2 = ['veinte', 'treinta', 'cuarenta', 'cincuenta', 'sesenta',
                'setenta', 'ochenta', 'noventa']
    centenas = ['ciento', 'doscientos', 'trescientos', 'cuatrocientos',
                'quinientos', 'seiscientos', 'setecientos', 'ochocientos',
                'novecientos']
    singulares = ['un millón', 'un billón', 'un trillón', 'un cuatrillón',
                'un quintillón']
    plurales = ['millones', 'billones', 'trillones', 'cuatrillones',
                'quintillones']
    
    # los dígitos
    if numero < 10:
        return unidades[numero]
    # los números entre 10 y 19
    if numero < 20:
        return decenas1[numero - 10]
    # los números entre 20 y 29
    if numero < 30:
        if numero % 10 == 0:
            return 'veinte'
        else:
            return 'veinti' + unidades[numero % 10]
    # los números entre 30 y 99
    if numero < 100:
        if numero % 10 == 0:
            return decenas2[numero // 10 - 2]
        else:
            return (decenas2[numero // 10 - 2] + ' y '
            + unidades[numero % 10])
    # los números entre 100 y 999
    if numero < 1000:
        if numero == 100:
            return 'cien'
        if numero % 100 == 0:
            return centenas[numero // 100 - 1]
        else:
            return (centenas[numero // 100 - 1] + ' '
            + numero_a_texto(numero % 100))
    # los números entre 1000 y 999999
    if numero < 1000000:
        if numero == 1000:
            return 'un mil'
        if numero < 2000:
            return 'un mil ' + numero_a_texto(numero % 1000)
        if numero % 1000 == 0:
            return numero_a_texto(numero // 1000) + ' mil'
        else:
            return (numero_a_texto(numero // 1000) + ' mil '
            + numero_a_texto(numero % 1000))
    # los números mayores de 999999
    for i in range(0, len(singulares)):
        base = 1000000 ** (i + 1)
        limite = base * 1000000
        if numero < limite:
            if numero == base:
                return singulares[i]
            if numero < 2 * base:
                return singulares[i] + ' ' + numero_a_texto(numero % base)

            if numero % base == 0:
                return numero_a_texto(numero // base) + ' ' + plurales[i]
            else:
                return (numero_a_texto(numero // base) + ' ' + plurales[i]
                + ' ' + numero_a_texto(numero % base))

    return False

def redondeo_preciso(numero):
    """
    Redondea un número mejorando la precision al usar la clase Decimal
    y una precisión de 50.

    Param:
        numero: Número a redondear
    Devuelve:
        Número redondeado (Decimal).

    """
    
    getcontext().prec = 50
    return Decimal(numero).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)

def formatear_cheque(numero):
    """
    Formatea un número para usarlo en un cheque

    Param:
        numero: Número a formatear
    Devuelve:
        Número formateado (str).
    Excepción:
        -1 cuando el número es mayor o igual a un sextillón (int).

    """

    numero = redondeo_preciso(numero)
    entero = int(numero)
    decimal = str(int((numero % 1) * 100))
    entero_texto = numero_a_texto(entero)
    if not entero_texto:
        return entero_texto
    if entero == 1:
        return 'UN PESO ' + decimal + '/100 M.N.'
    return entero_texto.upper() + ' PESOS ' + decimal + '/100 M.N.'


def validador(numero):
    """
    Valida que el número sea un positivo real de tipo entero o decimal
    
    Param:
        numero: Número a validar
    Devuelve:
        Confirmación de validación (bool).
    Excepción:
        False cuando no pasa las validaciones (int).
    
    """
    numero_limite = 1000000000000000000000000000000000000;
    numero_sin_punto = numero.replace('.', '')
    if not numero_sin_punto.isdigit():
        print('Por favor ingrese una cantidad válida.')
        return False
    if redondeo_preciso(numero) >= numero_limite:
        print("La cantidad excede los límites. "
        "Por favor ingrese un número mas pequeño")
        return False
    return True

def funcion_principal():
    """
    Constituye el flujo de ejecución principal
    
    """
    operacion_valida = False
    while(not operacion_valida):
        valor_cheque = input('Ingrese el valor del cheque en números: ')
        es_valido = validador(valor_cheque);
        if not es_valido:
            continue
        texto_cheque = formatear_cheque(valor_cheque)
        if texto_cheque:
            print(texto_cheque)
            operacion_valida = True
    

if __name__ == '__main__':
    funcion_principal()
