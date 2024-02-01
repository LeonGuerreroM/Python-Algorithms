# Por favor ejecutar antes del código
#   pip install unidecode
# si decide ejecutarlo en entorno local

from unidecode import unidecode

entidades = {
    'AG':'Aguascalientes',
    'BC':'Baja California',
    'BS':'Baja California Sur',
    'CC':'Campeche',
    'CL':'Coahuila',
    'CM':'Colima',
    'CS':'Chiapas',
    'CH':'Chihuahua',
    'DF':'Ciudad de México',
    'DG':'Durango',
    'GT':'Guanajuato',
    'GR':'Guerrero',
    'HG':'Hidalgo',
    'JC':'Jalisco',
    'MC':'México',
    'MN':'Michoacán',
    'MS':'Morelos',
    'NT':'Nayarit',
    'NL':'Nuevo León',
    'OC':'Oaxaca',
    'PL':'Puebla',
    'QT':'Querétaro',
    'QR':'Quintana Roo',
    'SP':'San Luis Potosí',
    'SL':'Sinaloa',
    'SR':'Sonora',
    'TC':'Tabasco',
    'TS':'Tamaulipas',
    'TL':'Tlaxcala',
    'VZ':'Veracruz',
    'YN':'Yucatán',
    'ZS':'Zacatecas'
}

meses = {
    "01": "ENERO",
    "02": "FEBRERO",
    "03": "MARZO",
    "04": "ABRIL",
    "05": "MAYO",
    "06": "JUNIO",
    "07": "JULIO",
    "08": "AGOSTO",
    "09": "SEPTIEMBRE",
    "10": "OCTUBRE",
    "11": "NOVIEMBRE",
    "12": "DICIEMBRE",
}

duracion_meses = {
    "01": 31,
    "02": 28,
    "03": 31,
    "04": 30,
    "05": 31,
    "06": 30,
    "07": 31,
    "08": 31,
    "09": 30,
    "10": 31,
    "11": 30,
    "12": 31
}

palabras_prohibidas = [
    "BUEI", "BUEY",
    "CACA", "CACO", "CAGA", "CAGO",
    "CAKA", "CAKO",
    "COGE", "COJA", "COJE", "COJI", "COJO",
    "CULO",
    "FETO",
    "GUEI", "GUEY",
    "JOTO", "JODE"
    "KACA", "KACO", "KAGA", "KAGO",
    "KOGE", "KOJO",
    "KAKA",
    "MAME", "MAMO",
    "MEAR", "MEAS", "MEON",
    "MION",
    "MOCO", "MULA", "MULO",
    "NACA", "NACO",
    "PEDA", "PEDO", "PENE", "PITO",
    "PIJA", "PUTA", "PUTO",
    "QULO",
    "RATA",
    "RUIN",
    "TETA", "TETO"
]

def bisiesto(anio):
    """
    Calcula si un año es bisiesto
    
    Entradas:
        anio: año a calcular
    Salidas:
        Confirmación o negación de año bisiesto (bool)
    
    """

    anio = int(anio)
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        return True
    return False

def leer_nombres():
    """Lee los nombres"""
    print('¿Cuáles son tus nombres? (Mayúsculas y sin acentos)')
    nombres = input('>>>').upper()
    while not nombres.replace(" ", "").isalpha():
        nombres = input('>>>').upper()
    return unidecode(nombres)

def leer_apellidos():
    """Lee los apellidos"""
    print('¿Cuáles son tus apellidos? (Mayúsculas y sin acentos)')
    primer_apellido = input('Primer apellido: ').upper().replace(" ", "")
    while not primer_apellido.isalpha():
        primer_apellido = input('Primer apellido: ').upper().replace(" ", "")
    segundo_apellido = input('Segundo apellido: ').upper().replace(" ", "")
    while not segundo_apellido.isalpha():
        segundo_apellido = input('Segundo apellido: ').upper().replace(" ", "")
    return unidecode(primer_apellido), unidecode(segundo_apellido)

def leer_anio_nacimiento():
    """Lee el año de nacimiento"""
    anio_minimo = 1900
    anio_maximo = 2023
    print('¿En qué año naciste? (4 dígitos)')
    anio_nacimiento = input('>>>')
    while (not anio_nacimiento.isdigit() or int(anio_nacimiento) < anio_minimo
        or int(anio_nacimiento) > anio_maximo):
        anio_nacimiento = input('>>>')
    return anio_nacimiento

def leer_mes_nacimiento():
    """Lee el mes de nacimiento"""
    print('¿En qué mes naciste? (2 dígitos)')
    for numero, mes in meses.items():
        print(numero + " -> " + mes)
    mes_nacimiento = input('>>>')
    while not mes_nacimiento in meses.keys():
        mes_nacimiento = input('>>>')
    return mes_nacimiento

def leer_dia_nacimiento(anio, mes):
    """Lee el día de nacimiento"""
    maximo_dia = duracion_meses[mes]
    if mes == '02' and bisiesto(anio):
        maximo_dia = 29;
    print('¿En qué día naciste? (2 dígitos)')
    dia_nacimiento = input('>>>')
    while (not dia_nacimiento.isdigit() or len(dia_nacimiento) != 2
    or int(dia_nacimiento) < 1 or int(dia_nacimiento) > maximo_dia):
        dia_nacimiento = input('>>>')
    return dia_nacimiento

def leer_sexo():
    """Lee el sexo"""
    print('¿Cuál es tu sexo? (H/M/X)')
    sexo = input('>>>').upper()
    while sexo not in ['H', 'M', 'X']:
        sexo = input('>>>').upper()
    return sexo

def leer_entidad():
    """Lee la entidad federativa de nacimiento"""
    print("¿En que entidad federativa naciste?\n(2 letras mayúsculas, "
    "por ejemplo: DF; ? para ver la lista de entidades)")
    entidad = input('>>>').upper()
    while entidad not in entidades:
        if entidad == '?':
            for clave, valor in entidades.items():
                print(clave, ':', valor)
            print('')

        entidad = input('>>>').upper()
    return entidad

def leer_datos():
    """Lee los datos del usuario"""
    nombres = leer_nombres()
    primer_apellido, segundo_apellido = leer_apellidos()
    anio_nacimiento = leer_anio_nacimiento()
    mes_nacimiento = leer_mes_nacimiento()
    dia_nacimiento = leer_dia_nacimiento(anio_nacimiento, mes_nacimiento)
    sexo = leer_sexo()
    entidad = leer_entidad()
    return nombres, primer_apellido, segundo_apellido, anio_nacimiento, \
        mes_nacimiento, dia_nacimiento, sexo, entidad

def siguiente_vocal(palabra):
    """Busca la primera vocal de una palabra"""
    for letra in palabra:
        if letra in ['A', 'E', 'I', 'O', 'U']:
            return letra
    return 'X'

def siguiente_consonante(palabra):
    """Busca la primera consonante de una palabra"""
    for letra in palabra:
        if letra not in ['A', 'E', 'I', 'O', 'U']:
            return letra
    return 'X'

def calcular_inicio_nombre(nombres):
    """
    Calcula en qué indice comienza a tomar las letras del nombre considerando
    que pueda llamarse José o María y tener un segundo nombre

    Entradas:
        nombres: Nombres de la persona
    Salida:
        indice donde comenzar a tomar las letras del nombre para la CURP

    """

    if nombres[0:5] == "JOSE " and len(nombres) > 4:
        return 5
    if nombres[0:6] == "MARIA " and len(nombres) > 5:
        return 6
    return 0

def curp_parte_1(primer_apellido, segundo_apellido, nombres):
    """Calcula la primera parte de la CURP"""
    inicio_nombre = calcular_inicio_nombre(nombres)
    curp = (primer_apellido[0:1] + siguiente_vocal(primer_apellido[1:]) +
            segundo_apellido[0:1] + nombres[inicio_nombre:inicio_nombre+1] )
    return curp

def curp_parte_2(anio_nacimiento, mes_nacimiento, dia_nacimiento):
    """Calcula la segunda parte de la CURP"""
    curp = anio_nacimiento[2:4] + mes_nacimiento + dia_nacimiento
    return curp

def curp_parte_5(primer_apellido, segundo_apellido, nombres):
    """Calcula la quinta parte de la CURP"""
    inicio_nombre = calcular_inicio_nombre(nombres) + 1
    curp = siguiente_consonante(primer_apellido[2:]) + \
        siguiente_consonante(segundo_apellido[1:]) + \
        siguiente_consonante(nombres[inicio_nombre:])
    return curp


def curp(nombres, primer_apellido, segundo_apellido, anio_nacimiento, \
    mes_nacimiento, dia_nacimiento, sexo, entidad):
    """Calcula la CURP"""

    curp_parte_1_resultado = curp_parte_1(primer_apellido, segundo_apellido, nombres)
    if curp_parte_1_resultado in palabras_prohibidas:
        curp_parte_1_resultado = curp_parte_1_resultado[0:3] + "X"
    curp = curp_parte_1_resultado + \
        curp_parte_2(anio_nacimiento, mes_nacimiento, dia_nacimiento) + \
        sexo + entidad + \
        curp_parte_5(primer_apellido, segundo_apellido, nombres) + 'XX'
    return curp

if __name__ == "__main__":
    curp_resultado = curp(*leer_datos())
    print('TU CURP => ' + curp_resultado)