import re

def extract_urls(text):
    # 使用正则表达式提取 http:// 或 https:// 开头的 URL
    url_pattern = re.compile(r'https?://[^\s]+')
    return url_pattern.findall(text)

def main():
    # 读取 dizhi.txt 文件
    with open('dizhi.txt', 'r', encoding='utf-8') as file:
        content = file.read()

    # 提取 URL
    urls = extract_urls(content)

    # 将提取的 URL 保存到 url.txt 文件中，每行一个 URL
    with open('url.txt', 'w', encoding='utf-8') as file:
        for url in urls:
            file.write(url + '\n')

if __name__ == "__main__":
    main()