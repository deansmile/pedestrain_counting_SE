import os

def get_file_name_without_extension(file_path):
    file_name = os.path.basename(file_path)
    file_name_without_extension = os.path.splitext(file_name)[0]
    return file_name_without_extension

# Example usage
file_path = "/path/to/file.txt"
result = get_file_name_without_extension(file_path)
print(result)
