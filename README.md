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

Licencia de Uso No Comercial

Copyright (c) 2025 kappak-dev

POR FAVOR LEA CUIDADOSAMENTE LOS SIGUIENTES TÉRMINOS Y CONDICIONES ANTES DE UTILIZAR ESTE SOFTWARE.

Esta licencia otorga permiso para utilizar el software *extension_webp* únicamente para **fines no comerciales**. Se consideran fines no comerciales aquellos que no están dirigidos principalmente a obtener una ventaja comercial o una compensación monetaria. Esto incluye el uso personal, la investigación académica y la evaluación interna.

**Se prohíbe expresamente cualquier uso comercial del Software, incluyendo, pero no limitado a:**

* La integración del Software en productos o servicios que se vendan o se ofrezcan a cambio de una tarifa.
* La utilización del Software para proporcionar servicios a terceros con fines de lucro.
* La distribución del Software con la intención de obtener ganancias económicas.

**Requerimiento de Contacto para Uso Comercial:**

Si usted desea utilizar el Software para cualquier fin comercial, **debe contactar y obtener una licencia explícita por escrito del titular de los derechos de autor**, *Javier Giraldo*, a la siguiente dirección de correo electrónico: *javiergiraldorivera@gmail.com*. La concesión de una licencia comercial estará sujeta a términos y tarifas que se acordarán mutuamente.

**Otras Condiciones:**

* Se permite la copia y distribución del Software para fines no comerciales, siempre y cuando se mantenga intacto este aviso de licencia en todas las copias y se dé el crédito adecuado al titular de los derechos de autor.
* Se prohíbe la modificación del Software sin el permiso explícito por escrito del titular de los derechos de autor.
* EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA, INCLUYENDO PERO NO LIMITADO A LAS GARANTÍAS DE COMERCIABILIDAD, IDONEIDAD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO EL AUTOR O LOS TITULARES DE LOS DERECHOS DE AUTOR SERÁN RESPONSABLES DE NINGUNA RECLAMACIÓN, DAÑO U OTRA RESPONSABILIDAD, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O DE OTRO TIPO, QUE SURJA DE, O EN CONEXIÓN CON EL SOFTWARE O EL USO U OTROS TRATOS EN EL SOFTWARE.