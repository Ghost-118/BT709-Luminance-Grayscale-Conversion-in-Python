# 🖼️ Conversión a Escala de Grises mediante Luminancia BT.709 en Python

Este repositorio contiene una implementación en Python para convertir imágenes a escala de grises aplicando los coeficientes de luminancia del estándar **ITU-R BT.709** sobre los canales de color (BGR) utilizando la librería OpenCV.

El algoritmo extrae individualmente los canales Rojo ($R$), Verde ($G$) y Azul ($B$), aplica una ponderación específica basada en la percepción visual estándar ($w_r = 0.2125, w_g = 0.7154, w_b = 0.072$) y guarda las imágenes resultantes en formato entero[cite: 12].

---

## 🚀 Características

* **Ponderación BT.709:** Aplica coeficientes específicos para cada canal de color según el estándar HDTV[cite: 12, 13]:
  $$Gris = \frac{0.2125 \cdot R + 0.7154 \cdot G + 0.072 \cdot B}{3}$$
* **Procesamiento por Lote:** Procesa iterativamente múltiples imágenes de prueba (`img1.jpg`, `img2.jpg`, `img3.jpg`)[cite: 12].
* **Exportación de Resultados:** Guarda automáticamente cada imagen procesada en formato JPEG añadiendo el sufijo `_E10.jpg`[cite: 12].

---

## 🛠️ Requisitos e Instalación

### Requisitos previos
* Python 3.x
* OpenCV (`opencv-python` o `opencv-python-headless` para entornos en la nube como GitHub Codespaces)

### Instalación

1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/Ghost-118/BT709-Luminance-Grayscale-Conversion-in-Python.git](https://github.com/Ghost-118/BT709-Luminance-Grayscale-Conversion-in-Python.git)
   cd BT709-Luminance-Grayscale-Conversion-in-Python
