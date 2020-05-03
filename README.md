allgemeine Notizen
====

Datendateien
----

**Input:** Visite_ZNS, Visite_Pflege, Visite_Oberarzt (ggf. später z.B. auch Zeit auf ICU)

**Output:** DDS, GCS, BPS, RASS

|Dateiname |Beschreibung|
|----------|------------|
|delir.csv|Gibt für einzelne Patienten an, ob die Diagnose Delir nach ICD gestellt wurde (F05.*).
|patienten.csv, patienten20200312.csv:|Metadaten über einzelne Patienten (Alter, Geschlecht, Zeit auf ICU etc). patienten20200312.csv enthält zusätzlich BMI
|scores1.csv|Enthält Scores der VarIDs 20512769,20512802,20512801 (GCS, DDS, BPS) pro Patient und Zeitpunkt.
|scores2.csv|Enthält Scores der 10 VarIDs aus Tabelle daten pro Patient und Zeitpunkt
|VarIDs.xlsx|Menschen-lesbare Namen der VarIDs

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
Du kannst dann vielleicht dem Beispiel [hier](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html) folgen fuer ne baseline, da werden numerische und kategorische features berücksichtigt.

Für Text-Daten: **TfIdfVectorizer**

Supervised model: entweder regression oder classification (wenn scores gethresholded werden)

Compare: Naive Bayes, **SVM**, ...

Hyperparameter (preprocessing Parameter und regularizer oder so) per GridSearchCV bestimmen