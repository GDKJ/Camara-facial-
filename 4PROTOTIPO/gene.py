from scipy.spatial import distance as dist
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils import face_utils
import imutils
import time
import dlib
import cv2
from urllib.request import urlopen 
import paho.mqtt.client as mqtt
import time
import threading





def ante_conexion_exitosa(client,userdata,flags, rc):
  print("CONECTADO")
  client.subscribe("Press/01")

def ante_llegada_mensaje(client,userdata,msg):
  mensaj=(str(msg.payload))
  t=time.time()
  while (mensaj=="b'ACT'" and time.time()<t+3):
      import camara
      ret, frame = cap.read()
      print("EMERGENCIA")
      cv2.putText(frame, "EMERGENCIA", (100, 100),
         cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
      

cliente=mqtt.Client()
cliente.on_connect=ante_conexion_exitosa
cliente.on_message=ante_llegada_mensaje


cliente.username_pw_set("JUNIOR","12345")
cliente.connect("broker.emqx.io",1883,60)


     
def eye_aspect_ratio(eye):
# Calcula las distancias euclidianas entre los dos conjuntos de
# Señales verticales del ojo (x, y) -coordenadas
  A = dist.euclidean(eye[1], eye[5])
  B = dist.euclidean(eye[2], eye[4])
 
# Calcular la distancia euclidiana entre la horizontal
  C = dist.euclidean(eye[0], eye[3])
 
# calcula AR del ojo
  ear = (A + B) / (2.0 * C)
 
# devuelve AR del ojo
  return ear
 
 
EYE_AR_THRESH = 0.2


    

detector = dlib.get_frontal_face_detector()

#ARCHIVO DE ENTRENAMIENTO
PREDICTOR_PATH = "shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(PREDICTOR_PATH)
 
#se selecionan los indices del los ojos
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]


cap = cv2.VideoCapture('http://192.168.1.13:81/stream')
#cap=urlopen('http://192.168.1.11:81/stream')
fileStream = False
time.sleep(1.0)


 
# ciclo de procesado ppal

def camara():
    t=time.time()
    tout=time.time()
    count=0
    aux=0
    
    while True:
        
      
          
          
    # Si se trata de un archivo de flujo de vídeo, entonces tenemos que comprobar si
    # Hay más cuadros dejados en el búfer para procesar
    # Si fileStream y no vs.more ():
    # descanso
     
    # Agarrar el marco de la secuencia de archivo de vídeo de rosca, cambiar el tamaño
    # It, y convertirlo a escala de grises
    # Canales)
      ret, frame = cap.read()
      
      
      
    #frame = imutils.resize(frame, width=450)
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     
    # detecta caras en la imagen en escala de grises
      rects = detector(gray, 0)
     
    # ciclo sobre las detecciones de la cara
      for rect in rects:
    # Determina las marcas faciales para la región de la cara, luego
    # Convierte el punto de referencia facial (x, y) - a coordenada NumPy
    #Array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
     
    # Extrae las coordenadas de los ojos izquierdo y derecho y calcula
    # la relación de aspecto (AR) del ojo para ambos ojos
     
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]

        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
     
    # media de AR para los dos ojos
        ear = (leftEAR + rightEAR) / 2.0
     
    # hace la convex hull para los dos ojos
    # se dibujan los dos ojos
        leftEyeHull = cv2.convexHull(leftEye)
       
        rightEyeHull = cv2.convexHull(rightEye)
        
        
        cv2.drawContours(frame, [leftEyeHull], -1,(255, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (255, 255, 0), 1)
        

        

     
    # Compruebe si la relación de aspecto del ojo está por debajo del parpadeo
    #, Y si es así se incrementa el contador del marco intermitente
        if ear < EYE_AR_THRESH:
            
            if time.time()-t>=5:
                cv2.putText(frame, "DORMIDO", (70, 300),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                
                cv2.putText(frame, "ALARMA ACTIVADA!!!!", (155, 300),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
                cliente.publish("Press/01","ALARMA")
                
                aux=1

            
            cv2.putText(frame, "OJOS CERRADOS", (300, 30),
               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            

     
        else:
            
            if aux==1:
                count=count+1
                aux=0
            
            t=time.time()
            cv2.putText(frame, "OJOS ABIERTOS", (300, 30),
               cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            cliente.publish("Press/01","DESACT")
           
                
    #TIEMPO EXCEDIDO  
        if time.time()-tout>30:
            cv2.putText(frame, "TIEMPO OUT", (260, 70),
               cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 5)   
            

            
    #def for tests
            
        def ojos_cerrados(ear):
            if ear < EYE_AR_THRESH:
                return "Ojos cerrados"
            
        def ojos_abiertos(ear):
            if ear > EYE_AR_THRESH:
                return "Ojos abiertos"
            
        def ojos(ear):
            if ear < EYE_AR_THRESH:
                return " "

        def tiempo(tiemp):
            if tiemp>=5:
                return"Alarma activada"
            else:
                return" "
                
        def conteo_activacion(alarma):
            if alarma>=1:
                return(alarma)
            else:
                return ("La alarma no se activo")
        
        
      
    # mostramos el frame
      cv2.imshow("Frame", frame)
      key = cv2.waitKey(1) & 0xFF
     
    # si pulsa q se rompe el ciclo
      if key == ord("q"):
         cv2.putText(frame, "VECES QUE SONO LA ALARMA:", (340, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)
         print("VECES QUE SONO LA ALARMA:")
         print(count)
         if count==0:
             print("LA ALARMA NO SE ACTIVO.")
         break

    time.sleep(1.0) 
    # limpiamos un poco
    cap.release()
    cv2.destroyAllWindows()

def clienteloop():
    cliente.loop_start()
    key = cv2.waitKey(1) & 0xFF
   
    if key == ord("q"):
        cliente.loop_stop()



hilo1=camara()
hilo2=clienteloop()

hilo1.start()
hilo2.start()


