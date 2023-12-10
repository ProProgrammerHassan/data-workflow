# Bundesliga matchen
## Info ophalen
Alle data die gebruikt word, word opgehaald van de open api voetbalscores van het internet. Deze gegeven worden gebruikt om alle date op te halen van het huidig Bundesliga seizoen en weer te geven in een duidelijke tabel. Zoals aantal goals voor/tegen en winpercentage.

# Gebruik scripts
## script ophalen.py
Dit script word gebruikt om alle data van de api op te halen en weer te geven in een text bestand met allemaal ruwe data.

## Script omzetten.py
Dit script past de data van het testbestand aan naar een leesbaar csv. Dat we kunnen gebruiken om nieuwe resultaten mee te berekenen.

## Script statistiek.py
Dit zet de gegenereerde csv bestand om naar een leesbare markdown, waarin je duidelijk waarden kan lezen. Zoals wijnpercentage of aantal gescoorde doelpunten. Ik heb gekozen voor een markdown tabel omdat ik dit een zeer duidelijke manier vind van voetbal resultaten weer te geven. Dit is een duidelijk bestand dat iedereen kan verstaan.

## Script bereken.py
Het script bereken.py zorgt ervoor dat de informatie van de leesbare markdown tabel worden omgezet naar een eindrapport. Met analysering en beschrijving van alle data zodat een gebruiker weet wat er deze data betekend.

