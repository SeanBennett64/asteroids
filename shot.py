import pygame
from circleshape import CircleShape
from constants import *
from player import *

class Shot(CircleShape):
  def __init__(self, x, y, rotation):
    super().__init__(x, y, SHOT_RADIUS)
    self.velocity = pygame.Vector2(0, 1).rotate(rotation) * PLAYER_SHOT_SPEED

  def update(self, dt):
    self.position += self.velocity * dt

  def draw(self, screen):
    pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), SHOT_RADIUS, 2)
