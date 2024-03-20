bilangan=int(input("masukan bilangan yang ingin dikonversi :\t"))

konversi1=bin(bilangan)[2:]

konversi2=hex(bilangan)

konversi3=oct(bilangan)

print("Bilangan Biner \t\t: ", konversi1.zfill(8))

print("Bilangan Hexadecimal \t: ", konversi2)

print("Bilangan Octal \t\t: ", konversi3)