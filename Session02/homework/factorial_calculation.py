from math import *
n = int(input("Nhap n = "))
if n <= 0:
    print("Vui long nhap mot so nguyen duong")
else:
    f = factorial(n)
    print("Tich cac so tu nhien lien tiep tu 1 den", n, "la:", f)