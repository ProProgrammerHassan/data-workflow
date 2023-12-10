@echo off
cd data-workflow
python3 ophalen.py
python3 omzetten.py
python3 statiestiek.py
python3 bereken.py

git add .
git commit -m 'uitvoeren scripts en toevoegen'
git push origin main
