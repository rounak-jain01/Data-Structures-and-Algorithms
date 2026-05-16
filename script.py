import os

# Folder path jahan files hain
folder_path = r"C:\Users\rouna\OneDrive\Desktop\DSA\Loops"

# Output file name
output_file = "combined.txt"

with open(output_file, "w", encoding="utf-8") as outfile:

    # Folder ki saari files traverse karo
    for file_name in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file_name)

        # Sirf files read karo
        if os.path.isfile(file_path):

            outfile.write(f"\n--- {file_name} ---\n")

            with open(file_path, "r", encoding="utf-8") as infile:
                content = infile.read()
                outfile.write(content)

            outfile.write("\n")

print("All files combined successfully!")