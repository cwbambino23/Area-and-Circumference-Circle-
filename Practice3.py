#this progrom will calculate the area and the circumference of a circle. It will has the user for the radius

import math                                                                                  #Use the math operators (MatH Library)


radius = float (input ("Enter the radius "))                                                  #Ask for user to input the radius (convert the string to float)
area = (math.pi * (radius ** 2))                                                              #The formula for area of a circle 
circumference = (2 * math.pi * radius)                                                        #The formula for circumference of a circle  

print ("The area is: ", round(area,2),  " The circumference is: ", round(circumference,2))    #Print the coversion for the area and the circumference 