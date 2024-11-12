import yaml
import numpy as np

import MathUtils

class Joint:
    def __init__(self, id):
        self.id = id
        
        self.theta = 0
        self.d = 0
        self.a = 0
        self.alpha = 0
        
        self.limit_negative = 0
        self.limit_positive = 0
        
        self.step_mode = 4
        self.degrees_per_step = 1.8
        self.gear_ratio = 0
    
    def load_params_from_yaml(self):
        with open("joint_params.yaml", "r") as file:
            data = yaml.safe_load(file)
        joint_data = data["joints"].get(f"joint_{self.id}")
        
        self.theta          = MathUtils.deg2rad(joint_data["theta"])
        self.d              = joint_data["d"]
        self.a              = joint_data["a"]
        self.alpha          = MathUtils.deg2rad(joint_data["alpha"])
        self.limit_negative = joint_data["limit_negative"]
        self.limit_positive = joint_data["limit_positive"]
        self.gear_ratio     = joint_data["gear_ratio"]
        
    # check if set and get is needed and which unit is wanted, eg rad, deg, steps
        
    def set_theta(self, theta):
        self.theta = MathUtils.deg2rad(theta)
        
    def get_theta(self):
        return MathUtils.rad2_deg(self.theta)
    
    def transformation_matrix(self):
        cos_theta = np.cos(self.theta)
        sin_theta = np.sin(self.theta)
        cos_alpha = np.cos(self.alpha)
        sin_alpha = np.sin(self.alpha)
        
        return np.array([
            [cos_theta, -sin_theta * cos_alpha,  sin_theta * sin_alpha, self.a * cos_theta],
            [sin_theta,  cos_theta * cos_alpha, -cos_theta * sin_alpha, self.a * sin_theta],
            [        0,              sin_alpha,              cos_alpha,             self.d],
            [        0,                      0,                      0,                  1]
        ])