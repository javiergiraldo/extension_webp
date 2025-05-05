# Convertidor de Imágenes a WebP

Este script de Python toma una carpeta que contiene archivos de imágenes (JPG, JPEG, PNG, GIF, WebP) y los convierte al formato WebP. Las imágenes originales son eliminadas después de la conversión exitosa.

## Características

* Convierte automáticamente imágenes JPG, JPEG, PNG y GIF a formato WebP.
* Mantiene la transparencia de las imágenes PNG (formato RGBA).
* Permite ajustar la calidad de la conversión WebP (por defecto es 85).
* Omite los archivos que ya están en formato WebP.
* Muestra mensajes informativos sobre el proceso de conversión y posibles errores.
* Elimina los archivos de imagen originales después de la conversión exitosa.

## Requisitos

* Python 3.x
* Pillow (PIL) instalado. Puedes instalarlo con:
    ```bash
    pip install Pillow
    ```

## Uso

1.  Guarda el script de Python (por ejemplo, `convertir_webp.py`).
2.  Crea una carpeta con las imágenes que deseas convertir (por ejemplo, `fondosCambiar`).
3.  Abre una terminal o símbolo del sistema, navega hasta el directorio donde guardaste el script.
4.  Ejecuta el script, modificando la ruta de la carpeta si es necesario:
    ```bash
    python convertir_webp.py
    ```
    O, si deseas especificar una calidad diferente (por ejemplo, 90):
    ```bash
    python convertir_webp.py -folder "otra_carpeta" -quality 90
    ```
    **Nota:** Actualmente, la ruta de la carpeta está hardcodeada en el script. Para mayor flexibilidad, considera modificar el script para recibir la ruta y la calidad como argumentos de línea de comandos.

## Advertencia

Este script elimina los archivos de imagen originales después de la conversión. Asegúrate de tener una copia de seguridad de tus imágenes si es necesario.

## Autor

Javier Giraldo

## Licencia

MIT License

Copyright (c) 2025 kappak-dev

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.