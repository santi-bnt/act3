import cv2
import numpy as np
import matplotlib.pyplot as plt

def pera(img_path):
    # Leer imagen y convertir a HSV
    img = cv2.imread(img_path)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    height, width = img.shape[:2]

    # Eliminar la parte superior (rabo)
    # Ignora el 15% superior de la imagen
    crop_start = int(height * 0.15)
    img_hsv = img_hsv[crop_start:height, :]
    img_rgb = cv2.cvtColor(img[crop_start:height, :], cv2.COLOR_BGR2RGB)

    # Detectar color café (manchas)
    lower_brown = np.array([5, 60, 20], dtype=np.uint8)
    upper_brown = np.array([25, 255, 180], dtype=np.uint8)
    mask_brown = cv2.inRange(img_hsv, lower_brown, upper_brown)

    # Limpiar ruido
    kernel = np.ones((5, 5), np.uint8)
    mask_brown = cv2.morphologyEx(mask_brown, cv2.MORPH_OPEN, kernel)
    mask_brown = cv2.morphologyEx(mask_brown, cv2.MORPH_CLOSE, kernel)

    # Calcular porcentaje de área café
    total_pixels = img_hsv.shape[0] * img_hsv.shape[1]
    brown_pixels = cv2.countNonZero(mask_brown)
    porcentaje_brown = (brown_pixels / total_pixels) * 100

    # Clasificación
    if porcentaje_brown < .5:
        estado = "🍐 Pera fresca"
    elif porcentaje_brown < 20:
        estado = "🍐 Pera en proceso de pudrirse"
    else:
        estado = "🍐 Pera podrida"

    # Visualización
    mask_rgb = cv2.applyColorMap(mask_brown, cv2.COLORMAP_HOT)
    blended = cv2.addWeighted(img_rgb, 0.7, mask_rgb, 0.5, 0)

    plt.subplot(1, 2, 2)
    plt.imshow(blended)
    plt.title(f"{estado}\nÁrea café: {porcentaje_brown:.2f}%")
    plt.axis("off")

    plt.show()

    # Resultados
    print(f"Área café: {brown_pixels} píxeles ({porcentaje_brown:.2f}%)")
    print("Clasificación final:", estado)

