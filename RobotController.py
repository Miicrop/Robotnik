from Robot import Robot
from SerialController import SerialController
from SpeedController import SpeedController
import ProgramController

class RobotController:
    def __init__(self):
        self.robot = Robot()
        self.serial_controller = SerialController(data_callback=self.get_steps_from_serial)
        self.speed_controller = SpeedController()
        self.program_controller = ProgramController.RobotProgram()
    
    def connect(self):
        self.serial_controller.connect()
    
    def increase_speed(self):
        self.speed_controller.increase_speed()
        self.serial_controller.send_serial("SPEED", self.speed_controller.get_speed())
    
    def decrease_speed(self):
        self.speed_controller.decrease_speed()
        self.serial_controller.send_serial("SPEED", self.speed_controller.get_speed())
        
    def activate_tool(self):
        self.serial_controller.send_serial("TOOL", "active")
        
    def deactivate_tool(self):
        self.serial_controller.send_serial("TOOL", "inactive")
    
    def get_program_index(self):
        return self.program_controller.program_index
    
    def set_program_index(self, index):
        self.program_controller.program_index = index
        
    def new_program(self):
        self.program_controller.new_program()
        
    def save_program(self, filename):
        self.program_controller.save_program(filename)
        
    def load_progam(self, filename):
        self.program_controller.load_program(filename)
        
    def move_command_up(self, index):
        self.program_controller.move_command_up(index)
    
    def move_command_down(self, index):
        self.program_controller.move_command_down(index)
        
    def delete_command(self, index):
        self.program_controller.delete_command(index)
        
    def start_program(self):
        self.program_controller.start_program()
        
    def stop_program(self):
        self.program_controller.stop_program()  
        
    def previous_program_step(self):
        self.program_controller.previous_program_step()
        
    def next_program_step(self):
        self.program_controller.next_program_step()
           
    def add_lin_command(self):
        position, orientation = self.robot.get_current_pose()
        self.program_controller.add_command(
            ProgramController.LinCommand(
                position=position,
                orientation=orientation
            ))

    def add_ptp_command(self):
        position, orientation = self.robot.get_current_pose()
        self.program_controller.add_command(
            ProgramController.PtpCommand(
                position=position,
                orientation=orientation
            ))
        
    def add_tool_active_command(self):
        self.program_controller.add_command(
            ProgramController.ToolCommand(
                is_active=True
            )
        )
        
    def add_tool_inactive_command(self):
        self.program_controller.add_command(
            ProgramController.ToolCommand(
                is_active=False
            )
        )
        
    def get_steps_from_serial(self, data):
        motor_steps = data.strip(",").split(",")
        for steps in motor_steps:
            joint, step = steps.split(":")
            joint = int(joint)
            step = int(step)
            
        #! ToDo: finish logic
        
        
    def move_joint_positive(self, joint):
        self.serial_controller.send_serial("JP", joint)
        
    def move_joint_negative(self, joint):
        self.serial_controller.send_serial("JN", joint)
        
    def stop_joint(self, joint):
        self.serial_controller.send_serial("STOP", joint)