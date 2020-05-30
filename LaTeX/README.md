Inhalt
===

## 1) Einführung
  * worum geht es?
  * Thematik
    * Problematik der Datenerfassung auf ICUs
    * bisherige Ansätze, Forschungsarbeiten, Paper etc.
  * was ist maschinelles lernen?
    * **Formale Definition von [Mitchell, Tom. (1997). Machine Learning]**
      * A machine is said to learn from experience E with respect to some class of tasks T and performance measure P...
    * historischer Kontext (big data, processing power Moore's law etc)
    * Arten von maschinellem lernen (supervised, unsupervised)
    * numerische optimierung
    * Herausforderungen von ML für NLP
    * warum ML f. Bearbeitung der Problematik?

## 2) Übersicht über die gegebenen Daten
  * Abb: Liniendiagramm Anzahl key-werte paare pro predicted varid (farbe) und text varid (line typ) sowie max cutoff time
  * **exemplarische Beschreibung eines Patienten (z.B. 0430)**
  * **Abb: scatter plot events f. einen Patient (z.B. 0430)**
  * **Vergleich der verschiedenen Methoden, Wertepaare aus den Daten zu generieren**
    * nearest value pairs
    * last text observation carried forward
    * Vergleich anhand der scatter plots f. **einen** geeigneten Patienten
  * **Tabelle: VarIDs | Bedeutungen**
  * **jeweils kurzer Überblick über die einzelnen VarIDs**

## 3) Vorgehensweise
  * Baseline-Modell
    * Implementierung
      * featurization der texte
      * was sind R-Value, gamma etc?
      * Tuning von Hyperparametern mit R^2 (siehe "Vgl. vers. Metriken")
    * Vergleich/Funktionsweise verschiedener Performance-Metriken (R^2, MSE, ...)
    * Ergebnisse
  * Novel model (ANN)
    * ...

## 4) Schluss
  * Ergebnisse
  * **Anwendung in der Zukunft**
    * Vorgänge bei Datenerfassung auf ICU optimieren
    * Erfassung von Qualität der bisher eingetragenen Daten


Literatur
===
* https://www.aclweb.org/anthology/W18-2502/
* https://scikit-learn.org/stable/modules/cross_validation.html
* https://scikit-learn.org/stable/modules/grid_search.html
* https://www.ingentaconnect.com/content/wk/ccm/2018/00000046/00000004/art00031
* https://www.aclweb.org/anthology/W17-5043/
* Mitchell, Tom. (1997). Machine Learning
  * formelle Definition von ML für die Einleitung