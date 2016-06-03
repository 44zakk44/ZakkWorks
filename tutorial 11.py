numberstaken = [2, 5, 12, 33, 17]

print("here are the numbers that are still available")

for n in range(1, 20):
    if n in numberstaken:
        continue
    print(n)