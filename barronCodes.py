def euclides(a,b):
    if a%b == 0:
        return b
    else:
        return euclides(b, a%b)

print(euclides(18,12))
print(euclides(12,8))

def phi(n):
    relativesAmount = 0
    for m in range(1,n):
        if euclides(n,m) == 1:
            relativesAmount += 1
    return relativesAmount

print(phi(12))

# Llamadas de derecha a izq y calculos de izq a derecha
def euclidex(a,b):
    if a%b == 0:
        return 0,1,b
    else:
        A, B, r = euclidex(b, a%b)
        return B,A-(a//b)*B,r

print(euclidex(18,12))

# Calculo de derecha a izquierda
def euclidex1(a,b):
    Q = a // b
    A = 0
    B = 1
    C = 1
    D = -Q
    while a%b!=0:
        bx=b
        b=a%b
        a=bx
        Q=a//b
        Ax=C
        Bx=D
        C=A-Q*C
        D=B-Q*D
        A=Ax
        B=Bx
    return A,B,b

print(euclidex1(18,12))

from math import sqrt
print((1 + sqrt(5))/2)

def pa(n):
    if n == 0:
        return 1
    else:
        return 1 + 1/pa(n-1)
print(pa(8))

def ra():
    if n == 0:
        return 2
    else:
        return 1/(2+ra(n-1))

def r2(n):
    return 1+ra(n)

import math
def criba(n):
  a = []
  for i in range(n):
    a = a + [i]
  ap = []
  i=2;imax=math.sqrt(n)
  while i < imax:
    k = 2
    while k*a[i] < n:
      a[k*a[i]] = 0
      k = k +1
    i = i + 1
    while a[i] == 0:
      i = i + 1
  for j in range(2,n):
    if a[j] != 0:
      ap = ap + [a[j]]
  return ap

p = criba(100)
#print(p)
def facp(n):
  e = []
  if n == 1:
    return 0;
  i = 0
  while n != 1:
    k = 0
    while n%p[i] == 0:
      k = k + 1
      n = n // p[i]
    e = e+[k]
    i = i + 1
  return e

def number(e):
  n = len(e)
  m = 1
  for i in range(n):
    m = m * (p[i]**e[i])
  return m

print(facp(8))
print(facp(12))
print(facp(18500))


def corbaseb(n, b):
    if n < b:
        return [n]
    return [n%b] + corbaseb(n//b, b)

def horner(a, x):
  if a == []:
    return 0
  return horner(a[1:], x)*x + a[0]

# print(corbaseb(11,3))
# print(horner([2, 0, 1], 3))
# print(corbaseb(30,2))
# print(horner([0, 1, 1, 1, 1], 2))

def residuo(b,x,r):
  l = []
  a = corbaseb(x,2)
  n = len(a)
  for i in range(n):
    c = b%r
    l = l + [c]
    b = c * c
  s = 1
  for i in range(n):
    if a[i] == 1:
      s = s*l[i]
      s = s%r
  return s,l

print(residuo(13,11,17))
from math import log, ceil
print(ceil(log(8, 2)))