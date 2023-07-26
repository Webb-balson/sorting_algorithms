items = [23,45,6,87,17,11]

for i in range(1, len(items)):
    key = items[i]

    j = i-1
    while j>=0 and key < items[j]:
        items[j+1] = items[j]
        j = j-1

    items[j+1] = key

print(("Sorted List - ", items))