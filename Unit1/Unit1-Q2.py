
set1 = {10,20,30,40,50}
set2 = {60,70,80,90,100}
print("Set 1:", set1)
print("Set 2:", set2)
print("\nAccessing elements of Set 1:")
for element in set1:
    print(element)
union_set = set1.union(set2)
print("\nUnion of Set1 and Set2:", union_set)
intersection_set = set1.intersection(set2)
print("Intersection of Set1 and Set2:", intersection_set)
difference_set1 = set1.difference(set2)
difference_set2 = set2.difference(set1)
print("Difference (Set1 - Set2):", difference_set1)
print("Difference (Set2 - Set1):", difference_set2)
