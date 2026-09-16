# Publikationen hinzufügen

Script: `scripts/add_publications.py`

## Kurzversion

```
python3 scripts/add_publications.py pfad/zu/neuen_paper.bib
```

Bib-Datei mit den neuen Einträgen reinwerfen (z. B. Export aus Zotero), das
Script legt für jeden neuen Eintrag eine Markdown-Datei in `_publications/`
an, im gleichen Format wie der Rest der Seite.

## Details

- Bereits vorhandene Publikationen werden automatisch übersprungen
  (erkannt am Dateinamen). Man kann also jederzeit den ganzen
  Zotero-Export erneut durchlaufen lassen, ohne dass etwas kaputtgeht
  oder von Hand editierte Dateien überschrieben werden.
- Um eine bestehende Datei trotzdem neu zu generieren: `--force` anhängen.

```
python3 scripts/add_publications.py pfad/zu/neuen_paper.bib --force
```

- Bilder: im Bib-Eintrag ein Feld `note = {dateiname.jpg}` eintragen und
  das Bild entweder direkt in `images/publications/` legen, oder den
  Ordner mit `--images pfad/zum/ordner` angeben. Das Script kopiert das
  Bild dann automatisch nach `images/publications/` und bindet es als
  Header-Teaser auf der Publikationsseite ein.

```
python3 scripts/add_publications.py pfad/zu/neuen_paper.bib --images pfad/zum/bilderordner
```

- Hilfe/alle Optionen: `python3 scripts/add_publications.py --help`

## Ablauf beim Hinzufügen neuer Paper

1. Neue Einträge in Zotero (oder wo auch immer) sammeln und als `.bib`
   exportieren.
2. Script wie oben laufen lassen.
3. Ausgabe prüfen: `Created/updated: N` zeigt, welche Dateien neu
   angelegt wurden, `Skipped` die, die schon existieren.
4. Falls gewünscht, die neu erzeugten `.md`-Dateien in `_publications/`
   noch von Hand nachschärfen (z. B. Abstract kürzen, Autorenreihenfolge
   korrigieren).
5. Wie gewohnt committen und pushen.
