import pygame
from pygame.locals import *
from graphics_functions import *
from linked_list import LinkedList

def main():
    pygame.init()
    display = [1728, 1117]
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glFrustum(-0.0128, 0.0128, -0.0083, 0.0083, 0.02, 1000)
    glTranslatef(0, 0, -5)
    camera_pos_x = 0
    camera_pos_y = 0
    saved_states = LinkedList()
    once_pressed = False
    button_count = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    print(f"Clic izquierdo en: {x}, {y}")
                    if 56 <= x <= 323 and 37 <= y <= 168:
                        if once_pressed:
                            button_count += 1
                        once_pressed = True
                        saved_states.insert([camera_pos_x, camera_pos_y])
                        camera_pos_x += 2
                        camera_pos_y = math.cos(button_count)
        glClearColor(0.2, 0.3, 0.3, 1.0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        generateCircle(camera_pos_x - camera_pos_x, camera_pos_y - camera_pos_y, 360, 0.2)
        current_node = saved_states.head
        if once_pressed == True:
            generateCircle(saved_states.head.node_data[0] - camera_pos_x, saved_states.head.node_data[1] - camera_pos_y, 360, 0.2)
            if button_count == 0:
                generateLine(saved_states.head.node_data[0] - camera_pos_x, saved_states.head.node_data[1] - camera_pos_y, camera_pos_x - camera_pos_x, camera_pos_y - camera_pos_y)
            else:
                generateLine(saved_states.tail.node_data[0] - camera_pos_x, saved_states.tail.node_data[1] - camera_pos_y, camera_pos_x - camera_pos_x, camera_pos_y - camera_pos_y)
            for i in range(button_count):
                generateCircle(current_node.next.node_data[0] - camera_pos_x, current_node.next.node_data[1] - camera_pos_y, 360, 0.2)
                generateLine(current_node.node_data[0] - camera_pos_x, current_node.node_data[1] - camera_pos_y, current_node.next.node_data[0] - camera_pos_x, current_node.next.node_data[1] - camera_pos_y)
                current_node = current_node.next
        generateButton(camera_pos_x - 2.5 - camera_pos_x, camera_pos_y + 1.7 - camera_pos_y, 0.5, 1, 0, 0, 0.8)
        generateButton(camera_pos_x - 2.5 - camera_pos_x, camera_pos_y + 1.1 - camera_pos_y, 0.5, 1, 0, 0.8, 0.8)
        generateButton(camera_pos_x - 2.5 - camera_pos_x, camera_pos_y + 0.5 - camera_pos_y, 0.5, 1, 0, 0.8, 0)
        pygame.display.flip()
        pygame.time.wait(10)

main()