import requests
from bs4 import BeautifulSoup

myVariable = "https://www.yelp.com/biz/milk-and-cream-cereal-bar-new-york?osq=Ice+Cream"

# Faites une requête HTTP pour obtenir le contenu HTML
response = requests.get(myVariable)
html_content = response.content

# Utilisez Beautiful Soup pour analyser le HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Ouvrir un fichier en mode écriture
with open('file.html', 'wb') as f:
    f.write(html_content)
    f.close()

# Trouvez toutes les balises <a> (liens) dans le HTML
links = soup.find_all('a')

# Ouvrez un fichier en mode texte ('w') pour écrire les liens
with open('justLink.html', 'w', encoding='utf-8') as f:
    # Écrivez le début du fichier HTML
    f.write('<html><body>\n')

    # Parcourez les liens et écrivez-les dans le fichier HTML
    for link in links:
        href = link.get('href')
        if href:
            f.write(f'<a href="{href}">{href}</a><br>\n')

    # Écrivez la fin du fichier HTML
    f.write('</body></html>')