# -*- coding: cp1252 -*-
#/usr/bin/env python
'''
Simon H. Larsen
Density simulator > Pygame_handling
Project startet: 06. september 2012
'''
import Buttons, subpixelsurface, Features
from zModule import * #includes pygame, os, sys and pygame.locals

RED   = (255,  0,  0)
GREEN = (0  ,255,  0)
BLUE  = (0  ,  0,255)

class Draw_options:
    def __init__(self):
        self.work_dir = os.getcwd()
        self.data_dir = os.path.join(self.work_dir,'data')
        self.image_dir= os.path.join(self.data_dir,'images')
        self.menuBar  = pygame.image.load(os.path.join(self.image_dir,'menu_bar.png'))
        AnimationArrow = pygame.image.load(os.path.join(self.image_dir,'arrow.png'))
        self.AnimationArrow_sub = subpixelsurface.SubPixelSurface(AnimationArrow, x_level=4)
        self.sphere = pygame.image.load(os.path.join(self.image_dir,'plastic.png'))
        self.sphere_sub = subpixelsurface.SubPixelSurface(self.sphere, x_level=4)
        self.font_path = os.path.join(self.work_dir, 'font')
        self.myFont = pygame.font.Font(os.path.join(self.font_path,'CALIBRI.TTF'), 19)
        self.valueFont = pygame.font.Font(os.path.join(self.font_path,'CALIBRIB.TTF'), 16)
        self.info   = ["Speed: ", "Volume: ", "Submerged height: ", "Submerged volume: ", "Gravity force: ", "Buoyancy: ", "Drag: ", "Acceleration: "] 
        self.spheres = {"soccer"    : pygame.image.load(os.path.join(self.image_dir,'soccer.png')),
                        "cork"    : pygame.image.load(os.path.join(self.image_dir,'cork.png')),
                        "wood"    : pygame.image.load(os.path.join(self.image_dir,'wood.png')),
                        "plastic" : pygame.image.load(os.path.join(self.image_dir,'plastic.png')),
                        "silicon" : pygame.image.load(os.path.join(self.image_dir,'silicon.png'))}
        self.densities = {"soccer"  : 2.5,
                          "cork"    : 240,
                          "wood"    : 700,
                          "plastic" : 1175,
                          "silicon" : 2330}
        self.currSphere = "cork"
        self.AnimationClock = pygame.time.Clock()
        self.animationTime = 0
        self.x_pos, self.y_pos = (340,445)
        
    def sphere2(self, surface, radius, scale, density, pos=0.0):
        radius *= scale
        centerx = surface.get_width()/2
        differences = {}
        for key in self.densities.iterkeys():
            difference = density - self.densities[key]
            if difference < 0: difference *= -1 
            differences[key] = difference
        sphere = min(differences, key=differences.get)
        if sphere == "soccer" and density > 50: sphere = "cork"
        if (self.sphere.get_size()[0] != int(radius*2) or 
            self.sphere.get_size()[1] != int(radius*2) or
            sphere != self.currSphere):
            print "Reshaping sphere"
            self.currSphere = sphere
            self.sphere = pygame.image.load(os.path.join(self.image_dir,self.currSphere+'.png'))
            self.sphere = pygame.transform.smoothscale(self.sphere, (int(radius*2), int(radius*2)))
            self.sphere_sub = subpixelsurface.SubPixelSurface(self.sphere, x_level=4)
        surface.blit(self.sphere_sub.at( centerx-radius, pos ), ( centerx-radius, pos ))
        return surface    
    
    def fluid(self, surface, air_color = (100,149,237)):
        screen_w,screen_h = surface.get_size()
        pygame.draw.rect(surface, air_color, (0,screen_h*0.3,screen_w,screen_h*0.7))
        return surface
    
    def fluid_opacity(self, surface, fluid_color = (135,206,250)):
        screen_w,screen_h = surface.get_size()
        s = pygame.Surface((screen_w,screen_h*0.7))
        s.fill((135,206,250))
        s.set_alpha(50)
        surface.blit(s, (0,screen_h*0.3))
        return surface
    
    def air(self, surface, fluid_color = (135,206,250)):
        screen_w,screen_h = surface.get_size()
        pygame.draw.rect(surface, fluid_color, (0,0,screen_w,screen_h*0.3))
        return surface
    
    def scale(self, surface, scale, ppi=99.34): #Default no. of pixel per inch is 99.34
        ppcm = ppi / 2.54 #converting to centimeters instead of inches
        scale_h = ppcm *5
        screenSize = surface.get_size()
        height = screenSize[1]*0.3
        pygame.draw.aaline(surface, (0,0,0), (5 , height)      , (45, height))
        pygame.draw.aaline(surface, (0,0,0), (25, height)      , (25, height+scale))
        pygame.draw.aaline(surface, (0,0,0), (5 , height+scale), (45, height+scale))
        surface.blit(self.myFont.render("1m", 1, (0,0,0)),(30,(scale/2)+height-15))
        return surface
    
    def menu(self, surface, cbs, btns, calculations, scale):
        surface.blit(self.menuBar, (0,450))
        self.cbs(surface, cbs)
        self.btns(surface, btns)
        self.values(surface, calculations, scale)
        return surface
    
    def cbs(self, surface, cbs):
        for cb in cbs:
            cb.draw(surface)
        return surface
            
    def btns(self, surface, btns):
        for btn in btns:
            btn.draw(surface)
        return surface
    
    def details(self, surface, calculations, radius, scale, pos):
        width, height = surface.get_width(), surface.get_height()
        centerx = width/2
        _height = _length = radius*scale*2
        #arrow if sphere is below surface
        if pos > height:
            myText = self.myFont.render("%.3f" %(pos/scale-(height/scale))+'m', 1, (0,0,0))
            surface.blit(myText, (centerx-(myText.get_width()/2), (height-110)-(myText.get_height()/2)))
            pygame.draw.aaline(surface, (0,0,0), (centerx, height-100), (centerx, height-20))
            pygame.draw.aaline(surface, (0,0,0), (centerx-50, height-50), (centerx, height-20))
            pygame.draw.aaline(surface, (0,0,0), (centerx+50, height-50), (centerx, height-20))
        #arrow if sphere is above surface
        elif pos < 0-_height:
            myText = self.myFont.render("%.3f" %(-pos/scale-(height/scale)+(radius*2))+'m', 1, (0,0,0))
            surface.blit(myText, (centerx-(myText.get_width()/2), (110)-(myText.get_height()/2)))
            pygame.draw.aaline(surface, (0,0,0), (centerx, 100), (centerx, 20))
            pygame.draw.aaline(surface, (0,0,0), (centerx-50, 50), (centerx, 20))
            pygame.draw.aaline(surface, (0,0,0), (centerx+50, 50), (centerx, 20))
        pygame.draw.aaline(surface, (0,0,0), (width-5, height*0.3), (width-5, (height*0.3)+(calculations[2]*scale)))
        pygame.draw.aaline(surface, (0,0,0), (width-5, height*0.3), (width-5, (height*0.3)+(calculations[2]*scale-_height)))
        return surface
    
    def forces(self, surface, calculations, radius, scale, pos):
        width = surface.get_width()
        height = surface.get_height()
        _scale = scale
        scale = radius * scale
        buoyancy = calculations[5]
        gravity = calculations[4]
        arrowHeight_buoyancy = ((buoyancy*0.01)*_scale)/scale
        arrowHeight_gravity = ((gravity*0.01)*_scale)/scale
        #draw it!
        #buoyancy...
        pygame.draw.rect(surface, GREEN, ((surface.get_width()/2)+(scale*0.1), pos+(scale), -scale*0.2, -arrowHeight_buoyancy))
        x1,y1 = (width/2)-(scale*0.2), pos+scale-arrowHeight_buoyancy 
        x2,y2 = width/2               , pos+scale-arrowHeight_buoyancy-(height*0.02)
        x3,y3 = (width/2)+(scale*0.18), pos+scale-arrowHeight_buoyancy 
        pygame.draw.polygon(surface, GREEN, ((x1,y1),(x2,y2),(x3,y3)))
        myText = self.myFont.render("%.2f" % buoyancy + 'N', 1, (255,255,255))
        surface.blit(myText, ((width/2)+(scale*0.18)+10, pos+scale-arrowHeight_buoyancy-10))
        #gravity...
        pygame.draw.rect(surface, BLUE, ((surface.get_width()/2)+(scale*0.1), pos+(scale), -scale*0.2, arrowHeight_gravity))
        x1,y1 = (width/2)-(scale*0.2), pos+scale+arrowHeight_gravity 
        x2,y2 = width/2               , pos+scale+arrowHeight_gravity+(height*0.02)
        x3,y3 = (width/2)+(scale*0.18), pos+scale+arrowHeight_gravity 
        pygame.draw.polygon(surface, BLUE, ((x1,y1-1),(x2,y2-1),(x3,y3-1)))
        myText = self.myFont.render("%.2f" % gravity + 'N', 1, (255,255,255))
        surface.blit(myText, ((width/2)+(scale*0.18)+10,(pos+scale+arrowHeight_gravity-10)))
        return surface
    
    def fps(self, surface, fps):
        surface.blit(self.myFont.render("fps: "+str(fps), 1, (255,255,0)),(2, 2))
        return surface
    
    def values(self, surface, calculations, scale):
        volume = calculations[1] * 1000
        if calculations[10] != 0:
            fluid_density = calculations[10]
        else:
            fluid_density = 1000
        if calculations[11] != 0:
            air_density = calculations[11]
        else:
            air_density = 1.29
        values = [calculations[8], volume, calculations[9], fluid_density, air_density, scale]
        var = 0
        x_pos = 134
        for value in values:
            var += 1
            if var >= 4: 
                x_pos = 426
                var = 1
            if value >= 50 : value = "%.0f" % value
            elif value >= 0.1 : value = "%.2f" % value
            else: value = "%.3f" % value
            surface.blit(self.valueFont.render(value, 1, (21,31,40)),(x_pos, 465 + (var-1)*35))

    def arrowAnimation(self, surface):
        currentAnimationTime = self.AnimationClock.tick()
        self.animationTime += currentAnimationTime
        if self.animationTime <= 500:
            self.x_pos += 30.0*(currentAnimationTime/1000.0)
            self.y_pos += 30.0*(currentAnimationTime/1000.0)
        elif 800 < self.animationTime <= 1300:
            self.x_pos -= 30.0*(currentAnimationTime/1000.0)
            self.y_pos -= 30.0*(currentAnimationTime/1000.0)
        elif self.animationTime > 1600:
            self.animationTime = 0
        surface.blit(self.AnimationArrow_sub.at(self.x_pos, self.y_pos), (self.x_pos, self.y_pos))

class Window:
    def __init__(self):
        self.Draw = Draw_options() #Draw_options object
        self.Features = Features.Methods() #Features object
        self.work_dir  = os.getcwd()
        self.data_dir  = os.path.join(self.work_dir,'data')
        self.image_dir = os.path.join(self.data_dir,'images')
        self.arrowUp   = pygame.image.load(os.path.join(self.image_dir,'menu_up.png'))
        self.arrowDown = pygame.image.load(os.path.join(self.image_dir,'menu_down.png'))
        
        text = ["Show details"]
        pos  = [(420,565)]
        self.cbs = []
        self.cbs_state = []
        self.create_cb(text, pos)
        #zModule buttons
        images    = [os.path.join(self.image_dir, 'rewind.png') ,os.path.join(self.image_dir, 'rewind.png'),
                     os.path.join(self.image_dir, 'stop.png')   ,os.path.join(self.image_dir, 'stop.png'),
                     os.path.join(self.image_dir, 'play.png')   ,os.path.join(self.image_dir, 'play.png'),
                     os.path.join(self.image_dir, 'forward.png'),os.path.join(self.image_dir, 'forward.png'),
                     os.path.join(self.image_dir, 'up.png')     ,os.path.join(self.image_dir, 'up.png'),
                     os.path.join(self.image_dir, 'down.png')   ,os.path.join(self.image_dir, 'down.png'),
                     os.path.join(self.image_dir, 'up.png')     ,os.path.join(self.image_dir, 'up.png'),
                     os.path.join(self.image_dir, 'down.png')   ,os.path.join(self.image_dir, 'down.png'),
                     os.path.join(self.image_dir, 'up.png')     ,os.path.join(self.image_dir, 'up.png'),
                     os.path.join(self.image_dir, 'down.png')   ,os.path.join(self.image_dir, 'down.png'),
                     os.path.join(self.image_dir, 'up.png')     ,os.path.join(self.image_dir, 'up.png'),
                     os.path.join(self.image_dir, 'down.png')   ,os.path.join(self.image_dir, 'down.png'),
                     os.path.join(self.image_dir, 'up.png')     ,os.path.join(self.image_dir, 'up.png'),
                     os.path.join(self.image_dir, 'down.png')   ,os.path.join(self.image_dir, 'down.png'),
                     os.path.join(self.image_dir, 'up.png')     ,os.path.join(self.image_dir, 'up.png'),
                     os.path.join(self.image_dir, 'down.png')   ,os.path.join(self.image_dir, 'down.png'),]
        functions = [nothing,
                     nothing,
                     nothing,
                     nothing,
                     nothing,
                     nothing,
                     nothing,
                     nothing,
                     nothing,
                     nothing,
                     nothing,
                     nothing,
                     nothing,
                     nothing,
                     nothing,
                     nothing,]
        pos       = [(18,564),
                     (71,564),
                     (124,564),
                     (157,564),
                     (116,462),
                     (116,475),
                     (116,498),
                     (116,511),
                     (116,532),
                     (116,545),
                     (408,462),
                     (408,475),
                     (408,498),
                     (408,511),
                     (408,532),
                     (408,545),]
        self.btns = []
        self.btns_state = []
        self.create_btn(pos, images, functions)
        
        #Buttons
        self.menuArrow = Buttons.Button()
        self.show_menu = False
        self.arrowAnimation = True
        print "Finished initiating Pygame_handling module..."
        
    def main_window(self, radius, pos, scale, fps, calculations):
        new_pos = None
        speed = calculations[0]
        self.Draw.air(self.screen)
        self.Draw.fluid(self.screen)
        self.Draw.sphere2(self.screen, radius, scale, calculations[9], pos)
        self.Draw.fluid_opacity(self.screen)   
        self.check_cbs(scale, calculations, fps, radius, pos)
        self.decide_drawing(radius, pos, scale, fps, calculations)
        self.draw_btn()
        if self.arrowAnimation == True: self.Draw.arrowAnimation(self.screen)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                if self.arrowAnimation is False:
                    new_pos = self.check_buttons(pygame.mouse.get_pos())
                self.arrowAnimation = False
            elif event.type == VIDEORESIZE:
                self.set_display(event.size)
        if self.show_menu:
            for n in range(len(self.cbs)):
                self.cbs_state[n] = self.cbs[n].update(events)
            for n in range(len(self.btns)):
                self.btns_state[n] = self.btns[n].update(events)
        pygame.display.flip()
        if new_pos is not None: 
            pos = new_pos[1] - (radius * scale)
            speed = 0
        return pos, speed
    
    def create_cb(self, text, pos):
        for n in range(len(text)):
            cb = zCheckbutton(text[n], pos[n], nothing, nothing, 2, os.path.join(self.Draw.font_path,'CALIBRI.TTF'), BLACK, BLACK, WHITE)
            self.cbs.append(cb)
            self.cbs_state.append(False)
            
    def create_btn(self, pos, images, functions):
        for n in range(len(pos)):    
            imgbutton = zImgButton(functions[n], pos[n], images[n*2], images[(n*2)+1])
            self.btns.append(imgbutton)
            self.btns_state.append(False)
    
    def check_btns(self):
        if self.btns_state[0]:
            print "Slowing down"
            self.btns_state[0] = False
            return {"time": 0.9}
        elif self.btns_state[1]:
            return {"time": False}
            self.btns_state[1] = False
            return "reset"
        elif self.btns_state[2]:
            print "Reset stuff..."
            self.btns_state[2] = False
            return {"time": True}
        elif self.btns_state[3]:
            print "Speeding up"
            self.btns_state[3] = False
            return {"time": 1.1}
        elif self.btns_state[4]:
            print "Increasing mass"
            self.btns_state[4] = False
            return {"mass": 1.05}
        elif self.btns_state[5]:
            print "Decreasing mass"
            self.btns_state[5] = False
            return {"mass": 0.95}
        elif self.btns_state[6]:
            print "Increasing volume"
            self.btns_state[6] = False
            return {"volume": 1.05}
        elif self.btns_state[7]:
            print "Decreasing volume"
            self.btns_state[7] = False
            return {"volume": 0.95}
        elif self.btns_state[8]:
            print "Increasing density"
            self.btns_state[8] = False
            return {"density": 1.05}
        elif self.btns_state[9]:
            print "Decreasing density"
            self.btns_state[9] = False
            return {"density": 0.95}
        elif self.btns_state[10]:
            print "Increasing fluid density"
            self.btns_state[10] = False
            return {"fluid density": 1.05}
        elif self.btns_state[11]:
            print "Decreasing fluid density"
            self.btns_state[11] = False
            return {"fluid density": 0.95}
        elif self.btns_state[12]:
            print "Increasing air density"
            self.btns_state[12] = False
            return {"air density": 1.05}
        elif self.btns_state[13]:
            print "Decreasing air density"
            self.btns_state[13] = False
            return {"air density": 0.95}
        elif self.btns_state[14]:
            print "Increasing scale"
            self.btns_state[14] = False
            return {"scale": 20}
        elif self.btns_state[15]:
            print "Decreasing scale"
            self.btns_state[15] = False
            return {"scale": -20}
        return None        
    
    def check_cbs(self, scale, calculations, fps, radius, pos):
        for n in range(len(self.cbs_state)):
            if self.cbs_state[n] is True:
                if n is 0: #Show scale
                    self.Draw.scale(self.screen, scale) 
                    self.Draw.forces(self.screen, calculations, radius, scale, pos)
                    self.Draw.fps(self.screen, fps)
                    self.Draw.details(self.screen, calculations, radius, scale, pos)
         
    def draw_btn(self):
        if self.show_menu == True:
            self.screen = self.menuArrow.create_image_button(self.screen,  455,423, self.arrowDown)
        else:
            self.screen = self.menuArrow.create_image_button(self.screen,  455,573, self.arrowUp)
            
    def decide_drawing(self, radius, pos, scale, fps, calculations):
        if self.show_menu:
            self.Draw.menu(self.screen, self.cbs, self.btns, calculations, scale)
                
    def set_display(self, screen_size, caption=False):
        if caption != False:
            sysicon = pygame.image.load(os.path.join(self.Draw.image_dir,'icon.jpg'))
            pygame.display.set_icon(sysicon)
            self.screen = pygame.display.set_mode(screen_size, RESIZABLE, 32)
            pygame.display.set_caption(caption)
        else:
            self.screen = pygame.display.set_mode(screen_size, RESIZABLE, 32)
        size = self.screen.get_size()
        width = (size[0]/2) - (232/2)
        height = (size[1]/2) - (232/2)
        self.screen.fill((240,240,240))
        self.screen.blit(pygame.image.load(os.path.join(self.Draw.image_dir,'working_on_it.png')), (width,height))
        pygame.display.flip()
        
    def check_buttons(self, pos):
        if self.menuArrow.pressed(pos): #reverse true/false
            if self.show_menu: 
                self.show_menu = False
            else: 
                self.show_menu = True
        elif not self.show_menu:
            return pos
        return None
    
    def prepare_sphere(self, radius, density, scale):
        self.Draw.sphere2(self.screen, radius, density, scale)
        return True