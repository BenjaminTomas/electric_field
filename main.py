import os
import numpy as np
from electric_field_calculator import electric_field_calculator
from electric_field_plotter import electric_field_plotter
os.system("cls")



class charge():

    def __init__(self,x,y,z,q):
        self.x=x
        self.y=y
        self.z=z
        self.q=q

        self.props=[self.x,self.y,self.z,self.q]
        


class electric_field():

    def __init__(self,x,y,z,x_dir,y_dir,z_dir):
        self.x=x
        self.y=y
        self.z=z

        self.x_dir=x_dir
        self.y_dir=y_dir
        self.z_dir=z_dir

        self.position=np.array([self.x,self.y,self.z])
        self.magnitud=np.array([self.x_dir,self.y_dir,self.z_dir])
      


q1=charge(1,1,0,25)
q2=charge(1,-1,0,25)
q3=charge(-1,1,0,25)
q4=charge(-1,-1,0,25)
q5=charge(0,0,5,20)

source_points=np.vstack([q1.props,q2.props,q3.props,q4.props,q5.props])


field_point=np.array([0,0,1])




a=electric_field_calculator(source_points,field_point)
E=electric_field(a[0][0],a[0][1],a[0][2],a[1][0],a[1][1],a[1][2])



electric_field_plotter(source_points,field_point,E.magnitud)





