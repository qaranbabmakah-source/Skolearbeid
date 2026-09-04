start = int(input("Start: "))
stopp = int(input("Stopp: "))
steg = int(input("Steg: "))

sum_tall = 0

for tall in range(start, stopp + 1, steg):
    print(tall)
    sum_tall = sum_tall + tall

print("Summen er", sum_tall)





