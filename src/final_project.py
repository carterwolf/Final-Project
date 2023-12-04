import pygame
import random
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Text Glitch, Fade, and Disappear Effect')

font = pygame.font.SysFont('Arial', 36)

def glitch_text(text):
    glitched_text = ''
    for char in text:
        glitched_text += char + ''.join(random.choice(['', ' ', '  ', '   ', '    ']))
    return glitched_text

def glitch_color(color):
    def clamp(value, minimum, maximum):
        return max(minimum, min(value, maximum))

    return (
        clamp(color[0] + random.randint(-50, 50), 0, 255),
        clamp(color[1] + random.randint(-50, 50), 0, 255),
        clamp(color[2] + random.randint(-50, 50), 0, 255)
    )

start_time = pygame.time.get_ticks()
glitch_duration = 5000 
fade_duration = 5000   
image_display_duration = 5000  

image = pygame.image.load('Failure and Success.png')  

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()  
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    elapsed_time = pygame.time.get_ticks() - start_time

    if elapsed_time < glitch_duration:
        original_text = "FAILURE"
        text_color = (255, 255, 255)
    else:
        original_text = "IS THE KEY TO SUCCESS"
        original_text += ''.join(random.choice(['', ' ', '  ', '   ', '    ']))  
        text_color = glitch_color((255, 0, 0))

        fade_start_time = glitch_duration
        fade_elapsed_time = elapsed_time - fade_start_time
        if fade_elapsed_time < fade_duration:
            fade_factor = 1 - fade_elapsed_time / fade_duration
            text_color = (
                int(text_color[0] * fade_factor),
                int(text_color[1] * fade_factor),
                int(text_color[2] * fade_factor)
            )
        else:
            image_start_time = fade_start_time + fade_duration
            image_elapsed_time = elapsed_time - image_start_time
            if image_elapsed_time < image_display_duration:
                screen.blit(image, (width / 2 - image.get_width() / 2, height / 2 - image.get_height() / 2))
            else:
                pygame.mixer.music.stop()  
                pygame.quit()
                sys.exit()

    text_surface = font.render(original_text, True, text_color)
    text_rect = text_surface.get_rect(center=(width / 2, height / 2))

    screen.blit(text_surface, text_rect)

    pygame.display.flip()

    pygame.time.Clock().tick(60)
