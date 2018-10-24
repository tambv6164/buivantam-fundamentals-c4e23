star = int(input("Nhap so ngoi sao muon ve: "))
print("*"*star)
print()

star_x = int(input("Tong so x và * muon ve:"))
r = star_x%2
print("x*"*(star_x//2)+"x"*r)
print()

n = int(input("Hang ngang: n = "))
m = int(input("Hang doc: m = "))
print("Ket qua: ")
print()
for i in range(m):
    print("*"*n)