# Python program for implementation of selection sort

items = [35, 12, 7, 7, 23, 88]

# Traverse through all the items
for i in range(len(items)):
	# Find the minimum item in the list
	min_idx = i
	for j in range(i+1, len(items)):
		if items[min_idx] > items[j]:
			min_idx = j
			
	# Swap the found minimum element with first item
	items[i], items[min_idx] = items[min_idx], items[i]
	
	
# Print the sorted test
print("Sorted Array:-")
for i in range(len(items)):
	print("%d" %items[i], end=" ")
