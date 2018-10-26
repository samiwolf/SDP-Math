import pygame
import random
import math

background_colour = (255, 255, 255)
(width, height) = (800, 600)
mass_of_air = 0.01
elasticity = 0.75
gravity = (math.pi, 0.002)
screen = pygame.display.set_mode((width, height))
number_of_particles = 0
my_particles = []

class ParticleFactory(object):
    def create_particle(self, type):
        size = random.randint(10, 20)
        density = random.randint(1, 10)
        x = random.randint(size, width - size)
        y = random.randint(size, height - size)

        if type=='red':
            particle = RedParticle(x, y, size, density * size ** 2)
        elif type=='green':
            particle = GreenParticle(x, y, size, density * size ** 2)
        elif type=='blue':
            particle = BlueParticle(x, y, size, density * size ** 2)
        particle.speed = random.random()
        particle.angle = random.uniform(0, math.pi * 2)
        my_particles.append(particle)


def addVectors(angle1, length1, angle2, length2):
    x = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y = math.cos(angle1) * length1 + math.cos(angle2) * length2

    angle = 0.5 * math.pi - math.atan2(y, x)
    length = math.hypot(x, y)

    return (angle, length)


def findParticle(particles, x, y):
    for p in particles:
        if math.hypot(p.x - x, p.y - y) <= p.size:
            return p
    return None


def collide(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y

    dist = math.hypot(dx, dy)
    if dist < p1.size + p2.size:
        angle = math.atan2(dy, dx) + 0.5 * math.pi
        total_mass = p1.mass + p2.mass

        (p1.angle, p1.speed) = addVectors(p1.angle, p1.speed * (p1.mass - p2.mass) / total_mass, angle,
                                          2 * p2.speed * p2.mass / total_mass)
        (p2.angle, p2.speed) = addVectors(p2.angle, p2.speed * (p2.mass - p1.mass) / total_mass, angle + math.pi,
                                          2 * p1.speed * p1.mass / total_mass)
        p1.speed *= elasticity
        p2.speed *= elasticity

        overlap = 0.5 * (p1.size + p2.size - dist + 1)
        p1.x += math.sin(angle) * overlap
        p1.y -= math.cos(angle) * overlap
        p2.x -= math.sin(angle) * overlap
        p2.y += math.cos(angle) * overlap


class Particle():
    colour = (0,0,0)
    def __init__(self, x, y, size, mass=1):
        self.x = x
        self.y = y
        self.size = size

        self.thickness = 0
        self.speed = 0
        self.angle = 0
        self.mass = mass
        self.drag = (self.mass / (self.mass + mass_of_air)) ** self.size

    def display(self):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)

    def move(self):
        self.angle, self.speed = addVectors(self.angle, self.speed, gravity[0], gravity[1])
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        self.speed *= self.drag

    def bounce(self):
        if self.x > width - self.size:
            self.x = 2 * (width - self.size) - self.x
            self.angle = - self.angle
            self.speed *= elasticity

        elif self.x < self.size:
            self.x = 2 * self.size - self.x
            self.angle = - self.angle
            self.speed *= elasticity

        if self.y > height - self.size:
            self.y = 2 * (height - self.size) - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity

        elif self.y < self.size:
            self.y = 2 * self.size - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity


class RedParticle(Particle):
    colour = (255,0,0)
class GreenParticle(Particle):
    colour = (0,255,0)
class BlueParticle(Particle):
    colour = (0,0,255)



def run():
    global number_of_particles
    factory = ParticleFactory()
    pygame.display.set_caption('Particle Simulation')

    for i in range(number_of_particles):
        factory.create_particle('blue')

    selected_particle = None
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    number_of_particles = number_of_particles +1
                    factory.create_particle('red')
                elif event.key == pygame.K_g:
                    number_of_particles = number_of_particles +1
                    factory.create_particle('green')
                elif event.key == pygame.K_b:
                    number_of_particles = number_of_particles +1
                    factory.create_particle('blue')

            elif event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                selected_particle = findParticle(my_particles, mouseX, mouseY)
            elif event.type == pygame.MOUSEBUTTONUP:
                selected_particle = None

        if selected_particle:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            dx = mouseX - selected_particle.x
            dy = mouseY - selected_particle.y
            selected_particle.angle = 0.5 * math.pi + math.atan2(dy, dx)
            selected_particle.speed = math.hypot(dx, dy) * 0.1

        screen.fill(background_colour)

        for i, particle in enumerate(my_particles):
            particle.move()
            particle.bounce()
            for particle2 in my_particles[i + 1:]:
                collide(particle, particle2)
            particle.display()

        pygame.display.flip()


run()