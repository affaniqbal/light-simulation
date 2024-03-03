import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Light Simulation")

# List to store light sources
light_sources = []

# List to store walls
walls = [
    pygame.Rect(100, 150, 20, 200),
    pygame.Rect(300, 100, 20, 200),
    pygame.Rect(500, 150, 20, 200),
]

# Number of rays
num_rays = 36  # Change the number of rays as needed

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Add light source on mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            light_sources.append(list(event.pos))

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw walls
    for wall in walls:
        pygame.draw.rect(screen, (0, 0, 0), wall)

    # Draw light sources and evenly spaced light rays
    for light_source in light_sources:
        pygame.draw.circle(screen, (255, 255, 0), light_source, 10)

        for i in range(num_rays):
            # Calculate evenly spaced angles
            angle = i * (360 / num_rays)

            # Convert angle to radians
            radians = math.radians(angle)

            # Calculate endpoint of light ray
            end_x = int(light_source[0] + 500 * math.cos(radians))
            end_y = int(light_source[1] + 500 * math.sin(radians))

            # Draw the light ray
            pygame.draw.line(screen, (255, 255, 0), light_source, (end_x, end_y), 2)

            # Check for wall collisions and simulate reflection
            ray = pygame.Rect(light_source[0], light_source[1], end_x - light_source[0], end_y - light_source[1])
            for wall in walls:
                if ray.colliderect(wall):
                    print(f"Collision detected with wall {wall}")

                    # Calculate reflection angle using the vector between the center of the wall and the point of incidence
                    wall_center = (wall.centerx, wall.centery)
                    incident_vector = (end_x - wall_center[0], end_y - wall_center[1])
                    reflection_vector = (-incident_vector[0], -incident_vector[1])

                    # Update endpoint of light ray after reflection
                    reflection_angle = math.atan2(reflection_vector[1], reflection_vector[0])
                    new_angle = radians + 2 * reflection_angle

                    end_x = int(light_source[0] + 500 * math.cos(new_angle))
                    end_y = int(light_source[1] + 500 * math.sin(new_angle))

                    # Draw the reflected light ray
                    pygame.draw.line(screen, (255, 255, 0), light_source, (end_x, end_y), 2)

    pygame.display.flip()
