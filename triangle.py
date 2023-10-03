# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    triangle.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mugwu <mugwu@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/01 08:38:48 by mugwu             #+#    #+#              #
#    Updated: 2023/10/01 09:06:19 by mugwu            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

# Define the vertices of the triangle
vertices = [
    [0, 1, 0],
    [-1, -1, 0],
    [1, -1, 0]
]

# Define the colors for each vertex
colors = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

# Rotation angle
angle = 0.0  # Initialize the angle

def draw_triangle():
    glBegin(GL_TRIANGLES)
    for i in range(3):
        glColor3fv(colors[i])
        glVertex3fv(vertices[i])
    glEnd()

def set_projection_matrix():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-1, 1, -1, 1, 1, 50.0)  # Set up a perspective projection matrix
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5)

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    set_projection_matrix()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        global angle
        glRotatef(1.0, 1.0, 1.0, 1.0)  # Rotate the triangle (adjust angle for speed)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_triangle()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
