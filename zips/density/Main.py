# -*- coding: cp1252 -*-
#/usr/bin/env python
'''
Simon H. Larsen
Density simulator
Project startet: 06. september 2012
'''
import pygame, Pygame_handling, Calculations, Features
#import profile
# profiling the program makes it easy to spot time consuming functions

class Simulator:
    def __init__(self):
        self.Clock = pygame.time.Clock() #Used to keep a constant frame-rate
        self.Time  = pygame.time.Clock() #Used to keep time of the simulation
        self.framerate = 10000            #Frame-rate
        '''
        Creating objects from my modules
        Calculations: calculates the physics which affect the sphere
        PyObject:     handles buttons, check boxes, what to draw and drawing it
        Features:     includes many different feature, some are essential
        '''
        self.Calculations = Calculations.Formulas()
        self.PyObject     = Pygame_handling.Window() 
        self.Features     = Features.Methods()
        #Simulator settings
        self.pos, self.speed = 0,0
        #Trying to load saved settings...
        try:
            settings = self.Features.get_settings()
            self.Features.monitor_changes(settings, True)
        except:
            self.mass, self.volume, self.density = 0,0,0
        self.verify_settings()
        #Save the settings
        #self.Features.save_settings(self.scale, self.radius, self.mass, 
        #                            self.pos, self.user_densityAir, 
        #                            self.user_densityFluid)
        #Start the program
        #Width & height, Window name
        self.PyObject.set_display((500,600), "Density Simulator - Simon Larsen") 
        self.PyObject.prepare_sphere(self.radius, self.density, self.scale)
        self.dictionary = ["mass","radius","volume","density","fluid density",
                           "air density","scale","time"]
        #Reset timer for the arrow animation on startup
        self.PyObject.Draw.AnimationClock.tick() 
        #Reset timer - nullifying time spend while initializing
        print "Initiate time:", self.Time.tick(), "ms" 
    '''
    The main loop:
    This function is what starts the chain. It keeps track
    of time, calls for calculations and calls Pygame to
    draw the simulation in a desired scale. 
    '''
    def main_loop(self):
        calculations = [0]
        while True:
            self.Clock.tick(self.framerate)
            # Set the time depending on the speed from self.time
            time = self.Time.tick() * self.time
            # Run through all calculations
            calculations = self.calculate(time, calculations[0])
            # Re-evaluate the position of the sphere
            self.pos += calculations[0]*(float(time)/1000.0)*self.scale 
            # Send a bunch of variables to the PyObject (Pygame_handling.py)
            self.pos, self.speed = self.PyObject.main_window(self.radius, 
                                   self.pos, self.scale, self.Clock.get_fps(), 
                                   calculations)
            # Get a change dictionary
            change = self.PyObject.check_btns()
            # Save the changes to the Features object
            self.Features.monitor_changes(change)
            # Verify the changes and re-calculate new constants
            if change is not None: self.verify_settings(change)
            #self.check_PyObject_btns()
                   
    def verify_settings(self, change = "None"):
        if self.Features.changes:
            variables = self.Features.dictionary
            self.mass = variables["mass"]
            self.volume = variables["volume"]
            self.radius = variables["radius"]
            self.density = variables["density"]
            self.user_densityFluid = variables["fluid density"]
            self.user_densityAir = variables["air density"]
            self.scale = variables["scale"]
            self.time = variables["time"]

            # Calculate changes
            if "mass" in change:
                self.gravity_force = self.Calculations.object_gravity(self.mass)
                self.density = self.Calculations.object_density(self.mass, 
                                                                self.volume)
            if "volume" in change:
                self.radius  = self.Calculations.object_radius_sphere(self.volume)
                self.density = self.Calculations.object_density(self.mass, 
                                                                self.volume)
            if "radius" in change:
                self.volume  = self.Calculations.object_volume_sphere(self.radius)
                self.density = self.Calculations.object_density(self.mass, 
                                                                self.volume)
            if "density" in change:
                self.mass = self.Calculations.object_mass(self.density, 
                                                          self.volume)
                
            self.radius = self.Calculations.object_radius_sphere(self.volume)
            self.gravity_force = self.Calculations.object_gravity(self.mass)
            self.volume = self.Calculations.object_volume_sphere(self.radius)
            self.density=self.Calculations.object_density(self.mass, self.volume)
             
            # Updating the dictionary with the new calculations
            self.Features.dictionary["mass"]    = self.mass
            self.Features.dictionary["volume"]  = self.volume
            self.Features.dictionary["radius"]  = self.radius
            self.Features.dictionary["density"] = self.density
# Call for calculations            
    def calculate(self, time, speed = 0):
        # Look at Calculatoins.py for more info
        size = self.PyObject.screen.get_size()[1]
        displaced_height = self.Calculations.object_displaced_height(self.pos, 
                           self.radius, self.scale, size)
        
        displaced_volume = self.Calculations.object_displaced_volume(self.radius, 
                           self.volume, displaced_height)
        
        drag_force = self.Calculations.drag_equation(speed, displaced_height, 
                     displaced_volume, self.radius, self.volume, 
                     self.user_densityFluid, self.user_densityAir)
        
        buoyancy = self.Calculations.object_buoyancy(displaced_volume, 
                   self.volume, self.user_densityAir, self.user_densityFluid)
        
        acceleration = self.Calculations.object_acceleration(self.gravity_force, 
                       buoyancy, self.mass, drag_force)
        
        self.speed += self.Calculations.object_speed(acceleration, time)
        return (self.speed, self.volume, displaced_height, displaced_volume, 
                self.gravity_force, buoyancy, drag_force, acceleration, self.mass,
                self.density, self.user_densityFluid, self.user_densityAir)

# This has been commented out because it has not yet been finished!
#    def check_PyObject_btns(self):
#        btn_pressed = self.PyObject.check_btns()
#        if btn_pressed == 0:
#            self.set_settings(self.Features.get_settings())
#            #self.time_manipulate += 0.05
#            
#    def set_settings(self, settings):
#        #settings: scale, radius, mass, spawnpoint, user_densityAir, user_densityFluid
#        for n in range(len(settings)):
#            settings[n] = float(settings[n])
#        self.scale  = settings[0]
#        self.radius = settings[1]
#        self.mass   = settings[2]
#        self.pos    = settings[3]
#        self.user_densityAir   = settings[4]
#        self.user_densityFluid = settings[5]
#        self.speed = 0        

Oop = Simulator()
Oop.main_loop() # Comment this line and uncomment next two lines to run profile
#remember to import profile
#profile.run('Oop.main_loop()')
