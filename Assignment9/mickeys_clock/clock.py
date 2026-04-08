import pygame, datetime

class Clock:
    
    def __init__(self):
        self.current_time = datetime.datetime.now()
        self.minute = self.current_time.minute
        self.second = self.current_time.second

    def calculate_hand_angles(self):
        minute_angle = -self.minute * 6
        second_angle = -self.second * 6

        return minute_angle, second_angle

    def move_forward(self):
        self.second += 1

        if self.second == 60:
            self.second == 0
            self.minute += 1

        if self.minute == 60:
            self.minute = 0