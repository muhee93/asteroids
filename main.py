import sys
import pygame
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    
    # GROUPS
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()


    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, "black")
        updatable.update(dt)
        for thing in asteroids:
            if thing.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for thing in asteroids:
            for bullet in shots:
                if thing.collides_with(bullet):
                    log_event("asteroid_shot")
                    thing.split()
                    bullet.kill()
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    print(dt)


if __name__ == "__main__":
    main()
