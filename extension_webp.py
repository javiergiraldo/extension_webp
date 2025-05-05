import os
from PIL import Image

def convert_images_to_webp(folder_path, quality=85):
    # Obtener todos los archivos en la carpeta
    files = os.listdir(folder_path)
    
    # Filtrar solo los archivos que son imágenes
    img_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp']
    img_files = [file for file in files if os.path.splitext(file)[1].lower() in img_extensions]

    for img_file in img_files:
        # Obtener el nombre del archivo sin extensión
        file_name = os.path.splitext(img_file)[0]
        
        # Crear el nuevo nombre con extensión .webp
        new_name = f"{file_name}.webp"
        
        # Rutas completas para el archivo original y el nuevo
        old_path = os.path.join(folder_path, img_file)
        new_path = os.path.join(folder_path, new_name)
        
        # Omitir si ya es webp
        if os.path.splitext(img_file)[1].lower() == '.webp':
            print(f"Ya era WebP, no se requirió conversión: {img_file}")
            continue
            
        try:
            # Abrir la imagen
            with Image.open(old_path) as img:
                # Si la imagen tiene transparencia (RGBA), mantenerla
                if img.mode == 'RGBA':
                    # WebP soporta transparencia, así que podemos mantener el modo RGBA
                    img.save(new_path, 'WEBP', quality=quality)
                else:
                    # Si no tiene transparencia, convertir a RGB si es necesario
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                    # Guardar la imagen en formato WebP
                    img.save(new_path, 'WEBP', quality=quality)
            
            # Eliminar el archivo original después de la conversión
            os.remove(old_path)
            print(f"Convertido: {img_file} -> {new_name}")
        except Exception as e:
            print(f"Error al procesar {img_file}: {str(e)}")

# Uso de la función
folder_path = "fondosCambiar"  # Reemplazar por la ruta de la carpeta a procesar
convert_images_to_webp(folder_path, quality=85)  # Puedes ajustar la calidad (0-100)