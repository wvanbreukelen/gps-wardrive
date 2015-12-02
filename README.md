# gps-wardrive
GPS library voor wardriving. Met specifieke reden gemaakt, namelijk het profielwerkstuk voor 5 HAVO

## Installatie

Om gps-wardrive te installeren zijn een aantal hulpprogramma's vereist, deze zijn te installeren door het volgende commando in een
terminal uit te voeren

```
sudo apt-get install gpsd gpsd-clients python-gps pip python python-dev
```

Wanneer dit is voltooid moet de wifi module voor Python geinstalleerd worden
Voer het onderstaande command in

```
sudo pip install wifi
```

Wanneer deze stappen zijn voltooid is het mogelijk om gps-wardrive zelf te installeren.

Voer het onderstaande commando uit in de map waarin je gps-wardrive geplaatst heb:

```
sudo python prepareDB.py
```

De benodigde database bestanden zullen nu aangemaakt worden

## Starten
Om gps-wardrive te starten wordt het volgende commando gebruikt

```
sudo bash gps-wardrive.sh
```

Gps-wardrive zal nu proberen om het benodigde WiFi en GPS signaal te pakken te krijgen.
Dit kan even duren, heb geduld...

## Stoppen
Om gps-wardrive te starten wordt er het volgende commando gebruikt.

```
sudo pkill gps-wardrive
```

LET OP! Dit is noodzakelijk, anders is het mogelijk dat er databasebestanden overschreven raken

In de toekomst kan dit worden geautomatiseerd.

## Todo lijstje

Zie het TODO.md bestand

## Over gps-wardrive

Gps-wardrrive is ontwikkeld door wvanbreukelen en uitgegeven onder GPLv3 licensie.

