import cv2

if __name__ == "__main__":
    
 # Leitura da imagem em escala de cinza
 img = cv2.imread(in_file("teste3.pbm"), cv2.IMREAD_GRAYSCALE)
 cv2.imshow("Imagem original", img)
 print(f"Dimensoes da imagem: {img.shape}")


 # Binarização da imagem (inverte as cores e ajusta para preto e branco)
 img_bin = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV)[1]
 cv2.imshow("Imagem binarizada", img_bin)
 
 # Aplica um filtro gaussiano com kernel de tamanho 5 e desvio padrão de 0
 img_suave = cv2.GaussianBlur(img_bin, (5, 5), 0)
 cv2.imshow("Imagem suavizada", img_suave)

 # Detecção dos contornos dos objetos na imagem binarizada
 contornos, _ = cv2.findContours(img_suave, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
 print(f"Total de contornos encontrados: {len(contornos)}")
 
 # Contagem do total de objetos e objetos com furos
 total_objetos = 0
 objetos_com_furos = -1
 
 for contorno in contornos:
     x, y, w, h = cv2.boundingRect(contorno)
     # Contagem do número de buracos preenchidos
     buracos_preenchidos = 0
     for i in range(x, x + w):
        for j in range(y, y + h):
               if img_suave[j, i] == 0:
                vizinhos = img_suave[j-1:j+2, i-1:i+2]
                if (vizinhos).sum() == 0:
                    buracos_preenchidos += 1
                
     
     # Verificação se o objeto tem furos ou não
     if buracos_preenchidos > 0:
        objetos_com_furos += 1
        
     total_objetos += 1
     
 # Impressão dos resultados
 print("Total de objetos: ", total_objetos)
 print("Objetos sem furos: ", total_objetos - objetos_com_furos)
 print("Objetos com furos: ", objetos_com_furos)
 
 cv2.waitKey(0)
 cv2.destroyAllWindows()
