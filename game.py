import time
import cv2
import numpy as np
import pyautogui
from ocr import Ocr
from pywinauto import Application


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
        self.app = None

    def start(self):
        Application().start(self.path, timeout=10)
        time.sleep(5)
        self.app = Application().connect(best_match='KeymapCanvasWindow', top_level_only=False, visible_only=False,
                                         timeout=30)
        win_str = "KeymapCanvasWindow"
        self.g_window = self.app.window(best_match=win_str, top_level_only=False, visible_only=False)
        self.b_window = self.app.window(best_match='BlueStacks')
        self.g_window.set_focus()
        self.g_window.wait('exists', timeout=20)
        print('GAME WINDOW READY')

    def set_focus(self):
        self.g_window.set_focus()
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

    def kill(self):
        self.app.kill()


class GameControl:
    def __init__(self, game):
        self.game = game
        self.pages = {}
        self.drags = {}

    @staticmethod
    def print(txt):
        return print('\t' + txt)

    def add_page(self, page_name, check_str, region):
        temp_dict = {
            page_name: {
                'region': region,
                'check_str': check_str
            }
        }
        self.pages.update(temp_dict)

    def at_page(self, page_name):
        try:
            if self.pages[page_name]['region'].check_for(self.pages[page_name]['check_str']):
                GameControl.print(f'At_Page: Currently at {page_name}.')
                return True
            else:
                GameControl.print(f'At_Page: NOT at {page_name}.')
                return False
        except KeyError:
            GameControl.print('At_Page: KEY NOT FOUND')

    def add_drag(self, drag_name, start_point, end_point):
        temp_dict = {
            drag_name:
                {
                    'start': start_point,
                    'end': end_point
                }
        }

        self.drags.update(temp_dict)

    def drag(self, drag_name, speed=1):
        try:
            self.game.set_focus()
            pyautogui.moveTo(*self.drags[drag_name]['start'].position())
            pyautogui.dragTo(*self.drags[drag_name]['end'].position(), speed)
            GameControl.print(f'Drag: {drag_name}')
        except KeyError:
            GameControl.print(f'Drag: KEY NOT FOUND')

    def set_quit_confirmation(self, check_str, region):
        temp_dict = {
            'quit': {
                'region': region,
                'check_str': check_str
            }
        }

        self.pages.update(temp_dict)

    def get_quit_confirmation(self):
        self.game.set_focus()

        try:
            if self.pages['quit']['region'].check_for(self.pages['quit']['check_str']):
                return True
            else:
                return False
        except KeyError:
            GameControl.print('Quit Confirmation NOT SET!')

    def back(self):
        self.game.set_focus()
        pyautogui.hotkey('ctrl', 'shift', '2')
        time.sleep(0.5)
        GameControl.print("Backed")

    def back_to_main(self, after_action=None, parameter=None):
        self.game.set_focus()

        while not self.get_quit_confirmation():
            self.back()

        self.back()
        if after_action is not None:
            after_action(parameter)
        GameControl.print('Back to Main Page.')

    def kill_program(self):
        self.game.kill()


APP_PATH = r'C:\Program Files\BlueStacks_bgp64\HD-RunApp.exe -json "{\"app_icon_url\":\"\",' \
           r'\"app_name\":\"LordOfHeroes\",\"app_url\":\"\",\"app_pkg\":\"com.clovergames.lordofheroes\"} '

loh = Game(APP_PATH)
loh.start()
game_control = GameControl(loh)
