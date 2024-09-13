# Clasificación de la Viruela del Mono usando Naive Bayes y Regresión Logística

Este proyecto clasifica la presencia o ausencia de la Viruela del Mono usando dos modelos: Naive Bayes y Regresión Logística. Los datos incluyen varias características clínicas que son usadas para predecir si un paciente tiene o no la enfermedad.

## Modelos Utilizados

### 1. Naive Bayes (CategoricalNB)
Naive Bayes es un modelo probabilístico basado en el Teorema de Bayes, que asume independencia condicional entre las características. Este modelo es ideal cuando las características son discretas o categóricas y funciona bien con datos balanceados.

**Ventajas:**
- Simple y eficiente.
- Menos propenso al sobreajuste.
- Rápido de entrenar y de predecir.
  
### 2. Regresión Logística
La Regresión Logística es un modelo lineal que utiliza una función sigmoide para modelar la probabilidad de una clase. Es ampliamente utilizado en problemas de clasificación binaria.

**Ventajas:**
- Altamente interpretable.
- Ideal para problemas donde se necesita entender la relación entre características y resultados.

## Resultados de los Modelos

- **Naive Bayes** mostró un mejor rendimiento debido a la independencia entre características y su capacidad de manejar datos discretos y balanceados.
- **Regresión Logística** también tuvo un buen rendimiento, aunque es más susceptible a datos ruidosos y características irrelevantes.

## Requisitos Previos

Antes de ejecutar el proyecto, asegúrate de tener instaladas las siguientes bibliotecas:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
