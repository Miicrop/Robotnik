from tkinter import Listbox, END
import customtkinter

class ViewController:
    def __init__(self, view):
        self.view = view
        self.counter = 0
        
        self.bind_program_buttons()
        self.bind_joint_buttons()
        self.bind_tool_and_speed_buttons()
        self.bind_command_buttons()
    
    def test(self):
        print(self.counter)
        self.counter += 1
        
    def bind_program_buttons(self):
        self.view.button_new_program.configure(command=self.test)
        self.view.button_save_program.configure(command=self.test)
        self.view.button_load_program.configure(command=self.test)
        self.view.button_move_command_upwards.configure(command=self.test)
        self.view.button_move_command_downwards.configure(command=self.test)
        self.view.button_connect.configure(command=self.test)
        
    def bind_joint_buttons(self):
        self.view.button_a1_decrease.bind('<ButtonPress-1>', lambda event: self.control_motor("I", 0))
        self.view.button_a2_decrease.bind('<ButtonPress-1>', lambda event: self.control_motor("I", 1))
        self.view.button_a3_decrease.bind('<ButtonPress-1>', lambda event: self.control_motor("I", 2))
        self.view.button_a4_decrease.bind('<ButtonPress-1>', lambda event: self.control_motor("I", 3))
        self.view.button_a5_decrease.bind('<ButtonPress-1>', lambda event: self.control_motor("I", 4))
        self.view.button_a6_decrease.bind('<ButtonPress-1>', lambda event: self.control_motor("I", 5))
        
        self.view.button_a1_decrease.bind('<ButtonRelease-1>', lambda event: self.stop_motor(0))
        self.view.button_a2_decrease.bind('<ButtonRelease-1>', lambda event: self.stop_motor(1))
        self.view.button_a3_decrease.bind('<ButtonRelease-1>', lambda event: self.stop_motor(2))
        self.view.button_a4_decrease.bind('<ButtonRelease-1>', lambda event: self.stop_motor(3))
        self.view.button_a5_decrease.bind('<ButtonRelease-1>', lambda event: self.stop_motor(4))
        self.view.button_a6_decrease.bind('<ButtonRelease-1>', lambda event: self.stop_motor(5))
        
        self.view.button_a1_increase.bind('<ButtonPress-1>', lambda event: self.stop_motor(0))
        self.view.button_a2_increase.bind('<ButtonPress-1>', lambda event: self.stop_motor(1))
        self.view.button_a3_increase.bind('<ButtonPress-1>', lambda event: self.stop_motor(2))
        self.view.button_a4_increase.bind('<ButtonPress-1>', lambda event: self.stop_motor(3))
        self.view.button_a5_increase.bind('<ButtonPress-1>', lambda event: self.stop_motor(4))
        self.view.button_a6_increase.bind('<ButtonPress-1>', lambda event: self.stop_motor(5))
        
        self.view.button_a1_decrease.bind('<ButtonRelease-1>', lambda event: self.stop_motor(0))
        self.view.button_a2_decrease.bind('<ButtonRelease-1>', lambda event: self.stop_motor(1))
        self.view.button_a3_decrease.bind('<ButtonRelease-1>', lambda event: self.stop_motor(2))
        self.view.button_a4_decrease.bind('<ButtonRelease-1>', lambda event: self.stop_motor(3))
        self.view.button_a5_decrease.bind('<ButtonRelease-1>', lambda event: self.stop_motor(4))
        self.view.button_a6_decrease.bind('<ButtonRelease-1>', lambda event: self.stop_motor(5))
        
    def bind_tool_and_speed_buttons(self):
        self.view.button_tool_activate.configure(command=self.test)
        self.view.button_tool_deactivate.configure(command=self.test)
        self.view.button_speed_decrease.configure(command=self.test)
        self.view.button_speed_increase.configure(command=self.test)
        
    def bind_command_buttons(self):
        self.button_prev_step.configure(command=self.test)
        self.button_next_step.configure(command=self.test)
        self.button_start.configure(command=self.test)
        self.button_stop.configure(command=self.test)
        self.button_tool_command_active.configure(command=self.test)
        self.button_tool_command_inactive.configure(command=self.test)
        self.button_lin.configure(command=self.test)
        self.button_ptp.configure(command=self.test)