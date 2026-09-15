# Dart and Arrow Classification and Point Reduction Effects

## Español

Esta carpeta reúne los códigos, modelos y materiales computacionales asociados al análisis de la **clasificación de puntas bifaciales de dardo y flecha** y del **efecto de la reducción o reactivación de las puntas durante su uso**.

El proyecto evalúa el desempeño de modelos estadísticos multivariados para distinguir puntas de dardo y flecha a partir de variables morfométricas, y examina en qué medida la reducción, particularmente la pérdida de longitud por reactivación y reparación, puede afectar esa clasificación.

### Clasificación mediante LDA

Se comparan tres modelos de **análisis discriminante lineal (LDA)**:

- **LW:** longitud + ancho
- **WT:** ancho + espesor
- **LWT:** longitud + ancho + espesor

Los modelos se evalúan mediante conjuntos de entrenamiento y prueba, diferentes umbrales de probabilidad posterior (0.15 y 0.50) y validación cruzada repetida. Entre las medidas de desempeño consideradas se incluyen exactitud (accuracy), sensibilidad, especificidad, exactitud balanceada (balanced accuracy) y Kappa.

### Efectos de la reducción

Una segunda parte del análisis examina la hipótesis de que la reducción de las puntas durante su uso puede introducir un sesgo sistemático en la clasificación. El interés se centra especialmente en la longitud, dado que la reactivación puede reducirla considerablemente mientras que el ancho y el espesor pueden cambiar relativamente poco.

El proyecto incluye análisis de datos experimentales de reactivación, modelos de regresión logística para evaluar la relación entre reducción y errores de clasificación, y simulaciones de puntas de dardo con longitudes reducidas para explorar cómo cambia la probabilidad de clasificación a medida que disminuye la longitud.

### Aplicación Shiny

La carpeta contiene también una aplicación **Shiny** que permite aplicar los modelos LDA desarrollados en este proyecto para estimar la asignación funcional de nuevas puntas como dardos o flechas.

### Estructura actual

```text
Dart_and_Arrows/
├── README.md
├── app.R
├── lda_LW.rds
├── lda_LWT.rds
└── lda_WT.rds
```

Los scripts de preparación de datos, ajuste y evaluación de modelos, análisis de umbrales, análisis de reducción y simulaciones se incorporarán progresivamente a esta carpeta.

### Referencia

Este repositorio acompaña el manuscrito:

> Shott, M. J., Cardillo, M. & Charlin, J. *Darts, Arrows and Stone-tool Length Reduction: A New Classification Model using an Expanded Dataset*.

El manuscrito compara métodos tradicionales basados en umbrales con métodos multivariados y analiza experimentalmente la posible influencia de la reducción de las puntas sobre la clasificación de dardos y flechas.

---

## English

This folder contains the code, models, and computational materials associated with the analysis of **bifacial dart and arrow point classification** and the **effects of point reduction or resharpening during use**.

The project evaluates multivariate statistical models for distinguishing dart and arrow points using morphometric variables and examines the extent to which reduction, particularly loss of length through resharpening and repair, can affect classification.

### LDA classification

Three **linear discriminant analysis (LDA)** models are compared:

- **LW:** length + width
- **WT:** width + thickness
- **LWT:** length + width + thickness

Models are evaluated using training and test sets, alternative posterior-probability thresholds (0.15 and 0.50), and repeated cross-validation. Performance measures include accuracy, sensitivity, specificity, balanced accuracy, and Kappa.

### Reduction effects

A second component of the project examines the hypothesis that point reduction during use can introduce systematic bias into dart and arrow classification. Particular attention is given to length because resharpening can substantially reduce it while width and thickness may change comparatively little.

The project includes analyses of experimental resharpening data, logistic regression models evaluating the relationship between reduction and classification errors, and simulations of dart points with reduced lengths to explore how classification probabilities change as length decreases.

### Shiny application

The folder also contains a **Shiny** application for applying the LDA models developed in this project to estimate the functional assignment of new points as darts or arrows.

### Current structure

```text
Dart_and_Arrows/
├── README.md
├── app.R
├── lda_LW.rds
├── lda_LWT.rds
└── lda_WT.rds
```

Scripts for data preparation, model fitting and evaluation, threshold analysis, reduction analyses, and simulations will be progressively added to this folder.

### Reference

This repository accompanies the manuscript:

> Shott, M. J., Cardillo, M. & Charlin, J. *Darts, Arrows and Stone-tool Length Reduction: A New Classification Model using an Expanded Dataset*.

The manuscript compares traditional threshold-based approaches with multivariate methods and experimentally examines the potential influence of point reduction on dart and arrow classification.
