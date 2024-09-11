# David Flores Becerril

# Importar librerías
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load data
data = pd.read_csv('processed_data.txt')
data_present = data[data['MonkeyPox'] == 1]
data_absent = data[data['MonkeyPox'] == 0]

data_present_sampled = data_present.sample(n=500, random_state=42)
data_absent_sampled = data_absent.sample(n=500, random_state=42)

balanced_data = pd.concat([data_present_sampled, data_absent_sampled])
balanced_data = balanced_data.sample(frac=1, random_state=42).reset_index(drop=True)

# Split data into X and y
X = balanced_data.drop('MonkeyPox', axis=1)
y = balanced_data['MonkeyPox']

m = len(y)        # Número de ejemplos de entrenamiento
'''
Beneficios de la Normalización:
Mejora la convergencia de los algoritmos de optimización:

Muchos algoritmos de aprendizaje automático, como el descenso de gradiente, convergen más rápido cuando las características están normalizadas.
Evita que características con diferentes escalas dominen el modelo:

Si una característica tiene un rango mucho mayor que otras, puede dominar el modelo y hacer que sea menos efectivo.
Mejora la precisión del modelo:

La normalización puede llevar a una mejor precisión del modelo al asegurar que todas las características contribuyan de manera equitativa.
'''

# Añadir columna de unos a X para el término de sesgo
X = np.hstack((np.ones((X.shape[0], 1)), X))
'''
Permite al modelo ajustarse mejor a los datos al añadir una constante a la función de predicción
'''

# Inicializar theta
theta_inicial = np.zeros(X.shape[1])  # Inicializar theta con ceros [0, 0, 0]

# Parámetros
iteraciones = 1500 # Número de iteraciones
alpha = 0.01    # Tasa de aprendizaje

# Función sigmoidal - Funcion hipótesis para regresión logística
def sigmoidal(z):
    return 1 / (1 + np.exp(-z))

# Función de costo
def funcionCosto(theta, X, y):
    m = len(y)
    h = sigmoidal(X @ theta)
    h = np.clip(h, 1e-10, 1 - 1e-10)  # Evitar valores extremos AYUDA DE GPT
    '''
    Esta función limita los valores de h para que no sean menores que 1e-10 ni mayores que 1 - 1e-10.
    Esto es útil para evitar problemas numéricos, como divisiones por cero o logaritmos de cero, que pueden ocurrir en cálculos posteriores.
    '''
    J = (1 / m) * np.sum(-y * np.log(h) - (1 - y) * np.log(1 - h)) # Función de costo
    grad = (1 / m) * X.T @ (h - y) # Función de gradiente con operaciones vectorizadas
    
    return J, grad

# Aprendizaje 
def aprende(theta, X, y, iteraciones):
    for _ in range(iteraciones):
        J, grad = funcionCosto(theta, X, y)
        theta = theta - alpha * grad # Actualizar theta con funcion delta
    return theta

# Predicción
def predice(theta, X):
    probabilidad = sigmoidal(X @ theta)
    return (probabilidad >= 0.5).astype(int) # Devuelve 1 si la probabilidad es mayor o igual a 0.5, de lo contrario 0

# Graficar datos y la línea de decisión
def graficaDatos(X, y, theta=None):
    present = (y == 1)
    abscent = (y == 0)
    
    # Crear la gráfica
    plt.figure(figsize=(8, 6))
    plt.scatter(X[present, 1], X[present, 2], c='b', marker='x', label='Prescent')
    plt.scatter(X[abscent, 1], X[abscent, 2], c='r', marker='o', label='Abscent')

    if theta is not None:
        # Graficar la línea de decisión
        x_value = np.array([np.min(X[:, 1]), np.max(X[:, 1])])
        y_value = -(theta[0] + theta[1] * x_value) / theta[2]
        plt.plot(x_value, y_value, 'g-', label='Línea de decisión')

    plt.xlabel('Examen 1')
    plt.ylabel('Examen 2')
    plt.legend()
    plt.title('Datos y Línea de Decisión')
    plt.show()

def main():
    # Entrenar el modelo
    theta_final = aprende(theta_inicial, X, y, iteraciones)
    
    # Verificar el costo final
    costo_final, _ = funcionCosto(theta_final, X, y)
    print(f'Costo final: {costo_final:.3f}')
    print(f'Theta final: {theta_final}')
    
    # Predicción
    predicciones = predice(theta_final, X)
    
    # Precisión
    precision = np.mean(predicciones == y) * 100
    print(f'Precisión: {precision:.2f}%')
    
    # Graficar datos y la línea de decisión
    graficaDatos(X, y, theta_final)

if __name__ == '__main__':
    main()
