import os
os.system("cls")



class charge():

    def __init__(self,x,y,z,q):
        self.x=x
        self.y=y
        self.z=z
        self.q=q


class electric_field():

    def __init__(self,x,y,z,x_dir,y_dir,z_dir):
        self.x=x
        self.y=y
        self.z=z

        self.x_dir=x_dir
        self.y_dir=y_dir
        self.z_dir=z_dir
        
class electric_force(electric_field):
    def __init__(self,x,y,z,x_dir,y_dir,z_dir,q):
        self.x=x
        self.y=y
        self.z=z
        self.q=q

        self.x_dir=x_dir*self.q
        self.y_dir=y_dir*self.q
        self.z_dir=z_dir*self.q





