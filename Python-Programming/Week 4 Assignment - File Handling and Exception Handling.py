def modify_content(content):
    # Example modification: reverse each line
    return [line[::-1] for line in content]

def main():
    filename = input("Enter the filename to read from: ")
    
    try:
        # Try reading the file
        with open(filename, "r") as file:
            lines = file.readlines()
        
        # Modify the content
        modified_lines = modify_content(lines)

        # Create the new filename
        new_filename = f"modified_{filename}"
        
        # Write to the new file
        with open(new_filename, "w") as new_file:
            new_file.writelines(modified_lines)
        
        print(f"Success! Modified content written to '{new_filename}'")

    except FileNotFoundError:
        print("Error: The file was not found.")
    except IOError:
        print("Error: Could not read the file.")

if __name__ == "__main__":
    main()
