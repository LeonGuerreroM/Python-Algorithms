import math

def calcular_entropia(tabla_frecuencias, longitud_texto):
    probabilidades = [frecuencia_simbolo / longitud_texto for frecuencia_simbolo in tabla_frecuencias.values()]
    entropia = -sum(probabilidad_simbolo * math.log2(probabilidad_simbolo) for probabilidad_simbolo in probabilidades)
    return round(entropia,2)

# Estructura para los nodos del árbol
class Nodo:
    def __init__(self, frecuencia, simbolo=None):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

# Combinación de los nodos
def combinar_nodos(nodo1, nodo2):
    nodo_union = Nodo(nodo1.frecuencia + nodo2.frecuencia)
    nodo_union.izquierda = nodo1
    nodo_union.derecha = nodo2
    return nodo_union

# Obtención de frecuencias de simbolos
def construir_tabla_frecuencias(texto):
    frecuencias = {}
    for simbolo in texto:
        if simbolo not in frecuencias:
            frecuencias[simbolo] = 0
        frecuencias[simbolo] += 1
    return frecuencias

# Función para construir el árbol de Huffman
def crear_arbol(texto):

    tabla_frecuencias = construir_tabla_frecuencias(texto)
    print('entropia', calcular_entropia(tabla_frecuencias, len(texto)))
    # Lista de nodos hoja
    nodos = [Nodo(frecuencia, simbolo) for simbolo, frecuencia in tabla_frecuencias.items()]

    # Construcción del árbol hasta llegar a la raíz
    while len(nodos) > 1:
        nodos = sorted(nodos, key=lambda nodo: nodo.frecuencia)

        # Selección de las menores frecuencias
        nodo1 = nodos.pop(0)
        nodo2 = nodos.pop(0)

        # Combinación de nodos
        nodo_union = combinar_nodos(nodo1, nodo2)
        nodos.append(nodo_union)

    return nodos[0]

# Recorrido del árbol para generar código
def generar_codigos(nodo, prefijo='', codigos={}):
    if nodo is not None:
        if nodo.simbolo is not None: # Nodos hoja
            codigos[nodo.simbolo] = prefijo
        generar_codigos(nodo.izquierda, prefijo + '0', codigos)
        generar_codigos(nodo.derecha, prefijo + '1', codigos)
    return codigos

def calcular_bits_promedio(codigos, texto):
    bits_promedio = 0
    tabla_frecuencias = construir_tabla_frecuencias(texto)
    for simbolo, codigo in codigos.items():
        bits_promedio += (tabla_frecuencias[simbolo] / len(texto) ) * len(codigo)

    return round(bits_promedio,2)

def codificacion_huffman(texto):
    nodo_root = crear_arbol(texto)
    codigos = generar_codigos(nodo_root)
    #print(codigos)
    print('Bits promedio', calcular_bits_promedio(codigos, texto))
    # Codificación del texto
    texto_codificado = ''
    for simbolo in texto:
        texto_codificado += codigos[simbolo]
    return texto_codificado

if __name__ == '__main__':
    #texto = 'MATEMATICAS'

    #texto = 'Se puede reconocer a los maestros antiguos de la pintura por la mancha de su pincel'

    #texto = '...sin volver si quiera la vista atrás, como si temiera que si se volvía una sola vez para mirar lo que dejaba, le fallase su resolución.'

    texto = 'Para ponerse a salvo, en lo posible, de los embates de la fortuna, hay que comportarse como los marineros diestros, que procuran evitar las tempestades pero que, cuando se encuentran con una, no se le enfrentan de proa, sino que se doblegan a ella, adaptando su navegación a sus sinuosidades, y así, obedeciéndola, la vencen. La previsión evita muchas de estas tempestades del azar, pero, cuando pese a todo se producen, hay que ir con los vientos, y de esta manera, lejos de quedar aniquilado, hasta se puede sacar provecho de lo imprevisto.'

    #texto = 'Había empezado a leer la novela unos días antes. La abandonó por negocios urgentes, volvió a abrirla cuando regresaba en tren a la finca; se dejaba interesar lentamente por la trama, por el dibujo de los personajes. Esa tarde, después de escribir una carta a su apoderado y discutir con el mayordomo una cuestión de aparcerías, volvió al libro en la tranquilidad del estudio que miraba hacia el parque de los robles. Arrellanado en su sillón favorito, de espaldas a la puerta que lo hubiera molestado como una irritante posibilidad de intrusiones, dejó que su mano izquierda acariciara una y otra vez el terciopelo verde y se puso a leer los últimos capítulos. Su memoria retenía sin esfuerzo los nombres y las imágenes de los protagonistas; la ilusión novelesca lo ganó casi en seguida. Gozaba del placer casi perverso de irse desgajando línea a línea de lo que lo rodeaba, y sentir a la vez que su cabeza descansaba cómodamente en el terciopelo del alto respaldo, que los cigarrillos seguían al alcance de la mano, que más allá de los ventanales danzaba el aire del atardecer bajo los robles. Palabra a palabra, absorbido por la sórdida disyuntiva de los héroes, dejándose ir hacia las imágenes que se concertaban y adquirían color y movimiento, fue testigo del último encuentro en la cabaña del monte. Primero entraba la mujer, recelosa; ahora llegaba el amante, lastimada la cara por el chicotazo de una rama. Admirablemente restañaba ella la sangre con sus besos, pero él rechazaba las caricias, no había venido para repetir las ceremonias de una pasión secreta, protegida por un mundo de hojas secas y senderos furtivos. El puñal se entibiaba contra su pecho, y debajo latía la libertad agazapada. Un diálogo anhelante corría por las páginas como un arroyo de serpientes, y se sentía que todo estaba decidido desde siempre. Hasta esas caricias que enredaban el cuerpo del amante como queriendo retenerlo y disuadirlo, dibujaban abominablemente la figura de otro cuerpo que era necesario destruir. Nada había sido olvidado: coartadas, azares, posibles errores. A partir de esa hora cada instante tenía su empleo minuciosamente atribuido. El doble repaso despiadado se interrumpía apenas para que una mano acariciara una mejilla. Empezaba a anochecer. Sin mirarse ya, atados rígidamente a la tarea que los esperaba, se separaron en la puerta de la cabaña. Ella debía seguir por la senda que iba al norte. Desde la senda opuesta él se volvió un instante para verla correr con el pelo suelto. Corrió a su vez, parapetándose en los árboles y los setos, hasta distinguir en la bruma malva del crepúsculo la alameda que llevaba a la casa. Los perros no debían ladrar, y no ladraron. El mayordomo no estaría a esa hora, y no estaba. Subió los tres peldaños del porche y entró. Desde la sangre galopando en sus oídos le llegaban las palabras de la mujer: primero una sala azul, después una galería, una escalera alfombrada. En lo alto, dos puertas. Nadie en la primera habitación, nadie en la segunda. La puerta del salón, y entonces el puñal en la mano, la luz de los ventanales, el alto respaldo de un sillón de terciopelo verde, la cabeza del hombre en el sillón leyendo una novela.'

    print('Texto codificado:', codificacion_huffman(texto))
    print(len(texto))
