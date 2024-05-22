import requests

def download_file(url):
    response = requests.get(url)
    response.raise_for_status()  # Assure que la requête a réussi
    return response.text

def text_to_list(text):
    return text.splitlines()

# URL du fichier à télécharger
url = "https://raw.githubusercontent.com/Rakou-FR/BDD-licences/main/tiktok.txt"

# Télécharger le contenu du fichier
file_content = download_file(url)

# Transformer le contenu en liste de lignes
lines_list = text_to_list(file_content)

# Afficher la liste des lignes
for line in lines_list:
    print(line)
