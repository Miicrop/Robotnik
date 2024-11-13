from tkinter import Listbox, END
import customtkinter

from ViewController import ViewController

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")


class RobotView(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Dr. Robotnik Control")
        self.geometry(f"{1200}x{580}")
        

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=0, minsize=240)
        self.grid_columnconfigure(2, weight=0, minsize=240)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        ###########################################################################################################################
        ##### FRAME: Left :: Program #####
        ###########################################################################################################################        
        self.frame_left = customtkinter.CTkFrame(self, corner_radius=10)
        self.frame_left.grid(row=0, column=0, rowspan=3, padx=(20, 0), pady=(10, 0), sticky="nsew")
        self.frame_left.grid_columnconfigure(0, weight=1)
        self.frame_left.grid_rowconfigure(3, weight=1)
        self.frame_left.grid_rowconfigure(7, weight=1)
        
        self.button_new_program = customtkinter.CTkButton(self.frame_left, text="New Program")
        self.button_save_program = customtkinter.CTkButton(self.frame_left, text="Save Program")
        self.button_load_program = customtkinter.CTkButton(self.frame_left, text="Load Program")
        self.button_move_command_upwards = customtkinter.CTkButton(self.frame_left, text="Move Command\nupwards", fg_color="#A633FF")
        self.button_move_command_downwards = customtkinter.CTkButton(self.frame_left, text="Move Command\ndownwards", fg_color="#A633FF")
        self.button_delete_command = customtkinter.CTkButton(self.frame_left, text="Delete Command", fg_color="#A633FF")
        self.button_connect = customtkinter.CTkButton(self.frame_left, text="Connect", width=80, fg_color="blue")
        
        self.button_new_program.grid(row=0, column=0, padx=20, pady=10)
        self.button_save_program.grid(row=1, column=0, padx=20, pady=10)
        self.button_load_program.grid(row=2, column=0, padx=20, pady=10)
        self.button_move_command_upwards.grid(row=4, column=0, padx=20, pady=10)
        self.button_move_command_downwards.grid(row=5, column=0, padx=20, pady=10)
        self.button_delete_command.grid(row=6, column=0, padx=20, pady=10)
        self.button_connect.grid(row=8, column=0, padx=20, pady=20)
        
        
        ###########################################################################################################################
        ##### FRAME: RIGHT :: Joints #####
        ###########################################################################################################################
        self.frame_right = customtkinter.CTkFrame(self, corner_radius=10)
        self.frame_right.grid(row=0, column=2, rowspan=4, padx=(0, 20), pady=(10, 10),sticky="nsew")
        self.frame_right.grid_rowconfigure(6, weight=1)
        self.frame_right.grid_rowconfigure(8, weight=1)
        self.frame_right.grid_columnconfigure((0,1,2), weight=1)

        self.button_a1_decrease = customtkinter.CTkButton(self.frame_right, text="-", fg_color="#A633FF", width=50)
        self.button_a2_decrease = customtkinter.CTkButton(self.frame_right, text="-", fg_color="#A633FF", width=50)
        self.button_a3_decrease = customtkinter.CTkButton(self.frame_right, text="-", fg_color="#A633FF", width=50)
        self.button_a4_decrease = customtkinter.CTkButton(self.frame_right, text="-", fg_color="#A633FF", width=50)
        self.button_a5_decrease = customtkinter.CTkButton(self.frame_right, text="-", fg_color="#A633FF", width=50)
        self.button_a6_decrease = customtkinter.CTkButton(self.frame_right, text="-", fg_color="#A633FF", width=50)
        self.button_a1_decrease.grid(row=0, column=0, padx=10, pady=15)
        self.button_a2_decrease.grid(row=1, column=0, padx=10, pady=15)
        self.button_a3_decrease.grid(row=2, column=0, padx=10, pady=15)
        self.button_a4_decrease.grid(row=3, column=0, padx=10, pady=15)
        self.button_a5_decrease.grid(row=4, column=0, padx=10, pady=15)
        self.button_a6_decrease.grid(row=5, column=0, padx=10, pady=15)
        
        self.button_a1_increase = customtkinter.CTkButton(self.frame_right, text="+", fg_color="#A633FF", width=50)
        self.button_a2_increase = customtkinter.CTkButton(self.frame_right, text="+", fg_color="#A633FF", width=50)
        self.button_a3_increase = customtkinter.CTkButton(self.frame_right, text="+", fg_color="#A633FF", width=50)
        self.button_a4_increase = customtkinter.CTkButton(self.frame_right, text="+", fg_color="#A633FF", width=50)
        self.button_a5_increase = customtkinter.CTkButton(self.frame_right, text="+", fg_color="#A633FF", width=50)
        self.button_a6_increase = customtkinter.CTkButton(self.frame_right, text="+", fg_color="#A633FF", width=50)
        self.button_a1_increase.grid(row=0, column=2, padx=10, pady=15)
        self.button_a2_increase.grid(row=1, column=2, padx=10, pady=15)
        self.button_a3_increase.grid(row=2, column=2, padx=10, pady=15)
        self.button_a4_increase.grid(row=3, column=2, padx=10, pady=15)
        self.button_a5_increase.grid(row=4, column=2, padx=10, pady=15)
        self.button_a6_increase.grid(row=5, column=2, padx=10, pady=15)
        
        self.label_a1 = customtkinter.CTkLabel(self.frame_right, text="Joint 1")
        self.label_a2 = customtkinter.CTkLabel(self.frame_right, text="Joint 2")
        self.label_a3 = customtkinter.CTkLabel(self.frame_right, text="Joint 3")
        self.label_a4 = customtkinter.CTkLabel(self.frame_right, text="Joint 4")
        self.label_a5 = customtkinter.CTkLabel(self.frame_right, text="Joint 5")      
        self.label_a6 = customtkinter.CTkLabel(self.frame_right, text="Joint 6")
        self.label_a1.grid(row=0, column=1, padx=10, pady=15)
        self.label_a2.grid(row=1, column=1, padx=10, pady=15)
        self.label_a3.grid(row=2, column=1, padx=10, pady=15)
        self.label_a4.grid(row=3, column=1, padx=10, pady=15)
        self.label_a5.grid(row=4, column=1, padx=10, pady=15)
        self.label_a6.grid(row=5, column=1, padx=10, pady=15)
        
        
        self.button_tool_activate = customtkinter.CTkButton(self.frame_right, text="Tool:\nactivate", fg_color="orange", width=50)
        self.button_tool_deactivate = customtkinter.CTkButton(self.frame_right, text="Tool:\ndeactivate", fg_color="orange", width=50)
        self.label_tool = customtkinter.CTkLabel(self.frame_right, text="Tool")
        self.button_tool_activate.grid(row=7, column=0, padx=10, pady=20)
        self.button_tool_deactivate.grid(row=7, column=2, padx=10, pady=20)
        self.label_tool.grid(row=7, column=1, padx=10, pady=20)
        
        self.button_speed_decrease = customtkinter.CTkButton(self.frame_right, text="-", fg_color="orange", width=50)
        self.button_speed_increase = customtkinter.CTkButton(self.frame_right, text="+", fg_color="orange", width=50)
        self.label_tool = customtkinter.CTkLabel(self.frame_right, text="Speed")
        self.button_speed_decrease.grid(row=9, column=0, padx=10, pady=20)
        self.button_speed_increase.grid(row=9, column=2, padx=10, pady=20)
        self.label_tool.grid(row=9, column=1, padx=10, pady=20)
        

        ###########################################################################################################################
        ##### FRAME: LISTBOX :: COMMANDS #####
        ###########################################################################################################################
        self.frame_listbox = customtkinter.CTkFrame(self, corner_radius=10)
        self.frame_listbox.grid(row=0, column=1, rowspan=3, padx=20, pady=(10, 0), sticky="nsew")
        self.frame_listbox.grid_rowconfigure(0, weight=1)
        self.frame_listbox.grid_columnconfigure(0, weight=1)
        
        self.listbox = Listbox(self.frame_listbox, bg="#2B2B2B", foreground="lightblue", relief="flat")
        self.listbox.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        
        ###########################################################################################################################
        ##### FRAME: BOTTOM :: COMMANDS #####
        ###########################################################################################################################
        self.frame_bottom = customtkinter.CTkFrame(self, corner_radius=10)
        self.frame_bottom.grid(row=3, column=0, columnspan=2, padx=20, pady=(20,10), sticky="nsew")
        self.frame_bottom.grid_rowconfigure(0, weight=1)
        self.frame_bottom.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        
        self.button_prev_step = customtkinter.CTkButton(self.frame_bottom, text="Previous", height=40, width=80, fg_color="purple")
        self.button_next_step = customtkinter.CTkButton(self.frame_bottom, text="Next", height=40, width=80, fg_color="purple")
        self.button_start = customtkinter.CTkButton(self.frame_bottom, text="Start", height=40, width=80, fg_color="green")
        self.button_stop = customtkinter.CTkButton(self.frame_bottom, text="Stop", height=40, width=80, fg_color="maroon")
        self.button_tool_command_active = customtkinter.CTkButton(self.frame_bottom, text="Tool Active", height=40, width=80, fg_color="#FF5733")
        self.button_tool_command_inactive = customtkinter.CTkButton(self.frame_bottom, text="Tool Inactive", height=40, width=80, fg_color="#FF5733")
        self.button_lin = customtkinter.CTkButton(self.frame_bottom, text="LIN", height=40, width=80, fg_color="#FF5733")
        self.button_ptp = customtkinter.CTkButton(self.frame_bottom, text="PTP", height=40, width=80, fg_color="#FF5733")
        self.button_prev_step.grid(row=0, column=0, padx=(20,5), pady=10)
        self.button_next_step.grid(row=0, column=1, padx=(5,20), pady=10)
        self.button_start.grid(row=0, column=2, padx=(20,5), pady=10)
        self.button_stop.grid(row=0, column=3, padx=(5,20), pady=10)
        self.button_tool_command_active.grid(row=0, column=4, padx=(20,5), pady=10)
        self.button_tool_command_inactive.grid(row=0, column=5, padx=(5,20), pady=10)
        self.button_lin.grid(row=0, column=6, padx=(20,5), pady=10)
        self.button_ptp.grid(row=0, column=7, padx=(5,20), pady=10)
        
        
        ###########################################################################################################################
        ##### View Controller #####
        ###########################################################################################################################
        self.controller = ViewController(self)



view = RobotView()
view.mainloop()