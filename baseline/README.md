Baseline Model
====

Annahme: **gelabelte, eingetragene Werte als "ground truth". Vermutlich ist so keine hohe predictive Genauigkeit möglich, weil die eingetragenen Werte im Datensatz oft von denen im Text abweichen. Das zu bestimmen ist ja genau der Punkt der Arbeit.**

### Probleme
* Texte enthalten z.B "RASS = -4", das wird vermutlich nicht richtig erkannt

### Erkenntnisse
* rechenintensivster Prozess ist die Featurization der Eingabedaten
* Featurization der Eingabedaten hat deutlich größeren Einfluss auf predictive performance als die hyperparameter
* SGD performance steigt ab etwa 3000 samples (?) nicht signifikant weiter an
* Performance durch GSCV-Optimierung f. R^2 ähnlich gut wie wenn man f. neg-MAE optimiert
* Anzahl der samples und die meisten Hyperparameter machen scheinbar keinen Unterschied f SVR

* Selbst, wenn man den Input text komplett entfernt, kommt man nur anhand von raten anhand der verteilung der mögl. werte auf MAE=1.765
* Wenn man nur auf erste 5 Zeichen guckt hat man MAE=1.3 (ca)

### Plots
1) performance by n_samples and model
1.1) fit times by n_samples
1.2) fit times by n_samples
2) performance by offset (n_samples gleich, aber abstand der texte größer)


### LETZTE SCHRITTE
Dafür: Visite_ZNS --> RASS, 45min max offset, genau 10.000 samples.
SVR verwenden mit folgenden Paramtern:
`{'svr__C': 10, 'svr__kernel': 'rbf' (gamma=scale), 'vect__analyzer': 'char', 'vect__ngram_range': (1, 5)}`

1) Vergleich mit: RASS=n vorher aus freitext rausfiltern
Ergebnis: Abweichung nur 1-2%

2) training mit allen werten, test mit 2 datensätzen (komplett separat von trainingsset): texte, die RASS=n enthalten und solchen, die es nicht enthalten, performance vergleichen