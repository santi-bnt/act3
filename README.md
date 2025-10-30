Requisitos: Python 3.8+


Instalación: crear (opcional) un entorno virtual, activarlo y ejecutar: pip install opencv-python numpy matplotlib


Librerías usadas:


OpenCV (cv2): cvtColor, inRange, bitwise_or, countNonZero


NumPy (np): array para definir umbrales HSV


Matplotlib (plt): figure, imshow, title, axis("off")




Uso mínimo: cargar la imagen con OpenCV, pasar el arreglo a tu función y visualizar con Matplotlib.


Notas rápidas: si aparece el error de cvtColor por “_src.empty()”, la imagen no se cargó (revisa ruta/nombre). Si los colores se ven raros al mostrar, convierte BGR→RGB al visualizar con Matplotlib usando cv2.cvtColor(..., COLOR_BGR2RGB).

