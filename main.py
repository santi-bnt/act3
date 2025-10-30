#Pera results
img = 'pera_fresca.jpg'
pera(img)

img2 = 'image.png'
pera(img2)

img3 = 'pera_3.jpg'
pera(img3)

#manzana results
manzana_n  = cv2.imread("manzana.jpg")
manzana_np = cv2.imread("manzana_not_fresh.jpg")
manzana_p  = cv2.imread("manzana_podrida.jpg")

detectar_manzana(manzana_n)
detectar_manzana(manzana_np)
detectar_manzana(manzana_p)
