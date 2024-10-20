# remove_duplicates.py  
  
def remove_duplicates(file_path):  
    with open(file_path, 'r', encoding='utf-8') as file:  
        lines = file.readlines()  
  
    seen = set()  
    unique_lines = []  
    for line in lines:  
        line = line.strip()  
        if line not in seen:  
            unique_lines.append(line)  
            seen.add(line)  
  
    with open(file_path, 'w', encoding='utf-8') as file:  
        file.writelines(f"{line}\n" for line in unique_lines)  
  
if __name__ == "__main__":  
    remove_duplicates('tt.txt')