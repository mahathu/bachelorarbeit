Inhalt
===

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
      * erklären wie pipeline funktioniert
      * was sind R-Value, gamma etc?
      * Tuning von Hyperparametern mit R^2 (siehe "Vgl. vers. Metriken")
        * Anwendung von Kreuzvalidierung beim finden der besten Hyperparameter
    * Vergleich/Funktionsweise verschiedener Performance-Metriken (R^2, MSE, ...)
      * **Unterschied zwischen RMSE und MAE!**
        * es gilt immer: MAE <= RMSE
      * **Mean bias error betrachten!!**
        * wie MEA, aber ohne absolutbetrag --> indikator für bias des modells
    * Ergebnisse
      * Figures:
        * MAE Performance je nach Input/Output VARID
        * Line-Chart: Vergleich Performance SGD vs SVR nach n_samples
          * Zufällige auswahl der n samples aus allen wertepaaren mit min<60
          * (SGD braucht viel Daten, SVR erreicht beste Performance schon nach ca n=1000)
        
  * Novel model (ANN)
    * ...

## 4) Fazit
  * Ergebnisse
  * TODO: Auswertung der Visitentexte: Wo gibt es große Abweichungen von eingetragenem Score/Modell-Vorhersage?
  * **Anwendung in der Zukunft**
    * Vorgänge bei Datenerfassung auf ICU optimieren
    * Erfassung von Qualität der bisher eingetragenen Daten
    * z.b. einbeziehen der scores in clinicial decision support systems

## 5) Anhänge
  * Anhang A: ausgewählte Listings


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
* https://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf
* https://peekaboo-vision.blogspot.com/2012/09/recap-of-my-first-kaggle-competition.html
* https://machinelearningmastery.com/k-fold-cross-validation/
  * enthält links zu diesen Büchern über cross validation:
  * An Introduction to Statistical Learning, 2013
  * Artificial Intelligence: A Modern Approach (3rd Edition), 2009
  * Applied Predictive Modeling, 2013
* aclweb.org/anthology/W18-5914/