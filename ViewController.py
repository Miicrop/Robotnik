from tkinter import Listbox, END
import customtkinter

from RobotController import RobotController     

class ViewController:
    def __init__(self, view):
        self.view = view
        self.robot_controller = RobotController()
        
        self.filename = "program.json"
        #ToDo: self.robot_controller.program_controller.current_index should be implemented in RobotController somehow
        
        self.bind_program_buttons()
        self.bind_joint_buttons()
        self.bind_tool_and_speed_buttons()
        self.bind_command_buttons()
        self.update_listbox()
    
    
        
    def bind_program_buttons(self):
        self.view.button_new_program.configure(
            command=lambda: (self.robot_controller.new_program(), self.update_listbox())
            )
        self.view.button_save_program.configure(
            command=lambda: self.robot_controller.save_program(self.filename)
            )
        self.view.button_load_program.configure(
            command=lambda: (self.robot_controller.load_progam(self.filename), self.update_listbox())
            )
        self.view.button_move_command_upwards.configure(
            command=self.move_listbox_item_up
            )
        self.view.button_move_command_downwards.configure(
            command=self.move_listbox_item_down
            )
        self.view.button_delete_command.configure(
            command=self.delete_listbox_entry
        )
        self.view.button_connect.configure(
            command=self.robot_controller.connect
            )
        
    def bind_joint_buttons(self):
        self.view.button_a1_decrease.bind('<ButtonPress-1>', lambda event: self.robot_controller.move_joint_negative(0))
        self.view.button_a2_decrease.bind('<ButtonPress-1>', lambda event: self.robot_controller.move_joint_negative(1))
        self.view.button_a3_decrease.bind('<ButtonPress-1>', lambda event: self.robot_controller.move_joint_negative(2))
        self.view.button_a4_decrease.bind('<ButtonPress-1>', lambda event: self.robot_controller.move_joint_negative(3))
        self.view.button_a5_decrease.bind('<ButtonPress-1>', lambda event: self.robot_controller.move_joint_negative(4))
        self.view.button_a6_decrease.bind('<ButtonPress-1>', lambda event: self.robot_controller.move_joint_negative(5))
        
        self.view.button_a1_increase.bind('<ButtonPress-1>', lambda event: self.robot_controller.move_joint_positive(0))
        self.view.button_a2_increase.bind('<ButtonPress-1>', lambda event: self.robot_controller.move_joint_positive(1))
        self.view.button_a3_increase.bind('<ButtonPress-1>', lambda event: self.robot_controller.move_joint_positive(2))
        self.view.button_a4_increase.bind('<ButtonPress-1>', lambda event: self.robot_controller.move_joint_positive(3))
        self.view.button_a5_increase.bind('<ButtonPress-1>', lambda event: self.robot_controller.move_joint_positive(4))
        self.view.button_a6_increase.bind('<ButtonPress-1>', lambda event: self.robot_controller.move_joint_positive(5))
        
        
        self.view.button_a1_decrease.bind('<ButtonRelease-1>', lambda event: self.robot_controller.stop_joint(0))
        self.view.button_a2_decrease.bind('<ButtonRelease-1>', lambda event: self.robot_controller.stop_joint(1))
        self.view.button_a3_decrease.bind('<ButtonRelease-1>', lambda event: self.robot_controller.stop_joint(2))
        self.view.button_a4_decrease.bind('<ButtonRelease-1>', lambda event: self.robot_controller.stop_joint(3))
        self.view.button_a5_decrease.bind('<ButtonRelease-1>', lambda event: self.robot_controller.stop_joint(4))
        self.view.button_a6_decrease.bind('<ButtonRelease-1>', lambda event: self.robot_controller.stop_joint(5))

        self.view.button_a1_increase.bind('<ButtonRelease-1>', lambda event: self.robot_controller.stop_joint(0))
        self.view.button_a2_increase.bind('<ButtonRelease-1>', lambda event: self.robot_controller.stop_joint(1))
        self.view.button_a3_increase.bind('<ButtonRelease-1>', lambda event: self.robot_controller.stop_joint(2))
        self.view.button_a4_increase.bind('<ButtonRelease-1>', lambda event: self.robot_controller.stop_joint(3))
        self.view.button_a5_increase.bind('<ButtonRelease-1>', lambda event: self.robot_controller.stop_joint(4))
        self.view.button_a6_increase.bind('<ButtonRelease-1>', lambda event: self.robot_controller.stop_joint(5))
        
    def bind_tool_and_speed_buttons(self):
        self.view.button_tool_activate.configure(command=self.robot_controller.activate_tool)
        self.view.button_tool_deactivate.configure(command=self.robot_controller.deactivate_tool)
        self.view.button_speed_decrease.configure(command=self.robot_controller.decrease_speed)
        self.view.button_speed_increase.configure(command=self.robot_controller.increase_speed)
        
    def bind_command_buttons(self):
        self.view.button_prev_step.configure(
            command=self.robot_controller.previous_program_step
            )
        self.view.button_next_step.configure(
            command=self.robot_controller.next_program_step
            )
        self.view.button_start.configure(
            command=self.robot_controller.start_program
            )
        self.view.button_stop.configure(
            command=self.robot_controller.stop_program
            )
        
        self.view.button_tool_command_active.configure(
            command=lambda: (self.robot_controller.add_tool_active_command(), self.update_listbox())
            )
        self.view.button_tool_command_inactive.configure(
            command=lambda: (self.robot_controller.add_tool_inactive_command(), self.update_listbox())
            )
        self.view.button_lin.configure(
            command=lambda: (self.robot_controller.add_lin_command(), self.update_listbox())
            )
        self.view.button_ptp.configure(
            command=lambda: (self.robot_controller.add_ptp_command(), self.update_listbox())
            )
        
        
    def update_listbox_cursor(self):
        self.view.listbox.selection_set(self.robot_controller.get_program_index())
        self.view.listbox.activate(self.robot_controller.get_program_index())
    
    def get_listbox_index(self):
        selected_index = self.view.listbox.curselection()
        if selected_index:
            self.robot_controller.set_program_index(selected_index[0])
            return selected_index[0]
    
    def update_listbox(self):
        self.clear_listbox()
        for idx, program in enumerate(self.robot_controller.program_controller.program):
            self.view.listbox.insert(idx, program.to_string())
            
    def clear_listbox(self):
        self.view.listbox.delete(0, END)
            
    def move_listbox_item_up(self):
        index = self.get_listbox_index()
        self.robot_controller.move_command_up(index)
        self.robot_controller.set_program_index(index - 1)
        self.update_listbox()
        self.update_listbox_cursor()
        
    def move_listbox_item_down(self):
        index = self.get_listbox_index()
        self.robot_controller.move_command_down(index)
        self.robot_controller.set_program_index(index + 1)
        self.update_listbox()
        self.update_listbox_cursor()
        
    def delete_listbox_entry(self):
        index = self.get_listbox_index()
        self.robot_controller.delete_command(index)
        self.update_listbox()
        self.update_listbox_cursor()
        