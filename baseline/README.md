Baseline Model
====

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
Vergleich von:
Key-Value Daten-Generierung: most recent Text per Score oder most recent Score per Text?

### Probleme
* Texte enthalten z.B "RASS = -4", das wird vermutlich nicht richtig erkannt

### Erkenntnisse
* rechenintensivster Prozess ist die Featurization der Eingabedaten
* Featurization der Eingabedaten hat deutlich größeren Einfluss auf predictive performance als die hyperparameter
* SGD performance steigt ab etwa 3000 samples (?) nicht signifikant weiter an

### Noch ausprobieren
* Einfluss von Stemming
* Auf das beste, getunte Modell andere Input-Daten anwenden, d.h. größere oder kleinere char ngram-range ausprobieren.

Anzahl der samples und die meisten Hyperparameter machen scheinbar keinen Unterschied f SVR