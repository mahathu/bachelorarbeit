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
    * classification vs regression
    * (numerische optimierung)
      * numerische optimierung: Lösungsgraum, Bewertungsfunktion
      * das Gradientenverfahren
      * stochastic gradient descend
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
  * **Problem mit Qualität der Daten! Geeignete Trainingspaare?**

## 3) Vorgehensweise
  * Baseline-Modell
    * Implementierung
      * featurization der texte
      * was sind R-Value, gamma etc?
      * Tuning von Hyperparametern mit R^2 (siehe "Vgl. vers. Metriken")
        * Anwendung von Kreuzvalidierung beim finden der besten Hyperparameter
    * Vergleich/Funktionsweise verschiedener Performance-Metriken (R^2, MSE, ...)
    * Ergebnisse
  * Novel model (ANN)
    * ...

## 4) Fazit
  * Ergebnisse
  * **Anwendung in der Zukunft**
    * Vorgänge bei Datenerfassung auf ICU optimieren
    * Erfassung von Qualität der bisher eingetragenen Daten

## 5) Anhänge
  * Anhang A: ausgewählte Listings


Notizen
===
section, subsection, und ggf. subsubsection machen noch sinn. 
paragraph, subparagraph sollten nicht verwendet werden

Literatur
===
* https://www.aclweb.org/anthology/W18-2502/
* https://scikit-learn.org/stable/modules/cross_validation.html
* https://scikit-learn.org/stable/modules/grid_search.html
* https://www.ingentaconnect.com/content/wk/ccm/2018/00000046/00000004/art00031
* https://www.aclweb.org/anthology/W17-5043/
* Mitchell, Tom. (1997). Machine Learning
  * formelle Definition von ML für die Einleitung
* https://storage.googleapis.com/pub-tools-public-publication-data/pdf/b91400f14e27ec9dacf0a389e72fd0e0fa9c2535.pdf
* https://www.cs.waikato.ac.nz/~eibe/pubs/ordinal_tech_report.pdf
* https://pubmed.ncbi.nlm.nih.gov/31947237/
* https://scikit-learn.org/stable/modules/svm.html#mathematical-formulation (Erklärung von SVM)
* https://www.cs.waikato.ac.nz/~ml/weka/book.html#Contents (Definition von Kreuzvalidierung)
* https://web.stanford.edu/~hastie/ElemStatLearn/