import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
 
os.system("cls")

def electric_field_plotter(source_points,field_point,electric_field_components):
    E_versor=electric_field_components/(np.sqrt(np.sum(electric_field_components[0:3]**2)))

    #visualization
    plt.close("all")
    fig=plt.figure()
    ax=fig.add_subplot(111,projection="3d")
    ax.scatter(xs=source_points[:,0],ys=source_points[:,1],zs=source_points[:,2],marker=".",s=100*np.abs(source_points[:,3]),color=["r" if i>0 else "b" for i in np.sign(source_points[:,3])])    

    ax.scatter(xs=field_point[0],ys=field_point[1],zs=field_point[2],marker="o",s=5)   

    ax.quiver(X=field_point[0],Y=field_point[1],Z=field_point[2],U=E_versor[0],V=E_versor[1],W=E_versor[2],length=2,color="black")    
    
    a=3*np.max(source_points[:3])
    ax.set_xlim([-a,a])
    ax.set_ylim([-a,a])
    ax.set_zlim([-a,a])    

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')    

    plt.show()
