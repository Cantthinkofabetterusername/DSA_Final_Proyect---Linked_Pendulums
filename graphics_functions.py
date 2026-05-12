from OpenGL.GL import *
import math

def generateCircle(center_x, center_y, segments, radius):
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.7, 0, 0)
    for i in range(segments):
        angle = 2 * math.pi * i / segments
        x_coordinate = center_x + radius * math.cos(angle)
        y_coordinate = center_y + radius * math.sin(angle)
        glVertex2f(x_coordinate, y_coordinate)
    glColor3f(1, 1, 1)
    glEnd()

def generateButton(center_x, center_y, height, width, R, G, B):
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(R, G, B)
    glVertex2f(center_x - width / 2, center_y + height / 2)
    glVertex2f(center_x + width / 2, center_y + height / 2)
    glVertex2f(center_x + width / 2, center_y - height / 2)
    glVertex2f(center_x - width / 2, center_y - height / 2)
    glColor3f(1, 1, 1)
    glEnd()

def generateLine(previous_x, previous_y, current_x, current_y):
    glBegin(GL_LINES)
    glColor3f(0.7, 0, 0)
    glVertex2f(previous_x, previous_y)
    glVertex2f(current_x, current_y)
    glColor3f(1, 1, 1)
    glEnd()