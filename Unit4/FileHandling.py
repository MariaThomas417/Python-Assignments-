file=open("NewFile.txt","w")
file.write("Name: Maria Thomas")
file.close()
print("File created successfully")

with open("NewFile.txt","r") as file:
    print("File contents")
    content1=file.read()
    print(content1)
    file.close()

Unit5/README.md
with open("NewFile.txt","a") as file:
    print("File contents ")



with open("NewFile.txt","a") as file:
    file.write("Div: SOC15")
    file.close()
    print("Added a line in file")

with open("NewFile.txt","r") as file:
    print("File contents")
    content2=file.read()
    print(content2)
    file.close()
