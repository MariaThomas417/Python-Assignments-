

filename = input("Enter the filename to open: ")

try:
    file = open(filename, "r")
    print("\nFile opened successfully!\n")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("Error: The file does not exist. Please check the filename.")

except PermissionError:
    print("Error: You don't have permission to read this file.")

except Exception as e:
    print("Unexpected error:", e)