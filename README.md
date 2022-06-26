# Zoo Shop

REQUIREMENTS:
1) python >3.7 pip must be installed on your pc
2) node package manager must be installed on your pc

HOW TO RUN
-

To setup python virtual environment (for Windows):
```cmd|powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

To install all dependencies:
```cmd|powershell
pip install -r reqiurements.txt
```

To start back-end:
```cmd|powershell
$env:FLASK_APP="flaskr/main"
flask run
```


To start front-end:
```cmd|powershell
cd ui
npm i
npm start
```
