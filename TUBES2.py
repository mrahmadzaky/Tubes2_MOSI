import random
from random import choices
### ~~~~~ Menyiapkan Variabel ~~~~~ ###
jum_indiv = 200
infected = jum_indiv * 5/100
waktu_pemulihan = 9
x_max,y_max = 20,20
x_min,y_min = 0,0
probability = 0.8
total_pemulihan_komunitas = 1
posx,posy = [],[]
posxInfected,posyInfected = [],[]
kesehatan = []
imunitas = []
infectedtime = []

### ~~~~~ Data 200 Individu ~~~~~ ###
virus = 0
i = 0
while virus <infected or i<jum_indiv:
    x = random.randint(x_min,x_max)
    y = random.randint(y_min,y_max)
    posx.append(x)
    posy.append(y)
    if virus <= 9:
        kesehatan.append("terinfeksi")
        imunitas.append("belum_imun")
        infectedtime.append(1)
        virus+=1
    else:
        kesehatan.append("belum_terinfeksi")
        imunitas.append("belum_imun")
        infectedtime.append(0)
    i+=1
### Mencatat titik koordinat yang terinfeksi ###
for i in range(jum_indiv):
    if kesehatan[i] == "terinfeksi":
        posxInfected.append(posx[i])
        posyInfected.append(posy[i])

def PBCx(x):
    if x > x_max:
        x += -x_max
    if x < x_min:
        x += +x_max
    return x

def PBCy(y):
    if y > y_max:
        y += -y_max
    if y < y_min:
        y += +y_max
    return y

totalinfected = virus
totalsembuh = 0
while totalsembuh != totalinfected:
    for i in range(jum_indiv):
        x = [0,1]
        weights = [probability,.2]
        b = random.choices(x,weights)
        if b[0] == 0: #Jika individu bergerak
            nilai = random.uniform(0,1)
            if nilai <= 0.25:
                posx[i]=posx[i]+1
                posx[i]=PBCx(posx[i])
            elif nilai <= 0.50:
                posy[i]=posy[i]-1
                posy[i]=PBCy(posx[y])
            elif nilai <= 0.75:
                posx[i]=posx[i]-1
                posx[i]=PBCx(posx[i])
            else:
                posy[i]=posy[i]+1
                posy[i]=PBCy(posx[y])
        if kesehatan[i] == "terinfeksi":
            infectedtime[i] = infectedtime[i]+1
            total_pemulihan_komunitas = total_pemulihan_komunitas + 1
            if infectedtime[i] >= waktu_pemulihan:
                kesehatan[i] = "pulih"
                imunitas[i] = "kuat"
                if not posxInfected:
                    print("abis")
                else:
                    posxInfected.pop(0)
                    posyInfected.pop(0)
        for j in range(len(posxInfected)):
            if posx[i]==posxInfected[j] and posy[i]==posyInfected[j]:
                if totalinfected < jum_indiv and kesehatan[i] == "belum_terinfeksi":
                    kesehatan[i] = "terinfeksi"
                    totalinfected = totalinfected + 1
                    posxInfected.append(posx[i])
                    posyInfected.append(posy[i])
    totalsembuh = totalsembuh + 1
print("Total Sembuh              :",totalsembuh)
print("Total Infected            :",totalinfected)
print("Total Pemulihan Komunitas :",total_pemulihan_komunitas,"Hari")
