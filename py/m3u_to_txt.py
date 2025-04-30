import os  
  
def read_m3u_file(file_path):  
    with open(file_path, 'r', encoding='utf-8') as file:  
        lines = file.readlines()  
    return lines  
  
def write_txt_file(file_path, content):  
    with open(file_path, 'w', encoding='utf-8') as file:  
        file.writelines(content)  
  
def convert_m3u_to_txt(m3u_lines):  
    channels = {}  
    current_group = None  
    i = 0  
  
    while i < len(m3u_lines):  
        line = m3u_lines[i].strip()  
        if line.startswith('#EXTINF'):  
            _, info = line.split('#EXTINF:', 1)  
            info_parts = info.split(',', 1)  
            metadata = [item.split('=') for item in info_parts[0].split() if '=' in item]  
            channel_name = info_parts[1].strip('"')  
            channel_url = m3u_lines[i + 1].strip()  
  
            group_title_info = next((item for item in metadata if item[0] == 'group-title'), None)  
            if group_title_info:  
                current_group = group_title_info[1].strip('"')  # 去掉双引号  
  
            channels.setdefault(current_group, []).append({'name': channel_name, 'url': channel_url})  
            i += 2  
        else:  
            i += 1  
  
    txt_content = []  
    for group, channel_list in channels.items():  
        # 确保 group 名称周围没有双引号  
        txt_content.append(f"{group},#genre#\n")  
        for channel in channel_list:  
            txt_content.append(f"{channel['name']},{channel['url']}\n")  
  
    return txt_content  
  
def main():  
    m3u_directory = 'tv'  
    for filename in os.listdir(m3u_directory):  
        if filename.endswith('.m3u'):  
            m3u_file_path = os.path.join(m3u_directory, filename)  
            txt_file_name = filename.rsplit('.', 1)[0] + '.txt'  
            txt_file_path = os.path.join(m3u_directory, txt_file_name)  
  
            m3u_lines = read_m3u_file(m3u_file_path)  
            txt_content = convert_m3u_to_txt(m3u_lines)  
            write_txt_file(txt_file_path, txt_content)  
            print(f"Converted {m3u_file_path} to {txt_file_path}")  
  
if __name__ == "__main__":  
    main()