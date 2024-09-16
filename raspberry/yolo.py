import os
import bluetooth
from ultralytics import YOLO
from picamera2 import Picamera2
from PIL import Image
import time
import threading
import subprocess

def enable_bluetooth_discoverable():
    try:
        subprocess.run(['sudo', 'bluetoothctl', 'power', 'on'], check=True)
        subprocess.run(['sudo', 'bluetoothctl', 'discoverable', 'on'], check=True)
        print("Raspberry Pi est maintenant détectable en Bluetooth.")
   
    except subprocess.CalledProcessError as e:
        print(f"Une erreur est survenue : {e}")

def initialize_camera():
    while True:
        try:
            picam2 = Picamera2()
            picam2.preview_configuration.main.size = (1280, 720)
            picam2.preview_configuration.main.format = "RGB888"
            picam2.preview_configuration.align()
            picam2.configure("preview")
            picam2.start()
            return picam2

        except Exception as e:
            print(f"Erreur lors de l'initialisation de la caméra : {e}")
            time.sleep(1)

def detect_objects(client_sock, picam2, model, detection_active):
    output_folder = "images"
    os.makedirs(output_folder, exist_ok=True)
    image_counter = 0
    try:
        while detection_active.is_set():
            frame = picam2.capture_array()
            results = model(frame, conf=0.8)

            annotated_frame = results[0].plot()
            annotated_image = Image.fromarray(annotated_frame)
            image_path = os.path.join(output_folder, f"image_{image_counter}.jpg")
            annotated_image.save(image_path)
            image_counter += 1
           
            for result in results:
                boxes = result.boxes
                for box in boxes:
                    x1, y1, x2, y2 = box.xyxy[0]  
                    class_id = int(box.cls[0])  
                    label = model.names[class_id]  
                    box_height = y2 - y1  
                    focal_length = 1000
                    real_height = 0.45  
                    distance = (focal_length * real_height) / box_height
                    print(f"{label} détecté a "+str(distance)+" m" )

                    if 2.5 > distance > 1.5:
                        try:
                            if label == "poubelles":
                                label = "poubelle"
                            client_sock.send(f"{label} à 2 mètre \n")
                        except Exception as e:
                            print(f"Erreur dans l'envoi de l'alerte: {e}")
                            detection_active.clear()
                            return  
                    elif 1 > distance:
                        try:
                            if label == "poubelles":
                                label = "poubelle"
                            client_sock.send(f"{label} à moins de 1 mètre \n")
                        except Exception as e:
                            print(f"Erreur dans l'envoi de l'alerte: {e}")
                            detection_active.clear()  
                            return  
                           
                    elif distance>5:
                        try:
                            if label == "poubelles":
                                label = "poubelle"
                            client_sock.send(f"{label} à plus de 5 mètre \n")
                        except Exception as e:
                            print(f"Erreur dans l'envoi de l'alerte: {e}")
                            detection_active.clear()
                            return  
            #time.sleep(0.1)
    except Exception as e:
        print(f"Erreur avec la caméra: {e}")
        print("Réinitialisation de la caméra...")
        picam2.close()  
        time.sleep(1)  
        picam2 = initialize_camera()
    finally:
        detection_active.clear()  

def main():
    enable_bluetooth_discoverable()
    picam2 = initialize_camera()
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_sock.bind(("", bluetooth.PORT_ANY))
    server_sock.listen(1)
    port = server_sock.getsockname()[1]
    print(f"Listening on port {port}")
    model = YOLO("1209.pt")
    while True:
        print("En attente d'une nouvelle connexion Bluetooth...")
        client_sock, client_info = server_sock.accept()
        print(f"Accepted connection from {client_info}")

        detection_active = threading.Event()

        try:
            while True:
                data = client_sock.recv(1024)
                if len(data) == 0:
                    break

                message = data.decode('utf-8').strip()
                print(f"Received: {message}")

                if message == "start":
                    if not detection_active.is_set():
                        print("Starting object detection...")
                        detection_active.set()
                        detection_thread = threading.Thread(target=detect_objects, args=(client_sock, picam2, model, detection_active))
                        detection_thread.start()
                    else:
                        print("Object detection already active.")
                elif message == "stop":
                    if detection_active.is_set():
                        print("Stopping object detection...")
                        detection_active.clear()
                    else:
                        print("Object detection is not active.")
                else:
                    print(f"Unknown message received: {message}")
                   
        except OSError:
            print("Connexion interrompue.")

        print("Client déconnecté.")
        client_sock.close()

if __name__ == "__main__":
    main()
