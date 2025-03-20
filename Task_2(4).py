def write_and_append_to_file(filename):

    user_input = input("Enter text to write to the file: ")

    
    with open(filename, 'w') as file:
        file.write(user_input + "\n")
        print("Data successfully written to output.txt")

    
    additional_data = input("Enter additional text to append: ")
    with open(filename, 'a') as file:
        file.write(additional_data + "\n")
    print("Data successfully appended.")

    
    print("\nFinal content of output.txt:")
    with open(filename, 'r') as file:
        print(file.read())


write_and_append_to_file("output.txt")
