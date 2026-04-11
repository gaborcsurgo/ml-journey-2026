expenses = []

for i in range(5):
    x = int(input("Add meg a kiadást: "))
    expenses.append(x)

total = sum(expenses)
avg = total / len(expenses)

print("Összesen:", total)
print("Átlag:", avg)

if total > 10000:
    print("Sokat költöttél")
    