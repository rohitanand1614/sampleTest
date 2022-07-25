cd "%cd%" &
pip install virtualenv &
virtualenv venv &
"cmd.exe" "/c .\venv\Scripts\activate && pip install -r requirements.txt && pytest --driver chrome"