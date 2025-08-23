# Creating an empty list
my_list = []

# Adding the list using appending method
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(f"Original List {my_list}")

# Inserting 15 in the second position
my_list.insert(1,15)
print(f"Inserted List {my_list}")

# Combinnig two lists using extend method
my_list.extend([50, 60, 70])
print(f"Extended List {my_list}")

# Sorting the list in ascending order
my_list.sort()
print(f"Sorted List {my_list}")

# Finding the index of 30: 
index_of_30 = my_list.index(30)
print(f"The index {index_of_30} ")

print(f"The Updated List {my_list}")

