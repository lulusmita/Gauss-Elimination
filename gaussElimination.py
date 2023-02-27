# Nama File: gaussElimination
# Pembuat: Lulus Dwiyan Mita 24060121120029
# Deskripsi: Program untuk gauss elimination 
# Tanggal: 23 Oktober 2022

## module gaussElimin
""" x = gaussElimin(a,b).
Solves [a]{b} = {x} by Gauss elimination.
"""
import numpy as np
def gaussElimin(a,b):
  n = len(b)
  # Elimination Phase
  for k in range(0,n-1):
    for i in range(k+1,n):
      if a[i,k] != 0.0:
        lam = a [i,k]/a[k,k]
        a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
        b[i] = b[i] - lam*b[k]
  # Back substitution
  for k in range(n-1,-1,-1):
    b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
  return b

a = np.zeros(0)
# masukkan matrix koefisien
for i in range (9):
  bufferX = float(input("Masukan a: "))
  a = np.append(a,bufferX)
  
b = np.zeros(0)
for i in range (3):
  bufferX = float(input("Masukan b: "))
  b = np.append(b,bufferX)
  

a = a.reshape(3,3)
print(a)
print(b)

# Sistem persamaan linier yang akan diselesaikan
# a = np.array([[3,-0.1,-0.2],[0.1,7,-0.3],[0.3,-0.2,10]])
# b = np.array([7.85,-19.3,71.4])

# eliminasi gauss
print("\nHasil Gauss Elimination")
gaussElimin(a,b)
