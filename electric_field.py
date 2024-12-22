import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
os.system("cls")



#Positions and charges [x,y,z,Q]:
p1=np.array([1,1,0,-1]) #[m,m,m,C]
p2=np.array([1,-1,0,-1]) #[m,m,m,C]
p3=np.array([-1,1,0,-1]) #[m,m,m,C]
p4=np.array([-1,-1,0,-1]) #[m,m,m,C]
source_points=np.vstack([p1,p2,p3,p4]) 


#Point where to calculate electric field.
field_point=np.array([0,0,1,1]) #[m,m,m,Q]

#Variable to define the electric field (Electric field vector).
E=0 # [V/m]

for i in range(source_points.shape[0]): 
    #This calculation is repeated for each charge.
    
    vector=field_point[0:3]-source_points[i,0:3] #Vector source-field (end-start).
    versor=1/(np.sqrt(np.sum(vector[0:3]**2))) #This factor converts vector in versor. 
    distance=1/(np.sqrt(np.sum(vector[0:3]**2)))**2 #This factor represents the inverse of distance squared (1/R^2).

    vector=vector/(versor*distance)

    E=E+vector #Sum of contribution of each charge to the total electric field.

k=1/(4*np.pi*8.85*10**(-12)) #Constant of calculus

E=k*E

E=np.round(E,2)
F=E*field_point[3]
mod_F=np.sqrt(np.sum(F[0:3]**2))
F_versor=F/mod_F


print(f"Force at charge: {field_point} \nEx={E[0]} [V/m]\nEy={E[1]} [V/m]\nEz={E[2]} [V/m]")  



#visualization
plt.close("all")
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.scatter(xs=source_points[:,0],ys=source_points[:,1],zs=source_points[:,2],marker=".",s=100*np.abs(source_points[:,3]),color=["r" if i>0 else "b" for i in np.sign(source_points[:,3])])

ax.scatter(xs=field_point[0],ys=field_point[1],zs=field_point[2],marker="o",s=10,color=["r" if np.sign(field_point[3])>0 else "b"])

ax.quiver(X=field_point[0],Y=field_point[1],Z=field_point[2],U=F_versor[0],V=F_versor[1],W=F_versor[2],length=2,color="black")


ax.set_xlim([-10,10])
ax.set_ylim([-10,10])
ax.set_zlim([-10,10])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

#There is something wrong, whit the charges in those place, f must be negative in z direction,
#Because the sign of the charges are different.