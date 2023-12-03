import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Text Glitch, Fade, and Disappear Effect')

# Set up fonts
font = pygame.font.SysFont('Arial', 36)

# Function to create glitched text
def glitch_text(text):
    glitched_text = ''
    for char in text:
        glitched_text += char + ''.join(random.choice(['', ' ', '  ', '   ', '    ']))
    return glitched_text

# Function to create glitched color
def glitch_color(color):
    def clamp(value, minimum, maximum):
        return max(minimum, min(value, maximum))

    return (
        clamp(color[0] + random.randint(-50, 50), 0, 255),
        clamp(color[1] + random.randint(-50, 50), 0, 255),
        clamp(color[2] + random.randint(-50, 50), 0, 255)
    )

# Main loop
start_time = pygame.time.get_ticks()
glitch_duration = 5000  # 5 seconds
fade_duration = 5000    # 5 seconds
image_display_duration = 5000  # 5 seconds

image = pygame.image.load('Failure and Success.png')  # Replace 'path_to_your_image.jpg' with the actual path

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()  # Stop the music when quitting
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Calculate elapsed time
    elapsed_time = pygame.time.get_ticks() - start_time

    # Display original text for 5 seconds
    if elapsed_time < glitch_duration:
        original_text = "FAILURE"
        text_color = (255, 255, 255)
    else:
        # Generate glitched text and color after 5 seconds
        original_text = "IS THE KEY TO SUCCESS"
        original_text += ''.join(random.choice(['', ' ', '  ', '   ', '    ']))  # Add glitch effect
        text_color = glitch_color((255, 0, 0))

        # Fade to black after 5 seconds of glitching
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
            # Display an image after the glitching and fading effect
            image_start_time = fade_start_time + fade_duration
            image_elapsed_time = elapsed_time - image_start_time
            if image_elapsed_time < image_display_duration:
                # Draw the image on the screen
                screen.blit(image, (width / 2 - image.get_width() / 2, height / 2 - image.get_height() / 2))
            else:
                # If total elapsed time exceeds glitch duration + fade duration + image display duration, exit the loop
                pygame.mixer.music.stop()  # Stop the music when the text disappears
                pygame.quit()
                sys.exit()

    # Render text
    text_surface = font.render(original_text, True, text_color)
    text_rect = text_surface.get_rect(center=(width / 2, height / 2))

    # Display text
    screen.blit(text_surface, text_rect)

    # Update display
    pygame.display.flip()

    # Control frame rate
    pygame.time.Clock().tick(60)
