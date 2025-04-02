t = [ 3, 8, 6, 4, 5, 1, 6]
#összegzés tétel
osszeg = 0
# i kettesével lépkedjünk
for i in range (2, len(t), 3): #t-ből kiveszi az értékeket sorban (az i változó értéke minden egyes ciklusban legyen az egyik elem a listából) Behelyettesíti a számokat a listából
    osszeg += t[i] # += ---> append-et jelenti #páros indexű elemek összege
print(osszeg)


t = [ 3, 8, 2, 4, 5, 1, 4]
#összegzés tétel
osszeg = 0
for szam in (t): #t-ből kiveszi az értékeket sorban (az i változó értéke minden egyes ciklusban legyen az egyik elem a listából) Behelyettesíti a számokat a listából
    osszeg += szam # += ---> append-et jelenti
print(osszeg)














