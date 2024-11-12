import SerialController
import SpeedController
import ProgramController

class Robot:
    def __init__(self):
        self.serial_controller = SerialController()
        self.speed_controller = SpeedController()
        self.program_controller = ProgramController()
    
    def connect(self):
        self.serial_controller.connect()
    
    def increase_speed(self):
        self.speed_controller.increase_speed()
        self.serial_controller.send_serial("SPEED", self.speed_controller.get_speed())
    
    def decrease_speed(self):
        self.speed_controller.decrease_speed()
        self.serial_controller.send_serial("SPEED", self.speed_controller.get_speed())