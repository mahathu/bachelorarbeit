Baseline Model
====

Annahme: **gelabelte, eingetragene Werte als "ground truth". Vermutlich ist so keine hohe predictive Genauigkeit möglich, weil die eingetragenen Werte im Datensatz oft von denen im Text abweichen. Das zu bestimmen ist ja genau der Punkt der Arbeit.**

### Input/Output
Verschiedene Möglichkeiten zum Generieren von Trainings-/Testdaten:

2) über einen Zeitraum labels Durchschnitt bilden, input texte konkatenieren

### Probleme
* Texte enthalten z.B "RASS = -4", das wird vermutlich nicht richtig erkannt

### Erkenntnisse
* rechenintensivster Prozess ist die Featurization der Eingabedaten
* Featurization der Eingabedaten hat deutlich größeren Einfluss auf predictive performance als die hyperparameter
* SGD performance steigt ab etwa 3000 samples (?) nicht signifikant weiter an
* Performance durch GSCV-Optimierung f. R^2 ähnlich gut wie wenn man f. neg-MAE optimiert
* Anzahl der samples und die meisten Hyperparameter machen scheinbar keinen Unterschied f SVR

### Noch ausprobieren
* Classification statt Regression?

### Plots
1) performance by n_samples and model
1.1) fit times by n_samples
1.2) fit times by n_samples
2) performance by offset (n_samples gleich, aber abstand der texte größer)