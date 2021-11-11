nama = input("Nama :")
ttl = input("Tempat Tanggal Lahir:")
splitTtl = ttl.split()
splitNama = nama.split()

print("Haloo! ",nama.replace(splitNama[0],''),",",splitNama[0])
print("Anda lahir di",splitTtl[0],"pada tanggal",ttl.replace(splitTtl[0],''))