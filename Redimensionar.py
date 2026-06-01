import os
import zipfile
from PIL import Image

# Configuración
ANCHO = 576
ALTO = 324
carpeta_assets = "./asset"
nombre_zip = "fondos_Level2_576x324.zip"

print("Comenzando el redimensionamiento de las imágenes del Nivel 2...")

# Creamos el archivo ZIP de respaldo
with zipfile.ZipFile(nombre_zip, 'w') as archivo_zip:
    # Buscamos las 7 capas del fondo del nivel 2 (del 0 al 6)
    for i in range(7):
        # CAMBIO AQUÍ: Ahora busca 'Level2BgX.png'
        nombre_archivo = f"Level2Bg{i}.png"
        ruta_completa = os.path.join(carpeta_assets, nombre_archivo)

        if os.path.exists(ruta_completa):
            # 1. Abrimos la imagen gigante del Nivel 2
            with Image.open(ruta_completa) as img:
                # 2. La redimensionamos manteniendo los píxeles nítidos (estilo Pixel Art)
                img_redimensionada = img.resize((ANCHO, ALTO), Image.Resampling.NEAREST)

                # 3. Guardamos los cambios directamente en tu carpeta asset
                img_redimensionada.save(ruta_completa)

                # 4. Añadimos la imagen al archivo ZIP
                archivo_zip.write(ruta_completa, arcname=nombre_archivo)
                print(f"✓ {nombre_archivo} procesada a 576x324 y guardada.")
        else:
            print(f"✗ No se encontró el archivo en la carpeta asset: {nombre_archivo}")

print(f"\n¡Listo! Las imágenes originales de 'Level2Bg' han sido modificadas.")
print(f"Se generó el respaldo '{nombre_zip}' en la raíz de tu proyecto.")