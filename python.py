

tall1 = 10
tall2 = 5

sum = tall1 + tall2
produkt = tall1 * tall2

print(sum)


print(produkt)

navn = input("Hva heter du? ")

print("Hei", navn)


bosted = input("Hvor bor du? ")

print("Hei", navn, "du bor i", bosted)

alder = int(input("Hvor gammel er du? "))

print("Om fem år er du", alder + 5)
alder = int(input("Hvor gammel er du? "))

print("Om 5 år er du", alder + 5, "år")
print("Om 10 år er du", alder + 10, "år")
print("Om 20 år er du", alder + 20, "år")
alder = int(input("Hvor gammel er du? "))
aar = int(input("Hvor mange år fram i tid? "))

print("Om", aar, "år er du", alder + aar, "år")

tall1 = int(input("Skriv inn første tall: "))
tall2 = int(input("Skriv inn andre tall: "))

sum = tall1 + tall2

print("Summen er", sum)
tall1 = float(input("Skriv inn første tall: "))
tall2 = float(input("Skriv inn andre tall: "))

tall1 = float(input("Skriv inn første tall: "))
tall2 = float(input("Skriv inn andre tall: "))

omaresum = tall1 + tall2
differanse = tall1 - tall2
produkt = tall1 * tall2
gjennomsnitt = (tall1 + tall2) / 2

print("Summen er", sum)
print("Differansen er", differanse)
print("Produktet er", produkt)
print("Gjennomsnittet er", gjennomsnitt)

alder = int(input("Alder: "))

if alder >= 18:
    print("Du er myndig")
else:
    print("Du er ikke myndig")

    alder = int(input("Alder: "))

if alder < 13:
    print("Du er et barn")
elif alder < 18:
    print("Du er ungdom")
else:
    print("Du er voksen")

    tall = int(input("Skriv inn et tall: "))

if tall > 0:
    print("Tallet er positivt")
else:
    print("Tallet er ikke positivt")
    tall = int(input("Skriv inn et tall: "))

if tall > 0:
    print("Tallet er positivt")
elif tall < 0:
    print("Tallet er negativt")
else:
    print("Tallet er null")
    alder = int(input("Hvor gammel er du? "))
alder = int(input("Hvor gammel er du? "))

if alder < 6:
    print("Billetten er gratis")
elif alder <= 17:
    print("Billetten koster 50 kr")
elif alder <= 66:
    print("Billetten koster 100 kr")
else:
    print("Billetten koster 50 kr")


start = int(input("Start: "))
stopp = int(input("Stopp: "))
steg = int(input("Steg: "))

sum_tall = 0

for tall in range(start, stopp + 1, steg):
    print(tall)
    sum_tall = sum_tall + tall

print("Summen er", sum_tall)