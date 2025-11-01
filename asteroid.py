from circleshape import CircleShape
import pygame
import random

from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(angle)
        vector2 = self.velocity.rotate(-angle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        offset1 = vector1.normalize() * (new_rad * 2.0)
        offset2 = vector2.normalize() * (new_rad * 2.0)
        a1 = Asteroid(self.position.x + offset1.x, self.position.y + offset1.y, new_rad)
        a2 = Asteroid(self.position.x + offset2.x, self.position.y + offset2.y, new_rad)
        a1.velocity = vector1 * 1.2
        a2.velocity = vector2 * 1.2


