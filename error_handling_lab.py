# Ask the user for a filename and handle errors if it can't be read

filename = input("Enter the filename you want to read: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile content:\n")
        print(content)

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied to read '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

