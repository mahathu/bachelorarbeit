allgemeine Notizen
====

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
| 20512802 | **DDS** (Delirium Detection Score)         | int, 1-35 (?)                                 | scores |
| 20512769 | **GCS** (Glasgow Coma Scale)           | int, 3-15                                     | scores |
| 20512801 | BPS (Behavior Pain Scale)          | int, 3-12                                     | scores |
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

Ideen f. BA
----

* Danksagungen: Henry Powell, Christine Szkudlarek, Felix Biessmann, Betreuer
* Überblick über die Daten
    * Probleme
        * Scores können sich schnell ändern
        * Daten evtl ungenau, erlauben keine hohe Präzision beim Predicten
    * Bar Charts f. Häufigkeit der verschiedenen Werte von DDS, GCS, BPS
    * exemplarisch: Eintragungen der Events pro Patient über Zeit, z.b. Patient 1019 
        * dazu Details zum Patienten, um es anschaulicher zu machen
        * Hinweis darauf, dass Daten anonymisiert vorlagen
* kurze Beschreibungen von DDS,GCS,BPS,CAM-ICU etc.

--------------

Baseline Model
----

Annahme: **gelabelte, eingetragene Werte als "ground truth". Vermutlich ist so keine hohe predictive Genauigkeit möglich, weil die eingetragenen Werte im Datensatz oft von denen im Text abweichen. Das zu bestimmen ist ja genau der Punkt der Arbeit.**

### Input/Output
Verschiedene Möglichkeiten zum Generieren von Trainings-/Testdaten:

1) last observation carried forward 
    * (+ ggf. wie lange diese her ist?)
    * Zeilen sortieren nach: Patient, dann Zeitpunkt. Danach Werte für GCS, RASS etc nach unten hin propagieren, bis sie geupdatet werden.
2) über einen Zeitraum labels Durchschnitt bilden, input texte konkatenieren
3) "man koennte auch irgendwie interpolieren zwischen den einzelnen werten der Schicht, dazu kann man auch andere Daten mit hoeherer Auflösung hernehmen um die Vorhersagen zu verbessern"

v.a.: damit rumexperimentieren, welche Textfelder die größte predictive power haben

Output: **RASS, GCS, etc**

### Vorgang (siehe E-Mail von Felix Biessmann vom 13.03.)
Du kannst dann vielleicht dem Beispiel [hier](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html) folgen fuer ne baseline, da werden numerische und kategorische features berücksichtigt. Für Text-Daten: **TfIdfVectorizer**. Supervised model: entweder regression oder classification (wenn scores gethresholded werden). Hyperparameter (preprocessing Parameter und regularizer oder so) per GridSearchCV bestimmen.

Compare: Naive Bayes, **SVM**, ...