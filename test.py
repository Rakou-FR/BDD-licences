import requests

def download_file(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(response.text)

def read_file_to_list(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()


url = "https://raw.githubusercontent.com/Rakou-FR/BDD-licences/main/tiktok.txt"
filename = "tiktok.txt"


download_file(url, filename)


lines_list = read_file_to_list(filename)

for line in lines_list:
    print(line.strip())