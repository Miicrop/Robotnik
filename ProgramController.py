import json


class Command:
    def execute(self):
        raise NotImplementedError("Child Classes should implement this function")
        
class HomeCommand(Command):
    def __init__(self):
        self.name = "HOME"
    
    def execute(self):
        pass
        
class LinCommand(Command):
    def __init__(self, position):
        self.name = "LIN"
        self.position = position
        
    def execute(self):
        pass
    
class PtpCommand(Command):
    def __init__(self, position):
        self.name = "PTP"
        self.position = position
        
    def execute(self):
        pass
    
class ToolCommand(Command):
    def __init__(self, action):
        self.name = "TOOL"
        self.action = action

    def execute(self):
        pass
    


class RobotProgram:
    def __init__(self):
        self.is_running = False
        self.current_index = 0
        self.program = [HomeCommand(), HomeCommand()]
        
    def new_program(self):
        self.program = [HomeCommand(), HomeCommand()]
        
    def save_program(self, filename):
        program_data = []
        for cmd in self.program:
            program_data.append(
                {
                "type": cmd.__class__.__name__,
                "params": vars(cmd)
                }
            )
            
        with open(filename, "w") as f:
            json.dump(program_data, f, indent=4)
        print("  >>  Program saved")
        
    def load_program(self, filename):
        with open(filename, "r") as f:
            program_data = json.load(f)
        
        self.program = [self.create_command(data) for data in program_data]
        print("  >>  Program loaded")
        
    def add_command(self, command):
        self.program.insert(-1, command)
        
    def create_command_from_json(self, data):
        type = data["type"]
        params = data["params"]
        
        if type == "HomeCommand":
            return HomeCommand()
        
        elif type == "LinCommand":
            return LinCommand(params["position"])
        
        elif type == "PtpCommand":
            return PtpCommand(params["position"])
        
        elif type == "ToolCommand":
            return ToolCommand(params["action"])
        
    def move_command_up(self, index):
        target_index = index - 1
        if target_index <= 0:
            print("  >>  Could not move command out of Bounds")
            return
        self.program[index], self.program[target_index] = self.program[target_index], self.program[index]
        
    def move_command_down(self, index):
        target_index = index + 1
        if target_index >= len(self.program):
            print("  >>  Could not move command out of Bounds")
            return
        self.program[index], self.program[target_index] = self.program[target_index], self.program[index]
        
    def start_program(self, index=None):
        self.is_running = True
        print("  >>  Program started")
        
        if index is None:
            for command in self.program:
                command.execute()
                self.current_index += 1
        
        elif isinstance(index, int) and 0 <= index < len(self.program):
            self.current_index = index
            while self.current_index < len(self.program):
                current_command = self.program[self.current_index]
                current_command.execute()
                self.current_index += 1            
        
    def stop_program(self):
        self.is_running = False
        #! Logic for how to stop here?
        
    def next_program_step(self):
        self.running = True
        if self.current_index < len(self.program):
            current_command = self.program[self.current_index]
            current_command.execute()
            self.current_index += 1
        self.running = False  #! get callback somewhere is current command is done executing, or handle this in the final controller
        
    def previous_program_step(self):
        self.running = True
        if self.current_index > 0:
            current_command = self.program[self.current_index]
            current_command.execute()
            self.current_index += 1
        self.running = False  #! get callback somewhere is current command is done executing, or handle this in the final controller
        
        