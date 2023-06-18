#Osztaly adatbekeres
class Auto:
    def __init__(self, sor:str):
        adatok = sor.strip().split(';')
        self.tipus = adatok[0]
        self.ev = int(adatok[1])
        self.utas = adatok[2]
        self.motortipus = adatok[3]
        self.utazosebesseg = int(adatok[4])
        self.vegsebesseg = int(adatok[5])
        self.hosszusag = float(adatok[6].replace(',','.'))
        #A listaba a megfelelo kategoriat rako metodus
        self.sebessegKategoria = ''
        if (self.utazosebesseg<500): self.sebessegKategoria='Alacsony sebességű'
        elif (self.utazosebesseg<1000): self.sebessegKategoria='Normál'
        elif (self.utazosebesseg<1200): self.sebessegKategoria='Gyors'
        else: self.sebessegKategoria = 'Szuperszonikus'

autok:list[Auto] = []


#Fajlbeolvasas
file = open('valami.txt', 'r', encoding='UTF-8')
file.readline() #opcionalis
for sor in file:
    autok.append(Auto(sor))
file.close()


#Elemszam/Darabszam
print(len(autok))


#Adott tipus darabszamainak kiirasa
adottTipusDB = 0
for item in autok:
    if item.tipus.__contains__('tipus_neve'): adottTipusDB +=1

print(adottTipusDB)


#Maximalis "utas"szam keresese (pl.: 134-345)

maxUtasPoz = 0
maxUtas = 0

for i in range(len(autok)):
    utasszam = int(autok[i].utas.split('-')[-1])
    if utasszam > maxUtas:
        maxUtas = utasszam
        maxUtasPoz = i

print('A legtöbb utast szallito tipus')
print(f'\tTipus: {autok[maxUtasPoz].tipus}')


#Statisztikaval meghatarozzuk melyik tipus nincs a listaban
    #Hozzaadjuk az osszes lehetoseget
stat = {"Alacsony sebességű":0,
        "Normál":0,
        "Gyors":0,
        "Szuperszonikus":0}

#Egy 'for' ciklussal megnoveljuk az egyes ertekek darabszamat a statisztikaban
for item in autok:
    if item.sebessegKategoria in stat.keys():
        stat[item]+=1

#Kiirjuk azokat a tipusokat ami nincs a listaban (ismet 'for' ciklussal)
db = 0
for key, value in stat.items():
    if value == 0:
        print(f'{key}', end=' ')
        db+=1
#Ha mindenbol talalhato ezt irjuk ki
if db == 0:
    print('Minden kategoriabol van auto.')

#-----------------------------------------------------------------------------------------------

#Kivetelkezeles
def terulet(a,b):
    ter = a*b
    if ter <100:
        raise ValueError('Hiba: Túl kicsi a telek!')
    return ter

print('2. feladat: Terület számítása')

while True:
    a = float(input('Kérem adja meg a telek szélességét (a): '))
    if a == -1:
        break
    b = float(input('Kérem adja meg a telek hosszúságát (b): '))
    if b == -1:
        break
    try:
        print(f'Telek területe: {terulet(a,b)} nm')
    except ValueError as error:
        print(error)



#------------------------------------------------------------------------------------------------
#osszegzes: mennyi a listaban levo szamok osszege

def osszeg():
    osszeg = 0
    for item in szamok:
        osszeg+item
    return osszeg

#megszamlalas: szamoljuk meg, hany paratlan szam van a listaban

def paratlanDarab():
    darab = 0
    for item in szamok:
        if item %2 == 1:
            darab += 1
    return darab

#Eldontes: benne van-e a szamok kozott a parameterben kapott szam (IGAZ vagy HAMIS)

def eldontes(szam):
    for item in szamok:
        if item==szam:
            return True
    return False

def eldontes_klasszikus(szam):
    i = 0
    while i<len(szamok) and szamok[i] !=szam:
        i+=1
        #ha az i = elemszam akkor nincs benne
        #ha az i< elemszam akkor megtalaltuk es az i megallt ahol megtalaltuk
    if i==len(szamok):
        return False
    else:
        return True

#Kereses: a keresett ertek elso elofordulasanak poziciojat adja vissza

def kereses(keresett):
    for index, ertek in enumerate(szamok):
        if keresett==ertek:
            return index
    return -1

#szelsoertek (maximum) kivalasztas: a legnagyobb elem meghatarozasa

def legnagyobb():
    max = szamok[0]
    maxIndex = 0
    for i in range(1, len(szamok)):
        if szamok[i] >max:
            max = szamok[i]
            maxIndex = i
    return  maxIndex

def legnagyobb2():
    maxIndex = 0
    for i in range(1,len(szamok)):
        if szamok[i]>max:
            maxIndex = i
    return maxIndex

def legnagyobb3():
    maxIndex = 0
    for index, ertek in enumerate(szamok):
        if ertek>szamok[maxIndex]:
            maxIndex = index
    return maxIndex

#szelsoertek (minimum)

def legkisebb():
    min = szamok[0]
    minIndex = 0
    for i in range(1, len(szamok)):
        if szamok[i]<min:
            min = szamok[i]
            minIndex = i
    return minIndex

#---------------------------------------------------------------------------------------------
#Abszolut ertek meghatarozasa (manualis modon)


def abszolut(number):
    if number < 0:
        number = number*-1
    return number


print("Kerem adjon meg egy egesz szamot!")

szam = int(input("szam = "))

# if szam < 0:
#     szam = szam*-1

szam = abszolut(szam)

print(f"A szam abszolut erteke: {szam}")

#Szazalekszamitas (hanyan mennek at az alapvizsgan)

def atmentTanuloSzazaleka(osszesTanuloDB,bukottTanuloDB):
    szazalek = (1-bukottTanuloDB/osszesTanuloDB)*100
    return szazalek

osszes = int(input("Osszes tanulok szama:"))
bukott = int(input("Bukott tanulok szama:"))
szazalek = atmentTanuloSzazaleka(osszes,bukott)

if szazalek<0:
    print('Hibas adatok.')

else:
    print(f'A tanulok {szazalek} %-a ment at a vizsgan')

#legkisebb terulet
minPoz = 0
for i in range(1,len(teruletek)):
    if teruletek[i] < teruletek[minPoz]:
        minPoz = i

print(f'A legkisebb teruletu orszag(ok):')
for i in range(len(teruletek)):
    if teruletek[i] == minPoz:
        print(f'{orszagok[i]} , terulete: {teruletek[i]}')

# x km-nel nagyobb teruletu orszagok szama

darab = 0

for item in teruletek:
    if item >200:
        darab = darab +1

print(darab)

# az orszagok teruletenek atlaga

osszeg = 0
for item in teruletek:
    osszeg += item

print(f'Atlagos orszagmeret {osszeg/len(teruletek)}')

#bekert orszag terulete

bekertOrszag = input('Kerek egy orszagot:')
i = 0

while i < len(orszagok) and orszagok[i] != bekertOrszag:
    i +=1
if i < len(orszagok):
    print(f'\tAz orszag terulete: {teruletek[i]}')
else:
    print('A keresett orszag nincs benne a listaban.')


#----------------------------------------------------------------------

#Bmi-ertek (egyszeru osztas, szorzas, feltetelek)

testsuly = int(input('Kérem a súlyt kilogrammban: '))
testmagassag = int(input('Kérem a magasságot cm-ben: '))

testmagassagMeter = testmagassag/100
testmagassagNegyzet = testmagassagMeter*testmagassagMeter
tti = testsuly/testmagassagNegyzet

print(f'A testtömeg indexe: {tti:.2f}')

if tti < 16:
    print('A testsúly osztálya: súlyos soványság')
elif tti >=16 and tti <=18.49:
    print('A testsúly osztálya: soványság')
elif tti >= 18.5 and tti <= 24.99:
    print('A testsúly osztálya: normális')
elif tti >= 25 and tti <= 29.99:
    print('A testsúly osztálya: túlsúlyos')
elif tti >=30:
    print('A testsúly osztálya: elhízás')

#Egy bekert mondatot megfordit
def mondatfordito(mondat:str):
    szavak = mondat.split(' ')
    ujmondat = ''
    for szo in szavak:
        ujszo = szo[::-1]
        ujmondat+= ujszo+' '
    return ujmondat

bekertmondat = ''
while bekertmondat != 'VÉGE':
    bekertmondat = str(input('Kérek egy szöveget: '))
    if bekertmondat != 'VÉGE':
        print(f'A szöveg visszafele: {mondatfordito(bekertmondat)}')

#Percet szamol at orara (Film hossza)
def óraperc(perc):
    óra = perc//60
    perc = perc-óra*60
    
    return str(óra) + ' óra ' + str(perc) + ' perc'

for i in range(3):
    filmcim = input('Add meg egy film címét! ')
    filmhossz = int(input('Hány perces a film? '))
    print(f'A(z) {filmcim} című film {óraperc(filmhossz)} hosszú')


#Legnagyobb kozos oszto
def lnko(a,b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

print('LNKO kivonásos algoritmussal')

a = int(input('a = '))
b = int(input(' b = '))
print(f'LNKO {a}, {b} = {lnko(a,b)}')


#Legtobb maganhangzo (A het napjaiban)
def mghSzama(szo):
    db = 0
    for i in szo:
        if i in mgh:
            db +=1
    return



napok = ['hétfő', 'kedd', 'szerda', 'csütörtök','péntek']
mgh = 'aöüóeuioőúaéáűí'

maxPoz = 0
for i in range(len(napok)):
    if mghSzama(napok[i]) > mghSzama(napok[maxPoz]):
        maxPoz = i
    
print(f'A legtöbb mgh a {napok[maxPoz]} -ben van!')

#ciklusok ellinput


#Ellenőrzött bekérés

""" szam = 0        #rossz ertek kell kezdonek
while szam < 1 or szam > 100:
    szam = int(input('Kerem adjon meg egy szamot 1 es 100 kozott:'))
print('Koszonom')


#Szamok kiirasa intervallumon

i = 1 
while i <= 100:
    print(i, end="; ")
    i+=1
 """
#-------------------------------------------------------
#véletlen szám generálása

""" from random import randint  #random generáláshoz elengedhetetlen

#addig dobaljuk a kockakat, amig mind a 2 nem lesz 6-os

print(f'\n\n Kockadobasok:')

elso_dobas = randint(1,6)
masodik_dobas = randint(1,6)

while elso_dobas != 6 or masodik_dobas != 6:
    print(f'{elso_dobas}, {masodik_dobas}')
    elso_dobas = randint(1,6)
    masodik_dobas = randint(1,6)

print('Mindket kockaval 6-ost dobtal, VEGE.') """


#legkisebb kozos tobbszoros es legnagyobb kozos oszto

from ast import withitem


def lkkt(a,b):
    if a > b:
        nsz = a
        ksz = b
    else:
        nsz = b
        ksz = a
    osztando = nsz
    while osztando% ksz!=0:
        osztando+=nsz

    return osztando

def lnko(a,b):
        while a!=b:
            if a > b:
                a-=b
            else:
                b-=a
        return a

print('Legkisebb kozos tobbszoros es legnagyobb kozos oszto meghatarozasa')

elso_szam = int(input('a: '))
masodik_szam = int(input('b: '))
print(f'A ket szam legkisebb kozos tobbszorose: {lkkt(elso_szam , masodik_szam)}')
print(f'A ket szam legnagyobb kozos osztoja: {lnko(elso_szam , masodik_szam)}')

#primszamok meghatarozasa

from operator import truediv
from xml.dom.minidom import Element


import math

def prim(szam):
    for i in range(2,int(math.sqrt(szam))+1):
        if szam % i==0:
            return False
    return True


print('Primszam vizsgalat')
szam = int(input('\n Kerek egy szamot: '))



if prim(szam):
    print('A megadott szam primszam')
else:
    print(' megadott szam nem primszam')

#Faktorialis szamitasa

print('Faktorialis:')

n = int(input('\nn: '))

faktorialis = 1

i = n

while i > 0:
    faktorialis*= i 
    i -=1

print(f'{n}! = {faktorialis}')

#for ciklus


""" for i in range(6):
    print(i) """

    
""" for i in range(2 ,10):
    print(i) """


for i in range(10):
    print('Teszt')


#For ciklus teljes bejarasra (pl.: string, ista, stb.)

for item in 'alma':
    print(item , end=' ')

print('\n\n')

gyumolcsok = ['alma' , 'korte' , 'barack' , 'dinnye' , 'cseresznye']

for item in gyumolcsok:
    print(item)

for i in range(1,4):
    print(gyumolcsok[i])

#Fibonacci szamsor
from distutils.command.sdist import sdist
from re import S
from this import d


elozo = 1                 #n-1
elozo_elotti = 0         #n-2

print(elozo_elotti , elozo , end=' ')

for i in range(2,40):
    osszeg = elozo + elozo_elotti
    print(osszeg , end=' ')
    elozo_elotti = elozo
    elozo = osszeg


#50 elso prim
import math

def prim(szam):
    for i in range(2 , int(math.sqrt(szam))+1):
        if szam%i==0:
           return False
        return True

db = 0
szam = 2

while db<50:
    if prim(szam):
        print(szam , end=' ')
        db += 1
    szam += 1


#Tokeletes szam
def tokeletes(tol, ig):
    szamok = []
    for num in range(tol, ig):
        Sum = 0
        for i in range(1, num):
            if num % i == 0:
                Sum = Sum +i
        if Sum == num:
            szamok.append(num)
    return szamok

print('2. feladat: Tökéletes számok')
print('Kérek két természetes számot:')
tol = int(input('tól = '))
ig = int(input('ig = '))
print(f'Tökéletes számok {tol} és {ig} között:')
if len(tokeletes(tol, ig)) == 0:
    print('A megadott tartományban nincsen tökéletes szám!')
else:
    print(tokeletes(tol, ig))

#Háromszög megszerheszthető-e?
print('1. feladat: A háromszög szerkeszthetősége')
print('Kérem a háromszög oldalait!')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a+b > c and a+c > b and b+c > a:
    print('A háromszög megszerkeszthető')
else:
    print('A háromszög nem szerkeszthető a megadott adatokkal!')

