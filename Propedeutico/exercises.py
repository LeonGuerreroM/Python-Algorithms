import timeit

def centigrados_a_f(grados):
    return 32 + 9*grados/5

def kmh_a_ms(kh):
    return kh / 3.6

def partir_entero(entero):
    return entero // 100, (entero % 100) // 10 , entero % 10

def divisores_propios(numero):
    divisores = []
    for i in range(1, numero//2+1):
        if numero%i == 0:
            divisores.append(i)
    return divisores

def numeros_perfectos(limite):
    perfectos = []
    for i in range(1, limite+1):
        divisores = divisores_propios(i)
        if sum(divisores) == i:
            perfectos.append(i)
    return perfectos

def num_palabras_en_frase(frase):
    palabras_separadas = frase.split(" ")
    return len(palabras_separadas)

def division_con_restas_recursivo(dividendo, divisor, cociente=0):
    resultado = dividendo - divisor
    if resultado < 0:
        return cociente
    cociente += 1
    return division_con_restas_recursivo(resultado, divisor, cociente)

def division_con_restas_iterativo(dividendo, divisor):
    cociente = 0
    while dividendo >= divisor:
        dividendo = dividendo - divisor
        cociente += 1
    return cociente

def decimal_a_binario(decimal):
    binario = ""
    while(decimal>0):
        binario = str(decimal%2) + binario
        decimal = decimal // 2
    return binario

def decimal_binario_recursivo(decimal):
    if decimal == 1:
        return 1
    return str(decimal_binario_recursivo(decimal // 2)) + str(decimal % 2)

def residuo_recursivo(dividendo, divisor):
    if dividendo - divisor < 0:
        return dividendo
    return residuo_recursivo(dividendo - divisor, divisor)

if __name__ == '__main__':
    # grados = float(input('Ingrese la cantidad de grados centigrados '))
    # f = centigrados_a_f(grados)
    # print(f)

    # grados = float(input('Ingrese la velocidad en km/h '))
    # ms = kmh_a_ms(grados)
    # print(ms)

    # numero = int(input('Ingrese un número de 3 cifras '))
    # cifras = partir_entero(numero)
    # print(cifras)

    # limite = int(input('Ingrese un limite '))
    # ini = timeit.timeit()
    # perfectos = numeros_perfectos(limite)
    # fin = timeit.timeit()
    # print(perfectos)
    # print((fin-ini)/1e9)

    # frase = input('Ingresa la palabra')
    # palabras = num_palabras_en_frase(frase)
    # print(palabras)

    #print(division_con_restas_recursivo(353252, 2131));
    #print(decimal_binario_recursivo(10892))
    
    print(residuo_recursivo(213132,1291))
    
    print(213132%1291)
    
x = [1,3,4]
print(x*2)