from constants import *
from circleshape import CircleShape
import random
import pygame

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt
    
  def split(self):
    self.kill()
    angle = random.uniform(20, 50)
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    if self.radius > ASTEROID_MIN_RADIUS and self.radius < ASTEROID_MAX_RADIUS:
      asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
      asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
      asteroid_1.velocity = self.velocity.rotate(angle) * 1.2
      asteroid_2.velocity = self.velocity.rotate(-angle) * 1.2
    if self.radius >= ASTEROID_MAX_RADIUS:
      asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
      asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
      asteroid_1.velocity = self.velocity.rotate(angle) * 1.2
      asteroid_2.velocity = self.velocity.rotate(-angle) * 1.2