import os
from PIL import Image


def redimensionar_enemigos():
    # Diccionario con la configuración de los enemigos: "Nombre": ("Archivo_Origen", (Ancho, Alto))
    enemigos = {
        "Enemy1": ("./asset/Enemy1.png", (59, 26)),
        "Enemy2": ("./asset/Enemy2.png", (59, 27))
    }

    for nombre, (ruta_origen, nuevo_tamano) in enemigos.items():
        if not os.path.exists(ruta_origen):
            print(f"❌ Error: No se encontró el archivo original en: {ruta_origen}")
            print(
                f"Asegúrate de que el archivo se llame exactamente '{os.path.basename(ruta_origen)}' dentro de asset.")
            continue

        try:
            with Image.open(ruta_origen) as img:
                # Creamos el nombre de destino (ej: ./asset/Enemy1_scaled_59x26.png)
                ruta_destino = f"./asset/{nombre}_scaled_{nuevo_tamano[0]}x{nuevo_tamano[1]}.png"

                # Redimensionar con filtro de alta calidad
                img_redimensionada = img.resize(nuevo_tamano, Image.Resampling.LANCZOS)

                # Guardar el resultado
                img_redimensionada.save(ruta_destino, "PNG")

                print(f"✨ ¡{nombre} listo! Guardado en: {ruta_destino}")
                print(f"   Tamaño original: {img.size} -> Nuevo tamaño: {img_redimensionada.size}")

        except Exception as e:
            print(f"💥 Ocurrió un error al procesar {nombre}: {e}")


if __name__ == "__main__":
    redimensionar_enemigos()