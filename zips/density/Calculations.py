# -*- coding: cp1252 -*-
#/usr/bin/env python
'''
Simon H. Larsen
Density simulator > Calculations
Project startet: 06. september 2012
'''
import math

class Formulas:
    def __init__(self):
        self.pi = 3.1415926535
        self.gravity = 9.82 #m/s^2
        self.density_water = 1000.0 #kg/m^3
        self.density_air   = 1.29 #kg/m^3
        self.drag_sphere   = 0.47
        print "Finished initiating Calculations module..."
    """
    --->Calculations<---
    """
    def object_displaced_height(self, height, radius, scale, screen_height): #Fortrængt højde
        displaced_height = (height) + ( 2*radius*scale ) - (screen_height*0.3)
        if displaced_height > radius*2*scale:
            displaced_height = radius*2*scale
        if displaced_height < 0:
            displaced_height = 0
        displaced_height /= scale #m
        return displaced_height    
    def decide_densities(self, user_densityAir, user_densityFluid):
        if user_densityAir > 0:
            air_density = user_densityAir
        else:
            air_density = self.density_air
        if user_densityFluid > 0:
            fluid_density = user_densityFluid
        else:
            fluid_density = self.density_water
        return air_density, fluid_density
    """
    --->Mathematics<---
    """
    def object_displaced_volume(self, radius, volume, displaced_height): #Fortrængt volume
        displaced_volume = self.pi * math.pow(displaced_height,2) * ( 1.0/3 ) * ( (3*radius) - displaced_height ) #m^3
        return displaced_volume   
    def CS_radius(self, volume, displaced_height):
        #Complex equation, it's been split to bits
        bit1 = volume * 6.0
        bit2 = self.pi * displaced_height
        if bit2 != 0:
            bit3 = math.pow(displaced_height,2)
            bit4 = bit1/bit2-bit3
            bit5 = bit4/3.0
            radius = math.sqrt(bit5)
        else:
            radius = None
        return radius
    def cross_sectional_area(self, radius):
        surface_area = self.pi * math.pow(radius, 2)
        return surface_area
    def object_radius_sphere(self, volume):
        radius = math.pow((volume*3.0)/(4.0*self.pi), 1.0/3.0)
        return radius
    def surface_area(self, radius): #Overfladeareal for kugle
        area = 4 * self.pi * math.pow(radius, 2) #m^2
        return area
    """
    --->Physics<---
    """
    def object_volume_sphere(self, radius=None, density=None, mass=None): #Kugle volume
        if radius != None:
            volume  = 1.3333333 * self.pi * math.pow(radius, 3) #m^3
        elif type(density) != None and type(mass) != None:
            volume = mass/density
        else:
            print "Invalid parameters return 0.5 cubic meters"
            return 0.5
        return volume
    def object_gravity(self, mass): #Tyngdekraften på kuglen
        gravity_force = mass * self.gravity #N
        return gravity_force
    def object_buoyancy(self, displaced_volume, volume, user_densityAir, user_densityFluid): #Opdrift
        user_densityAir, user_densityFluid = self.decide_densities(user_densityAir, user_densityFluid)
        buoyancy = displaced_volume * user_densityFluid * self.gravity #N 
        air_volume = volume - displaced_volume #This is zero  if the sphere is fully submerged
        air_buoyancy = air_volume * user_densityAir * self.gravity #N 
        buoyancy +=air_buoyancy
        return buoyancy
    def drag_equation(self, speed, displaced_height, displaced_volume, radius, volume, user_densityFluid, user_densityAir): #Modvirkende kraft fra væske
        if displaced_volume > 0.0 and speed > 0:
            medium = user_densityFluid
        elif volume - displaced_volume  < 0.000000001: #for unprecise calculations - 1e-6 liter or 1e-3 cm^3 unpresicion
            medium = user_densityFluid
        else:
            medium = user_densityAir
        if displaced_volume > 0.0 and speed > 0.0:
            volume = displaced_volume
            length = displaced_height
        elif displaced_volume > 0.0 and speed < 0.0:
            if volume - displaced_volume  < 0.000000001:
                length = displaced_height
            else:
                length = (radius*2.0)-displaced_height
        else:
            length = radius*2.0
        if length > radius: length = radius
        if length <= 0.0: length = 0.0001
        radius = self.CS_radius(volume, length)
        area = self.cross_sectional_area(radius)
        force_drag = 0.5 * medium * math.pow(speed, 2) * self.drag_sphere * area
        if speed < 0.0:
            force_drag *= -1 
        return force_drag
    def object_mass(self, density, volume): #Objektets masse
        mass = volume * density #kg
        return mass
    def object_acceleration(self, gravity_force, buoyancy, mass, drag_force): #Acceleration
        total_force = gravity_force - buoyancy - drag_force #N
        acceleration = total_force / mass #m/s^2
        return acceleration
    def object_speed(self, acceleration, time): #Hastighed efter tid
        speed  = acceleration * (float(time)/1000.0) #m/s
        return speed
    def object_density(self, mass, volume): #Densitet i forhold til masse og rumfang
        density  = mass / volume #kg/m^3
        return density
