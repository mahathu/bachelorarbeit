**Das Verzeichnis /data/ ist .gitignored, sodass keine patientenbezogenen Daten im öftl. git-repo vorliegen. Ohne diese funktioniert aber der Großteil des Codes nicht. Bei Bedarf also manuell Daten aus COPRA exportieren oder mich fragen**

für besseres Modell:
* **NRS/VAS Bedingungen mit einbeziehen**, jeweils 1 Spalte für "ruhe", "intervent" (one hot encoding)

http://ksrowell.com/blog-visualizing-data/wp-content/uploads/2012/02/optimal-colors-for-graphs.png
Colors:
blue: #3969b1
orange: #da7c30
green: #3e9651
red: #cc2529

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

--------------

Delirium Detection Score (DDS) hat nur 5 Parameter, richtig? Weil max score laut histogramm 35 ist --> Richtig!
DDS eher zur bestätigung eines vorliegenden Delirs. Wird idR nur von pflegeperson eingetragen
DDS besser geeignet, verlauf eines bestehenden delirs zu beschreiben, als nur cam-icu