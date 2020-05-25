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
Stemming ja/nein
Naive Bayes, **SVM**, ...

### Probleme
* Texte enthalten z.B "RASS = -4"

### Noch ausprobieren
* Key-Value Daten-Generierung: most recent Text per Score oder most recent Score per Text?
* Einfluss von Stemming