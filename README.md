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

Voer het onderstaande commando uit in de map zelf:

```
sudo python prepareDB.py
```

De benodigde database bestanden zullen nu aangemaakt worden

## Starten
Om gps-wardrive te starten wordt het volgende commando gebruikt

```
sudo python test.py
```

## Stoppen
Om gps-wardrive te starten wordt er het volgende commando gebruikt.

LET OP! Dit is noodzakelijk, anders is het mogelijk dat er databasebestanden overschreven raken

In de toekomst kan dit worden geautomatiseerd.

## Todo lijstje

Zie het TODO.md bestand

## Over gps-wardrive

GPS Wardrive is uitgegeven onder een GPLv3 licensie.
