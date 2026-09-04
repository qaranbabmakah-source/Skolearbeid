for tall in range(1, 11):
    print(tall)
for tall in range(10, 0, -1):
    print(tall)
for tall in range(0, 21, 2):
    print(tall)

tall = int(input("Hvilken gangetabell? "))
slutt = int(input("Hvor langt skal tabellen gå? "))

for i in range(1, slutt + 1):
    print(tall, "x", i, "=", tall * i)


sum_tall = 0
for tall in range(1, 101):
    sum_tall = sum_tall + tall

print(sum_tall)