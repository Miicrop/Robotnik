class SpeedController:
    def __init__(self):
        self.max_speed = 2000
        self.valid_speeds = [1, 3, 5, 10, 30, 50, 100]
        self.speed = 100
        
    def get_speed(self):
        return self.max_speed * self.speed / 100
        
    def set_speed(self, new_speed):
        if new_speed in self.valid_speeds:
            self.speed = new_speed
            print(f"  >>  set new speed: {self.speed}")
        else:
            raise ValueError("Wrong Speed Percentage")
        
    def increase_speed(self):
        index = self.valid_speeds.index(self.speed)
        if index < len(self.valid_speeds) - 1:
            self.set_speed(self.valid_speeds[index + 1])
            
    def decrease_speed(self):
        index = self.valid_speeds.index(self.speed)
        if index > 0:
            self.set_speed(self.valid_speeds[index - 1])