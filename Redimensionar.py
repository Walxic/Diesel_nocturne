from PIL import Image
import os

# Rutas de las imágenes
ruta_original = "./asset/Score_.png"
ruta_nueva = "./asset/Score.png"

# Tamaño deseado
NUEVO_ANCHO = 576
NUEVO_ALTO = 324

print("Buscando la imagen de Score...")

if os.path.exists(ruta_original):
    # 1. Abrir la imagen original
    img = Image.open(ruta_original)

    # 2. Redimensionar usando un filtro de alta calidad (LANCZOS)
    print(f"Redimensionando de {img.size[0]}x{img.size[1]} a {NUEVO_ANCHO}x{NUEVO_ALTO}...")
    img_redimensionada = img.resize((NUEVO_ANCHO, NUEVO_ALTO), Image.Resampling.LANCZOS)

    # 3. Guardar con el nuevo nombre
    img_redimensionada.save(ruta_nueva)
    print(f"¡Éxito! Imagen guardada correctamente en: {ruta_nueva}")
else:
    print(f"Error: No se encontró el archivo '{ruta_original}'.")
    print("Asegúrate de que el script esté en la raíz del proyecto y que la imagen se llame exactamente 'Score_.png'.")