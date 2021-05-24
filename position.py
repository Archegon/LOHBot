import abc
import time
import pyautogui
import cv2
import re
from game import loh


class BasePosition(metaclass=abc.ABCMeta):
    # Set game object to LordOfHeros
    game = loh
    window_w = game.window_size()[0]
    window_h = game.window_size()[1]
    start_left = game.start_position()[0]
    start_top = game.start_position()[1]

    def __init__(self, w, h, left, top, right=None, bottom=None):
        self.scale = BasePosition.window_w / w
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    def get_relative(self):
        if self.right is None and self.bottom is None:
            relative_left = round(self.left * self.scale)
            relative_top = round(self.top * self.scale)
            return relative_left, relative_top
        else:
            relative_left = round(self.left * self.scale)
            relative_top = round(self.top * self.scale)
            relative_right = round(self.right * self.scale)
            relative_bottom = round(self.bottom * self.scale)

            return relative_left, relative_top, relative_right, relative_bottom

    def get_absolute(self):
        if self.right is None and self.bottom is None:
            absolute_left = self.get_relative()[0] + BasePosition.start_left
            absolute_top = self.get_relative()[1] + BasePosition.start_top

            return absolute_left, absolute_top
        else:
            absolute_left = self.get_relative()[0] + BasePosition.start_left
            absolute_top = self.get_relative()[1] + BasePosition.start_top
            absolute_right = self.get_relative()[2] + BasePosition.start_left
            absolute_bottom = self.get_relative()[3] + BasePosition.start_top

            return absolute_left, absolute_top, absolute_right, absolute_bottom

    @abc.abstractmethod
    def position(self, absolute=True):
        pass

    def click(self):
        if self.right is None and self.bottom is None:
            pyautogui.click(self.position())
        else:
            center_x = (self.position()[0] + self.position()[2]) / 2
            center_y = (self.position()[1] + self.position()[3]) / 2

            pyautogui.click((center_x, center_y))

        time.sleep(2)

    @staticmethod
    def print(txt):
        return print('\tPosition Class: ' + txt)


class Point(BasePosition):
    def __init__(self, w, h, left, top):
        super().__init__(w, h, left, top)

    def position(self, absolute=True):
        if absolute:
            return self.get_absolute()[0], self.get_absolute()[1]
        else:
            return self.get_relative()[1], self.get_relative()[0]


class Region(BasePosition):
    def __init__(self, w, h, left, top, right, bottom):
        super().__init__(w, h, left, top, right, bottom)
        self.img = None

    def position(self, absolute=True):
        if absolute:
            return self.get_absolute()[0], self.get_absolute()[1], self.get_absolute()[2], self.get_absolute()[3]
        else:
            return self.get_relative()[0], self.get_relative()[1], self.get_relative()[2], self.get_relative()[3]

    def read(self, visualize=False):
        return Region.game.read_region(self.position(), visualize=visualize)

    def check_for(self, check_str='None', visualize=False, filter_str=False):
        read = self.read(visualize=visualize)

        if len(read):
            read = read[0][1]

            if filter_str:
                read = re.sub(r"[^a-zA-Z0-9 ]+", '', read)

            Region.print(f'Result: {read.upper()}  Check: {check_str.upper()}')

            if read.upper() == check_str.upper():
                return True
            else:
                return False
        else:
            Region.print("No Result")
            return False

    def check_empty(self, visualize=False):
        if not len(self.read(visualize=visualize)):
            return True
        else:
            return False

    def save(self):
        self.img = Region.game.save_region(self.position())

        return self.img

    def locate(self, check_str, visualize=False):
        result_location = None

        if not self.check_empty():
            for detection in self.read(visualize=visualize):
                if detection[1].upper() == check_str.upper():
                    result_location = detection[0]

        if result_location is None:
            return None

        left = result_location[0][0]
        top = result_location[0][1]
        right = result_location[2][0]
        bottom = result_location[2][1]

        if visualize:
            self.img = self.save()
            self.img = cv2.rectangle(self.img, (left, top), (right, bottom),
                                     (0, 255, 0), 2)
            cv2.imshow('Locate', self.img)
            cv2.waitKey(0)

        left_relative = left + self.position(absolute=False)[0]
        top_relative = top + self.position(absolute=False)[1]
        right_relative = right + self.position(absolute=False)[0]
        bottom_relative = bottom + self.position(absolute=False)[1]

        left_absolute = left_relative + Region.start_left
        top_absolute = top_relative + Region.start_top
        right_absolute = right_relative + Region.start_left
        bottom_absolute = bottom_relative + Region.start_top

        center_x = round((left_absolute + right_absolute) / 2)
        center_y = round((bottom_absolute + top_absolute) / 2)

        # Return the center of rectangle.
        return center_x, center_y

    def locate_click(self, check_str, visualize=False):
        pyautogui.click(self.locate(check_str, visualize=visualize))
        time.sleep(0.5)

    def draw(self):
        self.img = Region.game.save()
        self.img = cv2.imread(self.img)
        self.img = cv2.rectangle(self.img, (self.position(absolute=False)[0], self.position(absolute=False)[1]),
                                 (self.position(absolute=False)[2], self.position(absolute=False)[3]),
                                 (0, 255, 0), 2)
        cv2.imshow('Result', self.img)
        cv2.waitKey(0)
