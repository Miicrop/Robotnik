import serial
import time
import threading

class SerialController:
    def __init__(self, port="COM4", baudrate=115200):
        self.serial_thread = None
        self.arduino = None
        self.port = port
        self.baudrate = baudrate
    
    def connect(self):
        try:
            self.arduino = serial.Serial(self.port, self.baudrate)
            time.sleep(1)
            print("  >>  Arduino Connection successful")
            self.start_serial_thread()
        except:
            print("  >>  Arduino Connection failed")            
    
    def read_serial(self):
        while self.arduino and self.arduino.is_open:
            try:
                line = self.arduino.readline().decode("utf-8").strip()
                if line:
                    print(f"  >>  Serial:: {line}")
                    
            except serial.SerialException as e:
                print(f"  >>  Serial:: Error:: {e}")
                break

    def start_serial_thread(self):
        if not self.arduino or not self.arduino.is_open:
            print("  >>  Serial:: Thread:: No active serial connection.")
            return
        
        if not self.serial_thread or not self.serial_thread.is_alive():
            self.serial_thread = threading.Thread(target=self.read_serial, daemon=True)
            self.serial_thread.start()
            print("  >>  Serial:: Thread started.")
        else:
            print("  >>  Serial:: Thread already running.")
        
    def send_serial(self, prefix, value):
        command = f"{prefix}:{value}\n"
        self.arduino.write(bytes(command), "utf-8")