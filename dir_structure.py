import os
import sys
 
def save_directory_structure(root_path, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for dirpath, dirnames, filenames in os.walk(root_path):
            depth = dirpath.replace(root_path, "").count(os.sep)
            indent = "    " * depth
            folder_name = os.path.basename(dirpath)
            f.write(f"{indent}📁 {folder_name}/\n")
 
            sub_indent = "    " * (depth + 1)
            for filename in filenames:
                f.write(f"{sub_indent}📄 {filename}\n")
 
    print(f"Directory structure saved to: {output_file}")
 
 
if len(sys.argv) < 2:
    print("Usage: python dirmap.py <root_path> [output_file]")
    sys.exit(1)
 
root_path   = sys.argv[1].rstrip(os.sep)
output_file = sys.argv[2] if len(sys.argv) >= 3 else os.path.join(root_path, "directory_structure.txt")
 
save_directory_structure(root_path, output_file)