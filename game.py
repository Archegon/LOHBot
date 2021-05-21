import time
import cv2
import numpy as np
import pyautogui
from ocr import Ocr
from pywinauto import Application


APP_PATH = r'C:\Program Files\BlueStacks_bgp64\HD-RunApp.exe -json "{\"app_icon_url\":\"\",' \
           r'\"app_name\":\"LordOfHeroes\",\"app_url\":\"\",\"app_pkg\":\"com.clovergames.lordofheroes\"} '


class Game:
    ocr = Ocr()

    def __init__(self, path):
        self.path = path
        self.g_window = None
        self.b_window = None
        self.img = None
        self.width = None
        self.height = None
        self.region_img_path = 'images/game_region.png'
        self.game_img_path = 'images/game_screenshot.png'
        self.__start_x = None
        self.__start_y = None

    def start(self):
        Application().start(self.path, timeout=10)
        time.sleep(5)
        app = Application().connect(best_match='KeymapCanvasWindow', top_level_only=False, visible_only=False,
                                    timeout=10)
        win_str = "KeymapCanvasWindow"
        self.g_window = app.window(best_match=win_str, top_level_only=False, visible_only=False)
        self.b_window = app.window(title='BlueStacks')
        self.g_window.set_focus()
        self.g_window.wait('exists', timeout=20)
        print('GAME WINDOW READY')

    def set_focus(self):
        self.g_window.set_focus()
        time.sleep(0.2)

    def set_keyboard_focus(self):
        self.b_window.set_keyboard_focus()
        time.sleep(0.2)

    def save(self):
        self.set_focus()
        self.img = self.g_window.capture_as_image()
        self.img = cv2.cvtColor(np.array(self.img), cv2.COLOR_RGB2BGR)
        cv2.imwrite(self.game_img_path, self.img)

        return self.img

    def window_size(self):
        return self.g_window.rectangle().width(), self.g_window.rectangle().height()

    def save_region(self, region):
        width = region[2] - region[0]
        height = region[3] - region[1]

        self.set_focus()
        self.img = pyautogui.screenshot(region=(region[0], region[1], width, height))
        self.img = cv2.cvtColor(np.array(self.img), cv2.COLOR_RGB2BGR)
        cv2.imwrite(self.region_img_path, self.img)

        return self.img

    def read_region(self, region, visualize=False):
        width = region[2] - region[0]
        height = region[3] - region[1]

        self.set_focus()
        self.img = pyautogui.screenshot(region=(region[0], region[1], width, height))
        self.img = cv2.cvtColor(np.array(self.img), cv2.COLOR_RGB2BGR)
        cv2.imwrite(self.region_img_path, self.img)

        return Game.ocr.read(self.region_img_path, visualize=visualize)

    def size(self):
        self.width = self.g_window.rectangle().width()
        self.height = self.g_window.rectangle().height()
        return self.width, self.height

    def start_position(self):
        self.__start_x = self.g_window.rectangle().left
        self.__start_y = self.g_window.rectangle().top
        return self.__start_x, self.__start_y


loh = Game(APP_PATH)
