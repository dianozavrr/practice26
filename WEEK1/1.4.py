import math

v = float(input("швидкість: "))
ang = float(input("кут: "))
g = 9.81 

angle_rad = math.radians(ang) 

R = (v**2 * math.sin(2 * angle_rad)) / g 
print("дальність польоту:", R)

H_max = (v**2 * (math.sin(angle_rad))**2) / (2 * g) 
print("макс висота:", H_max)

t = 0
while True:
    y = v * math.sin(angle_rad) * t - 0.5 * g * t**2
    if y < 0:
        break
    print("Час", t, "с:", "висота", y)
    t += 1
    
