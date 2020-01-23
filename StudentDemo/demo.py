import threading
import AvacomControl as avacom
import lampControl as lamp

cameraIP = "192.168.1.116"
lampIP = "192.168.1.104"
panCt = 2
def pan():
    camera = avacom.accessAvacomWebPortal(cameraIP)
    for i in range(panCt):
        avacom.avacomHorizPan(camera, 5)
        avacom.avacomVertPan(camera, 5)
    camera.close

def main():
    lampThread = threading.Thread(target = lamp.strobeLight, args = (lampIP, 10))
    cameraThread = threading.Thread(target = pan, args = ())
    
    cameraThread.start()
    lampThread.start()
    
    cameraThread.join(5)
    lampThread.join(5)
    

    

   

main()
