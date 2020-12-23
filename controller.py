#not used yet

import os
import pprint
import pygame

class PS4Controller(object):#https://gist.github.com/claymcleod/028386b860b75e4f5472
    """Class representing the PS4 controller. Pretty straightforward functionality."""

    controller = None
    axis_data = None
    button_data = None
    hat_data = None

    def init(self):
        """Initialize the joystick components"""
        
        pygame.init()
        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

    def listen(self):
        """Listen for events to happen"""
        
        if not self.axis_data:
            self.axis_data = {}

        if not self.button_data:
            self.button_data = {}
            for i in range(self.controller.get_numbuttons()):
                self.button_data[i] = False

        if not self.hat_data:
            self.hat_data = {}
            for i in range(self.controller.get_numhats()):
                self.hat_data[i] = (0, 0)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    if event.axis == 0:
                        if event.value > 0.1:
                            print("right")
                        if event.value < -0.1:
                            print("left")
                    if event.axis == 1:
                        if event.value > 0.1:
                            print ("down")
                        if event.value < -0.1:
                            print ("up")
                elif event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 1:
                        print ("wow pressed the X button")
                elif event.type == pygame.JOYBUTTONUP:
                    if event.button == 1:
                        print ("he-yump")
                elif event.type == pygame.JOYHATMOTION:
                    if event.hat == 0:
                        if event.value == (1, 0):
                            print ("right")
                        if event.value == (-1, 0):
                            print ("left")
                        if event.value == (0, 1):
                            print ("up")
                        if event.value == (0, -1):
                            print ("down")

                # Insert your code on what you would like to happen for each event here!
                # In the current setup, I have the state simply printing out to the screen.

                #os.system('clear')
                #pprint.pprint(self.button_data)
                #pprint.pprint(self.axis_data)
                #pprint.pprint(self.hat_data)


if __name__ == "__main__":
    ps4 = PS4Controller()
    ps4.init()
    ps4.listen()