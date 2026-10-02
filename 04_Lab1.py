import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, 1, 1),
    (1, 1, -1),
    (1, -1, -1),
    (1, -1, 1),
    (-1, 1, 1),
    (-1, -1, -1),
    (-1, -1, 1),
    (-1, 1, -1)
)

triangles = (
    
    (0, 3, 2),
    (0, 2, 1),
  
    (4, 7, 5),
    (4, 5, 6),
   
    (0, 4, 6),
    (0, 6, 3),

    (1, 2, 5),
    (1, 5, 7),
  
    (0, 1, 7),
    (0, 7, 4),

    (3, 6, 5),
    (3, 5, 2)
)


face_colors = (
    (1, 0, 0), 
    (0, 1, 0),  
    (0, 0, 1), 
    (1, 1, 0),  
    (1, 0, 1),  
    (0, 1, 1)   
)


def draw_cube():
    glBegin(GL_TRIANGLES)
    for triangle_index, triangle in enumerate(triangles):
        if triangle_index % 2 == 0:
            glColor3f(*face_colors[triangle_index // 2])
        for vertex in triangle:
            glVertex3fv(vertices[vertex])
    glEnd()


def apply_controls(keys, delta_time):
    move_step = 2.0 * delta_time
    rotate_step = 90.0 * delta_time
    scale_step = 1.8 ** delta_time

    if keys[pygame.K_a]:
        glTranslatef(-move_step, 0, 0)
    if keys[pygame.K_d]:
        glTranslatef(move_step, 0, 0)
    if keys[pygame.K_w]:
        glTranslatef(0, move_step, 0)
    if keys[pygame.K_s]:
        glTranslatef(0, -move_step, 0)

    if keys[pygame.K_LEFT]:
        glRotatef(rotate_step, 0, 1, 0)
    if keys[pygame.K_RIGHT]:
        glRotatef(-rotate_step, 0, 1, 0)
    if keys[pygame.K_UP]:
        glRotatef(rotate_step, 1, 0, 0)
    if keys[pygame.K_DOWN]:
        glRotatef(-rotate_step, 1, 0, 0)

    if keys[pygame.K_z]:
        glScalef(1 / scale_step, 1 / scale_step, 1 / scale_step)
    if keys[pygame.K_x]:
        glScalef(scale_step, scale_step, scale_step)

pygame.init()

display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

pygame.display.set_caption("04 Lab 1")

glEnable(GL_DEPTH_TEST)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0, 0, -5)
glScalef(0.7, 0.7, 0.7)

clock = pygame.time.Clock()

while True:
    delta_time = min(clock.tick(60) / 1000.0, 0.05)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    keys = pygame.key.get_pressed()
    apply_controls(keys, delta_time)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_cube()
    pygame.display.flip()
