# Highscore API

Ett enkelt REST-API byggt med Python och Flask för att hantera och hämta spelresultat.

## 🛠️ Installation och Körning

Följ dessa steg för att köra projektet lokalt på din dator:

### 1. Klona repositoryt
```bash
git clone <din-repo-länk-här>
cd <mapp-namn>

2. Skapa en virtuell miljö (venv)
Skapa en virtuell miljö i mappen:
python -m venv venv

3. Aktivera den virtuella miljön
Windows (PowerShell):
venv\Scripts\Activate.ps1

Windows (Command Prompt):
venv\Scripts\activate.bat

Mac / Linux:
source venv/bin/activate

4. Installera beroenden (Flask)
pip install Flask

5. Starta servern
flask --app toplista run

🚀 Hur man testar API:et
Hämta högsta poängen (GET):
Gå till webbläsaren eller kör:
curl [http://127.0.0.1:5000/highscores](http://127.0.0.1:5000/highscores)

Lägga till en ny poäng (POST):
Kör följande kommando i terminalen:
curl.exe -X POST [http://127.0.0.1:5000/highscores](http://127.0.0.1:5000/highscores) -H "Content-Type: application/json" -d "1500"