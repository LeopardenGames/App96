# Update V0.1.5624
# 25.03.24

import time
import requests
import os

print('Starting Server...')
time.sleep(1)
print('Checking for Updates...')

def check_for_updates(repo_url, file_path):
    # GitHub API endpoint für die Releases des Repositories
    releases_url = f"{repo_url}/releases/latest"
    
    # GET-Anfrage an die Releases-URL senden
    response = requests.get(releases_url)
    
    # Überprüfen, ob die Anfrage erfolgreich war
    if response.status_code == 200:
        # JSON-Daten aus der Antwort extrahieren
        release_info = response.json()
        
        # Den neuesten Download-Link finden
        if 'assets' in release_info and len(release_info['assets']) > 0:
            download_url = release_info['assets'][0]['browser_download_url']
            
            # Den Dateinamen extrahieren
            file_name = os.path.basename(download_url)
            
            # Den Download-Link ausgeben
            print("Neueste Version gefunden. Lade herunter:", download_url)
            
            # Die Datei herunterladen
            download_file(download_url, file_path)
        else:
            print("Keine Dateien gefunden.")
    else:
        print("Fehler beim Abrufen der Informationen. Statuscode:", response.status_code)

def download_file(url, file_path):
    # GET-Anfrage senden und die Datei herunterladen
    response = requests.get(url)
    
    # Überprüfen, ob die Anfrage erfolgreich war
    if response.status_code == 200:
        # Die heruntergeladene Datei speichern
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print("Datei erfolgreich heruntergeladen.")
    else:
        print("Fehler beim Herunterladen der Datei. Statuscode:", response.status_code)

# GitHub-Repository-URL und Dateipfad für die heruntergeladene Datei festlegen
github_repo_url = "https://github.com/BENutzer123/Beispiel-Repository"
file_path = "update.py"

# Auf Updates prüfen und die Datei herunterladen
check_for_updates(github_repo_url, file_path)

time.sleep(2)


datei = open('logo.txt','r')
print(datei.read())
else
print('fehler')
