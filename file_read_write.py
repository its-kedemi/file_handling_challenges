try:
    with open("input.txt", "r") as file:
        content = file.read()

    word_count = len(content.split())
    processed_text = content.upper()

    with open("output.txt", "w") as file:
        file.write(processed_text + "\n")
        file.write(f"\nWord Count: {word_count}")

    print("File processing complete! 'output.txt' created successfully.")

except FileNotFoundError:
    print("Error: 'input.txt' does not exist. Please create the file and try again.")
except Exception as e:
    print(f"An error occurred: {e}")
