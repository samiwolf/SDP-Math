# -*- coding: cp1252 -*-
#/usr/bin/env python
'''
Simon H. Larsen
Density simulator > Features
Project startet: 06. september 2012
'''
import ast
class Methods():
    def __init__(self):
        self.changes = True
        self.dictionary = {"mass": 350, "radius": 0,"volume": 0.524, "density": 667.93893, "fluid density": 1000, "air density": 1.29, "scale": 200, "time": 1.0}
        self.err_getSettings = "Not possible to get settings. Try to save new settings."
        print "Finished initiating Features module..."

    def monitor_changes(self, changes=None, initiative=False):
        if changes is None:
            self.changes is True
        elif not initiative:
            for change in changes:
                if 'scale' in changes:
                    print "Re-evaluating:", changes[change], "to", change
                    self.dictionary[change] += changes[change]
                    if self.dictionary[change] <= 1.0: self.dictionary[change] = 2
                elif self.dictionary[change] + changes[change] >= 0.005:
                    self.dictionary[change] *= changes[change]
                    print "Re-evaluating:", (changes[change]-1)*100, "% to", change
                    if change is "time" and changes[change] is False:
                        self.dictionary[change] = 0.0
                    elif change is "time" and changes[change] is True:
                        self.dictionary[change] = 1.0
                else:
                    self.dictionary[change] = 0.005
                    print "Re-evaluating:", change, "equal to", 0.005
                    print "Cannot be reduced below zero"
        else:
            for change in changes:
                self.dictionary[change] = changes[change]
                print "Performing change:", change, changes[change]

# This has been commented out because it has not yet been finished!
#    def set_speed(self, time=0):
#        if time: self.dictionary["time"] = 1
#        else:    self.dictionary["time"] += time
#        return time
#    def save_settings(self, scale, radius, mass, spawnpoint, user_densityAir=0, user_densityFluid=0):
#        settings = self.dictionary
#        f = open("settings.txt", "w") #Create new file of overwrite existing
#        f.write(str(settings))
#        f.close()
#        return settings
#    def get_settings(self):
#        try:
#            f = open("settings.txt", "r")
#            f = f.read()
#            settings = ast.literal_eval(str(f))
#            return settings
#        except:
#            print self.err_getSettings
    
    
    
