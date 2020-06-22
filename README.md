wichtiges Zeug
====

für besseres Modell:
* **NRS/VAS Bedingungen mit einbeziehen**, jeweils 1 Spalte für "ruhe", "intervent", ...
* **Spell Checker anwenden!** http://norvig.com/spell-correct.html

allgemeine Notizen
====

rot: #fb8072
blau: #80b1d3
limette: #b3de69
orange: #fdb462
lila: #bc80bd
pink: #fccde5
hellgelb: #ffffb3
(siehe colorbrewer)

Datendateien
----

|Dateiname |Beschreibung|
|----------|------------|
|delir.csv|Gibt für einzelne Patienten an, ob die Diagnose Delir nach ICD gestellt wurde (F05.*).
|patienten.csv, patienten20200312.csv|Metadaten über einzelne Patienten (Alter, Geschlecht, Zeit auf ICU etc). patienten20200312.csv enthält zusätzlich BMI
|scores1.csv|Enthält Scores der VarIDs 20512769,20512802,20512801 (GCS, DDS, BPS) pro Patient und Zeitpunkt.
|scores2.xlsx|Enthält Scores der 10 VarIDs aus Tabelle daten pro Patient und Zeitpunkt
|VarIDs.xlsx|Menschen-lesbare Namen der VarIDs

Die Spalte "Zeitpkt" in den scores-Dateien bezieht sich auf "**für wann** die Eintragung gelten soll" und ist berechnet in "Sekunden nach Aufnahme ins Krankenhaus"

|VarID     |Wert                                    |Inhalt                                         |Tabelle |
|----------|----------------------------------------|-----------------------------------------------|--------|
| 20512802 | **DDS** (Delirium Detection Score)     | int, 1-35 (?)                                 | scores |
| 20512769 | **GCS** (Glasgow Coma Scale)           | int, 3-15                                     | scores |
| 20512801 | BPS (Behavior Pain Scale)              | int, 3-12                                     | scores |
| 22085815 | **Visite_ZNS**                         | Text, idr kurz                                | daten  |
| 22085836 | **Visite_Pflege**                      | Text, eher länger                             | daten  |
| 22085820 | **Visite_Oberarzt**                    | Text, idr lang                                | daten  |
| 22085897 | Ramsay Sedation Scale (ähnl. RASS, wird aber nicht oft erhoben) | int, 1-6             | daten  |
| 22086169 | **CAM-ICU** (Confusion Assessment Method)  | (neg./pos.)                               | daten  |
| 22086158 | **RASS** (Richmond Agitation Sedation Scale) | int, +4 - -5                            | daten  |
| 22086067 | Vigilanz                               | Freitext, 1 Wort (z.b. "wach","somnolent")    | daten  |
| 22086170 | BPS-Bewertung                          | Freitext, 1-2 Worte (fast immer "ruhe")       | daten  |
| 22085911 | NRS/VAS (Schmerz?)                     | int (0-9)                                     | daten  |
| 22086172 | NRS/VAS Bedingungen                    | Freitext, 1-2 Worte (sehr ähnlich zu BPS)     | daten  |

**Input:** Visite_ZNS, Visite_Pflege, Visite_Oberarzt (ggf. später z.B. auch Zeit auf ICU)

**Predict:** (DDS), GCS, (BPS), CAM-ICU, RASS

--------------

Farben: https://material.io/design/color/the-color-system.html#tools-for-picking-colors

Ideen f. BA
----

* Überblick über die Daten
    * Probleme
        * Scores können sich schnell ändern
        * Daten evtl ungenau, erlauben keine hohe Präzision beim Predicten
    * VISUALISIERUNG: Bar Charts f. Häufigkeit der verschiedenen Werte von DDS, GCS, BPS
    * exemplarisch: Eintragungen der Events pro Patient über Zeit, z.b. Patient 1019 
        * dazu Details zum Patienten, um es anschaulicher zu machen
        * Hinweis darauf, dass Daten anonymisiert vorlagen
    * Methoden der Generierung von Wertepaaren aus den Daten
        * lassen sich gut durch Pfeile vergleichen
        * latest text
        * latest score
        * nearest value
        * VISUALISIERUNG: (y) n of data pairs vs (x) max time between (cut off)
* kurze Beschreibungen von DDS,GCS,BPS,CAM-ICU etc.
* Performance Metriken, und warum diese geeignet sind Performance der Modelle zu beurteilen