import numpy as np

import MathUtils
import Joint

class Robot:
    def __init__(self):
        self.joints = []
        
        for joint_id in range(1, 7):
            joint = Joint.Joint(joint_id)
            joint.load_params_from_yaml()
            self.joints.append(joint)
    
    def forward_kinematics(self):
        T = np.eye(4)
        for joint in self.joints:
            T = np.dot(T, joint.transformation_matrix())
            T[np.abs(T) < 1e-10] = 0
            T = np.round(T, decimals=5)
        return T