import file_manager as fm

# Create a new file
fm.create_file("example.txt", "Hello, this is a test file!")

# Copy file
fm.copy_file("example.txt", "copy_example.txt")

# Move file
fm.move_file("copy_example.txt", "C:/Users/rishi.ss/Desktop/copy_example.txt")

# List files in current directory
fm.list_files(".")

# Delete file
fm.delete_file("example.txt")
