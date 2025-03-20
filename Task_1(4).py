def read_file(filename):
    print("Reading file content:")

    try:
        with open(filename, 'r') as file:
            for i, line in enumerate(file, start=1):
                print(f"Line {i}: {line.strip()}")  
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")


file_path = r"C:\sample.txt"
read_file(file_path)
