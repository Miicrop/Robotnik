import json
import numpy as np
import time


class Command:
    def __init__(self):
        self.process_complete = False
        
    def execute(self):
        raise NotImplementedError("Child Classes should implement this function")
    
    def to_string(self):
        raise NotImplementedError("Child Classes should implement this function")
    
    def reset(self):
        self.process_complete = False
    
    
        
class HomeCommand(Command):
    def __init__(self):
        super().__init__()
        self.name = "HOME"
    
    def execute(self):
        print("HOME started")
        #! Logic here
        self.process_complete = True
        
    def to_string(self):
        return f"{self.name}"
        
        
class LinCommand(Command):
    def __init__(self, position, orientation):
        super().__init__()
        self.name = "LIN"
        self.position = position
        self.orientation = orientation

    def execute(self):
        print("LIN")
        #! Logic here
        self.process_complete = True
        
    def to_string(self):
        return f"{self.name} :: {self.position} :: {self.orientation}"
        
    
class PtpCommand(Command):
    def __init__(self, position, orientation):
        super().__init__()
        self.name = "PTP"
        self.position = position
        self.orientation = orientation
        
    def execute(self):
        print("PTP")
        #! Logic here
        self.process_complete = True
        
    def to_string(self):
        return f"{self.name} :: {self.position} :: {self.orientation}"
        
    
class ToolCommand(Command):
    def __init__(self, is_active):
        super().__init__()
        self.name = "TOOL"
        self.is_active = is_active

    def execute(self):
        print("TOOL")
        #! Logic here
        self.process_complete = True
        
    def to_string(self):
        return f"{self.name} :: {self.is_active}"
        
    


class RobotProgram:
    def __init__(self):
        self.is_running = False
        self.running_index = 0
        self.program_index = 0
        self.program = [HomeCommand(), HomeCommand()]
        
    def new_program(self):
        self.program = [HomeCommand(), HomeCommand()]
        
    def save_program(self, filename):
        program_data = []
        for cmd in self.program:
            program_data.append({
                "type": cmd.__class__.__name__,
                "params": self.command_to_dict(cmd)
            })
            
        with open(filename, "w") as f:
            json.dump(program_data, f, indent=4)
        print("  >>  Program saved")
        
    def load_program(self, filename):
        with open(filename, "r") as f:
            program_data = json.load(f)
        
        self.program = [self.create_command_from_json(data) for data in program_data]
        print("  >>  Program loaded")
        
    def delete_command(self, index):
        self.program.pop(index)
        
    def add_command(self, command):
        self.program.insert(-1, command)
        
    def command_to_dict(self, cmd):
        """Serialisiert das Command-Objekt zu einem Dictionary für JSON"""
        data = {
            "name": cmd.name,
        }
        if isinstance(cmd, LinCommand) or isinstance(cmd, PtpCommand):
            data["position"] = cmd.position.tolist()
            data["orientation"] = cmd.orientation.tolist()
        if isinstance(cmd, ToolCommand):
            data["is_active"] = cmd.is_active
        return data
        
    def create_command_from_json(self, data):
        type = data["type"]
        params = data["params"]
        
        if type == "HomeCommand":
            return HomeCommand()
        
        elif type == "LinCommand":
            position = np.array(params["position"])
            orientation = np.array(params["orientation"])
            return LinCommand(position, orientation)
        
        elif type == "PtpCommand":
            position = np.array(params["position"])
            orientation = np.array(params["orientation"])
            return PtpCommand(position, orientation)
        
        elif type == "ToolCommand":
            return ToolCommand(params["is_active"])
        
    def move_command_up(self, index):
        target_index = index - 1
        if target_index < 0:
            return
        self.program[index], self.program[target_index] = self.program[target_index], self.program[index]
        
    def move_command_down(self, index):
        target_index = index + 1
        if target_index > len(self.program):
            return
        self.program[index], self.program[target_index] = self.program[target_index], self.program[index]
        
    def start_program(self):
        print("  >>  Program started")
        self.is_running = True
        self.running_index = 0
        
        while self.is_running and self.running_index < len(self.program):
            current_command = self.program[self.running_index]
            
            if current_command.process_complete == False:
                current_command.execute()
                
            if current_command.process_complete == True:
                self.running_index += 1
                current_command.reset()
                
            time.sleep(0.1)
            
        self.stop_program()
        
    def stop_program(self):
        print("  >>  Program stopped")
        self.is_running = False
        
    def next_program_step(self):
        if self.running_index <= len(self.program) - 1:
            current_command = self.program[self.running_index]
            current_command.execute()
            self.running_index += 1
        
    def previous_program_step(self):
        if self.running_index > 0:
            current_command = self.program[self.running_index - 1]
            current_command.execute()
            self.running_index -= 1