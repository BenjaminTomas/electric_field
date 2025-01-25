import os
import numpy as np

os.system("cls")


def electric_field_calculator(source_points,field_point):
    #Point where to calculate electric field.
    
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
    # print(f"El campo electrico es {E}")
    E=np.round(E,2)    



    return field_point, E
