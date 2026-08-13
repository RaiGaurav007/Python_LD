NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20,21,24,27]

i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i+=1

for name in NAMES:
    print(name)

for name, age in zip(NAMES, AGES):
    print(f"{name} {age}")
    