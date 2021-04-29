Baseline Model
====

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


### RASS=n filtern?
Visite_ZNS: 24040 Texte, 8426 enthalten RASS (35.05%)
Visite_Pflege: 27330 Texte, 284 enthalten RASS (1.04%)
Visite_Oberarzt: 11674 Texte, 446 enthalten RASS (3.82%)

1) Vergleich mit: RASS=n vorher aus freitext rausfiltern

Dafür: Visite_ZNS --> RASS, 45min max offset. da gibt es insgesamt 11022 paare aus diesem Datensatz.
genau 1000 random samples. normales svr trainiert, sowie ein svr, in dem alle vorkommen der Art "rass=n" aus den datensätzen gefiltert wurden. die performance wurde anhand von MAE mit 5-fold CV bestimmt (test_size=.2). dieser vorgang wurde 10 mal wiederholt, und für beide modelle wurde der mittelwert gebildet.
SVR verwendet mit folgenden Paramtern:
`{'svr__C': 10, 'svr__kernel': 'rbf' (gamma=scale), 'vect__analyzer': 'char', 'vect__ngram_range': (1, 5)}`

**Ergebnis:**
MAE for default SVR: 1.1294237465189472
MAE for SVR where RASS=n got filtered: 1.1697420881171667
In keinem der 10 Testläufe schnitt das modell, bei dem RASS=n herausgefiltert wurde, besser ab.
**Schlussfolgerung:** keine statistisch signifikante abweichung zwischen den ergebnissen -> SVR Modell nutzt vorkommen von rass=n nur bedingt, um daraus eine vorhersage des dem text entsprechenden RASS-Wertes zu bestimmen.

2/optional) training mit allen werten, test mit 2 datensätzen (komplett separat von trainingsset): texte, die RASS=n enthalten und solchen, die es nicht enthalten, performance vergleichen