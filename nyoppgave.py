alder = int(input("Hvor gammel er du? "))

if alder < 6:
    print("Billetten er gratis")
elif alder <= 17:
    print("Billetten koster 50 kr")
elif alder <= 66:
    print("Billetten koster 100 kr")
else:
    print("Billetten koster 50 kr")

    alder = int(input("Hvor gammel er du? "))
student = input("Er du student? (ja/nei): ")

if alder < 6:
    pris = 0
elif alder <= 17:
    pris = 50
elif alder <= 66:
    pris = 100
else:
    pris = 50

if student == "ja":
    pris = pris * 0.80

print("Billetten koster", pris, "kr")