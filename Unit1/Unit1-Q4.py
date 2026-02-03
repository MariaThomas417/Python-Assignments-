student = {
    "Name": "Maria",
    "Age": 18,
    "Roll no.": 68
}
print("Dictionary:", student)
print("Name:", student["Name"])
print("Age:", student.get("age"))
print("\nAll keys:", student.keys())
print("All values:", student.values())
student["Div"] = "SOC-15"     
print("\nUpdated Dictionary:", student)
student.pop("Roll no.")       
print("\nAfter removing 'Roll no.':", student)
student.popitem()            
print("After popitem():", student)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}   
print("\nDictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Merged Dictionary:", merged_dict)
