import os

# Set the directory where the folders should be created
directory = "C:/Users/Lenovo/Desktop/Class notes"  # Change this to your actual directory path

# Create folders DAY 3 to DAY 31
for i in range(3, 32):
    folder_name = f"DAY {i}"
    folder_path = os.path.join(directory, folder_name)
    os.makedirs(folder_path, exist_ok=True)

print("Folders created successfully.")
