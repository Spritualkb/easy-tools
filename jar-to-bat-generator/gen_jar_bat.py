import os
import sys

def generate_bat_files(root_folder):
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith(".jar"):
                jar_path = os.path.join(dirpath, filename)
                bat_content = f'java -jar "{filename}"\n'
                bat_filename = os.path.splitext(filename)[0] + ".bat"
                bat_path = os.path.join(dirpath, bat_filename)
                
                with open(bat_path, "w") as bat_file:
                    bat_file.write(bat_content)
                print(f"Generated {bat_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python gen_jar_bat.py <path_to_directory>")
        sys.exit(1)
    
    root_folder = sys.argv[1]
    generate_bat_files(root_folder)
