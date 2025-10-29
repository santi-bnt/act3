import cv2
import numpy as np
import matplotlib.pyplot as plt


manzana_n = cv2.imread("manzana.jpg")
manzana_p = cv2.imread("manzana_podrida.jpg")
manzana_np = cv2.imread("manzana_not_fresh.jpg")

#Definimos el rango para rojo podrido
rojo_podrido_bajo = np.array([6, 100, 90], np.uint8)
rojo_podrido_alto = np.array([19, 225, 240], np.uint8)

#Definimos 2 ranbgos para normal para mejor deteccion
rojo_normal_bajo  = np.array([ 0, 120, 120], np.uint8)
rojo_normal_alto  = np.array([12, 255, 255], np.uint8)

rojo_normal_bajo_2 = np.array([170, 120, 120], np.uint8)
rojo_normal_alto_2 = np.array([180, 255, 255], np.uint8)

#Definimos el rango para rojo casi podrido
rojo_casi_podrido_bajo = np.array([ 6, 145, 155], np.uint8)
rojo_casi_podrido_alto = np.array([22, 245, 255], np.uint8)




def detectar_manzana(manzana):

    manzana = cv2.cvtColor(manzana, cv2.COLOR_BGR2HSV)
#Hacemos todas las mascaras
    mask_normal1 = cv2.inRange(manzana, rojo_normal_bajo, rojo_normal_alto)
    mask_normal2 = cv2.inRange(manzana, rojo_normal_bajo_2, rojo_normal_alto_2)
    mask_podrido = cv2.inRange(manzana, rojo_podrido_bajo, rojo_podrido_alto)
    mask_normal = cv2.bitwise_or(mask_normal1,mask_normal2)
    mask_casi = cv2.inRange(manzana, rojo_casi_podrido_bajo, rojo_casi_podrido_alto)
  
#se genera una matriz de 0 y se compara con la mascara contando cuantos pixeles no son 0
    count_podrido = cv2.countNonZero(mask_podrido)
    count_normal = cv2.countNonZero(mask_normal)
    count_casi = cv2.countNonZero(mask_casi)
    
#con max busca cual es el numero mas grande y lo guarda 
    max_color = max(count_podrido, count_normal, count_casi)
    if max_color == count_podrido:
        estado = "Podrida"
    elif max_color == count_casi:
        estado = "Casi podrida"
    else:
        estado = "Normal"

    return estado


estado_n  = detectar_manzana(manzana_n)
estado_p  = detectar_manzana(manzana_p)
estado_np = detectar_manzana(manzana_np)


manzana_n_rgb  = cv2.cvtColor(manzana_n, cv2.COLOR_BGR2RGB)
manzana_p_rgb  = cv2.cvtColor(manzana_p, cv2.COLOR_BGR2RGB)
manzana_np_rgb = cv2.cvtColor(manzana_np, cv2.COLOR_BGR2RGB)

plt.figure()
plt.subplot(3,4,1)
plt.imshow(manzana_n_rgb)
plt.title(f"Estado: {estado_n}")
plt.axis("off")

plt.subplot(3,4,2)
plt.imshow(manzana_p_rgb)
plt.title(f"Estado: {estado_p}")
plt.axis("off")

plt.subplot(3,4,3)
plt.imshow(manzana_np_rgb)
plt.title(f"Estado: {estado_np}")
plt.axis("off")
plt.show()
