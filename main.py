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
    saved_times = LinkedList()
    once_pressed = False
    frozen = False
    button_count = 0
    t = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    if 55 <= x <= 324 and 37 <= y <= 168:
                        if once_pressed and frozen == False:
                            button_count += 1
                        if frozen == False:
                            once_pressed = True
                            saved_states.insert([camera_pos_x, camera_pos_y])
                            saved_times.insert(t)
                            camera_pos_x += 2
                            t = 0
                        elif frozen:
                            saved_states.move_next()
                            camera_pos_x = saved_states.current_node.node_data[0]
                            camera_pos_y = saved_states.current_node.node_data[1]
                    elif 55 <= x <= 324 and 197 <= y <= 332:
                        if once_pressed and button_count > 0 and frozen == False:
                            button_count -= 1
                            t = saved_times.tail.node_data
                            saved_states.delete()
                            saved_times.delete()
                        elif frozen:
                            saved_states.move_prev()
                            camera_pos_x = saved_states.current_node.node_data[0]
                            camera_pos_y = saved_states.current_node.node_data[1]
                    elif 55 <= x <= 324 and 357 <= y <= 496:
                        if once_pressed and button_count > 0 and frozen == False:
                            frozen = True
                            saved_states.insert([camera_pos_x, camera_pos_y])
                            saved_states.circulify()
        glClearColor(0.2, 0.3, 0.3, 1.0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        generateCircle(camera_pos_x - camera_pos_x, camera_pos_y - camera_pos_y, 360, 0.2)
        current_node = saved_states.head
        if once_pressed:
            generateCircle(saved_states.head.node_data[0] - camera_pos_x, saved_states.head.node_data[1] - camera_pos_y, 360, 0.2)
            if button_count == 0:
                generateLine(saved_states.head.node_data[0] - camera_pos_x, saved_states.head.node_data[1] - camera_pos_y, camera_pos_x - camera_pos_x, camera_pos_y - camera_pos_y)
            else:
                if frozen == False:
                    generateLine(saved_states.tail.node_data[0] - camera_pos_x, saved_states.tail.node_data[1] - camera_pos_y, camera_pos_x - camera_pos_x, camera_pos_y - camera_pos_y)
            for i in range(button_count):
                generateCircle(current_node.next.node_data[0] - camera_pos_x, current_node.next.node_data[1] - camera_pos_y, 360, 0.2)
                generateLine(current_node.node_data[0] - camera_pos_x, current_node.node_data[1] - camera_pos_y, current_node.next.node_data[0] - camera_pos_x, current_node.next.node_data[1] - camera_pos_y)
                current_node = current_node.next
            angle = (math.pi / 2) * math.e**(-0.1 * t) * math.cos(math.sqrt(4.89) * t)
            t += 0.01
            if frozen:
                generateCircle(saved_states.tail.node_data[0] - camera_pos_x, saved_states.tail.node_data[1] - camera_pos_y, 360, 0.2)
                generateLine(saved_states.tail.node_data[0] - camera_pos_x, saved_states.tail.node_data[1] - camera_pos_y, saved_states.head.node_data[0] - camera_pos_x, saved_states.head.node_data[1] - camera_pos_y)
                generateLine(saved_states.tail.prev.node_data[0] - camera_pos_x, saved_states.tail.prev.node_data[1] - camera_pos_y, saved_states.tail.node_data[0] - camera_pos_x, saved_states.tail.node_data[1] - camera_pos_y)
                generateButton(camera_pos_x - 2.5 - camera_pos_x, camera_pos_y + 1.7 - camera_pos_y, 0.5, 1, 0, 0.5, 0)
                generateButton(camera_pos_x - 2.5 - camera_pos_x, camera_pos_y + 1.1 - camera_pos_y, 0.5, 1, 0.5, 0, 0)
            else:
                camera_pos_x = 2 * math.sin(angle) + saved_states.tail.node_data[0]
                camera_pos_y = -2 * math.cos(angle) + saved_states.tail.node_data[1]
                generateButton(camera_pos_x - 2.5 - camera_pos_x, camera_pos_y + 1.7 - camera_pos_y, 0.5, 1, 0, 0, 0.8)
                generateButton(camera_pos_x - 2.5 - camera_pos_x, camera_pos_y + 1.1 - camera_pos_y, 0.5, 1, 0, 0.8, 0.8)
                generateButton(camera_pos_x - 2.5 - camera_pos_x, camera_pos_y + 0.5 - camera_pos_y, 0.5, 1, 0, 0.8, 0)
        else:
            generateButton(camera_pos_x - 2.5 - camera_pos_x, camera_pos_y + 1.7 - camera_pos_y, 0.5, 1, 0, 0, 0.8)
            generateButton(camera_pos_x - 2.5 - camera_pos_x, camera_pos_y + 1.1 - camera_pos_y, 0.5, 1, 0, 0.8, 0.8)
            generateButton(camera_pos_x - 2.5 - camera_pos_x, camera_pos_y + 0.5 - camera_pos_y, 0.5, 1, 0, 0.8, 0)
        pygame.display.flip()
        pygame.time.wait(10)

main()