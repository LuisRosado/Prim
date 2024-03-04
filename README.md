# Programa de Detección de Esquinas y Creación de Grafo Mínimo en Mapa

Este programa en Python utiliza la biblioteca OpenCV para detectar esquinas en un mapa dado y luego construye un grafo mínimo utilizando el algoritmo de Prim de NetworkX. El objetivo es encontrar las esquinas del mapa y conectarlas de manera óptima para formar un camino mínimo.

## Requisitos de Instalación

Para ejecutar este programa, necesitará tener instaladas las siguientes bibliotecas de Python:

- OpenCV (`cv2`)
- NumPy (`numpy`)
- NetworkX (`networkx`)

Puede instalar estas bibliotecas utilizando pip:

```
pip install opencv-python numpy networkx
```

## Instrucciones de Uso

1. Asegúrese de tener el mapa en formato de imagen en el mismo directorio que este script.
2. Ejecute el script proporcionado.
3. El programa mostrará el mapa original en escala de grises y luego aplicará varios filtros para detectar esquinas y construir un grafo mínimo.
4. Finalmente, se mostrará el mapa con las esquinas detectadas y las conexiones entre ellas.

## Detalles del Programa

- El programa utiliza la función `cv2.cornerHarris` para detectar las esquinas en el mapa.
- Luego, aplica varios filtros morfológicos y de umbral para refinar la detección de esquinas.
- Utiliza NetworkX para construir un grafo mínimo conectando las esquinas detectadas.
- Las conexiones entre esquinas se calculan utilizando la distancia euclidiana entre ellas.
- Finalmente, se visualiza el mapa con las esquinas y las conexiones dibujadas.

## Ejemplo de Resultado

A continuación se muestra un ejemplo de cómo se vería el resultado de la detección de esquinas y la construcción del grafo mínimo:

![Ejemplo de Resultado](https://github.com/LuisRosado/Prim/assets/140114139/8f84be6e-5d12-4e5c-8235-2ee7fd1f645b)
![Ejemplo de Resultado](https://github.com/LuisRosado/Prim/assets/140114139/d8ac4a14-f17a-481b-9783-ba0decc7ce82)
![Ejemplo de Resultado](https://github.com/LuisRosado/Prim/assets/140114139/289ecb3a-6af3-49c3-86a5-4be89896ff13)

![Ejemplo de Resultado](https://github.com/LuisRosado/Prim/assets/140114139/03686b57-6de0-4568-846b-7aeeede72b18)
![Ejemplo de Resultado](https://github.com/LuisRosado/Prim/assets/140114139/01d66304-45b3-492b-a8b2-95b763ce6e3d)
![Ejemplo de Resultado](https://github.com/LuisRosado/Prim/assets/140114139/0b1e087e-4c82-4a57-af23-bc0262d68d90)

## Notas Adicionales

- Ajuste los parámetros según sea necesario para adaptarse a diferentes tipos de mapas y requisitos de detección de esquinas.
- Consulte la documentación de OpenCV y NetworkX para obtener más detalles sobre las funciones utilizadas en este programa.

¡Disfrute explorando y optimizando sus mapas con este programa!
