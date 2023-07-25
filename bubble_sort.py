
items = [75, 34, 88, 12, 7, 55]

for i in range(len(items)):

    swapped = False

    for j in range(0, len(items)-i-1):
        if items[j] > items[j+1]:
            items[j], items[j+1] = items[j+1], items[j]
            swapped = True

    if swapped == False:
        break

print("Sorted list -> ",items)

