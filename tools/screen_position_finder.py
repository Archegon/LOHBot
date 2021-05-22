import pyautogui
import time
import pyperclip
from pynput.mouse import Listener
from game import loh


click = 0
left_top1 = None
right_bottom1 = None

TYPE = pyautogui.confirm(text='Choose Mode', title='Coords Finder',
                         buttons=['button', 'region', 'region hold', 'cancel'])
loh.g_window.set_focus()
time.sleep(1)

if TYPE == 'button':
    print('Start Clicking')


    def is_clicked(x, y, button, pressed):
        if pressed:
            if button == button.left:
                absolute_x, absolute_y = pyautogui.position()
                relative_x = absolute_x - loh.start_position()[0]
                relative_y = absolute_y - loh.start_position()[1]
                txt = None

                if relative_x >= 0 and relative_y >= 0:
                    txt = f'Point({loh.size()[0]}, {loh.size()[1]}, {relative_x}, {relative_y})'
                    print(f'Position: {relative_x}, {relative_y}')
                    pyperclip.copy(txt)
                    print("Coords Copied to clipboard!")
                else:
                    pyautogui.alert('Out of Range!', title='Coords')
            return False  # to stop the thread after click


    with Listener(on_click=is_clicked) as listener:
        listener.join()

elif TYPE == 'region':
    print('Start Clicking')


    def is_clicked(x, y, button, pressed):

        global click, left_top1, right_bottom1
        if pressed:
            click += 1
            print(click)
            if click == 1:
                if button == button.left:
                    absolute_x, absolute_y = pyautogui.position()
                    relative_x = absolute_x - loh.start_position()[0]
                    relative_y = absolute_y - loh.start_position()[1]

                    if relative_x >= 0 and relative_y >= 0:
                        left_top1 = (relative_x, relative_y)
                        print(f'Left Top: {left_top1}')
                    else:
                        pyautogui.alert('Out of Range!', title='Coords')
            if click == 2:
                if button == button.left:
                    absolute_x, absolute_y = pyautogui.position()
                    relative_x = absolute_x - loh.start_position()[0]
                    relative_y = absolute_y - loh.start_position()[1]

                    if relative_x >= 0 and relative_y >= 0:
                        right_bottom1 = (relative_x, relative_y)
                        print(f'Right Bottom: {right_bottom1}')
                        txt1 = f'Region({loh.size()[0]}, {loh.size()[1]}, {left_top1[0]}, {left_top1[1]}, {right_bottom1[0]}, {right_bottom1[1]})'
                        pyperclip.copy(txt1)
                        print("Coords Copied to clipboard!")
                    else:
                        pyautogui.alert('Out of Range!', title='Coords')

                return False


    with Listener(on_click=is_clicked) as listener:
        listener.join()

elif TYPE == 'region hold':
    print('Start')


    def is_clicked(x, y, button, pressed):

        global click, left_top1, right_bottom1
        if pressed:
            print(click)
            if button == button.left:
                absolute_x, absolute_y = pyautogui.position()
                relative_x = absolute_x - loh.start_position()[0]
                relative_y = absolute_y - loh.start_position()[1]

                if relative_x >= 0 and relative_y >= 0:
                    left_top1 = (relative_x, relative_y)
                    print(f'Left Top: {left_top1}')
                else:
                    pyautogui.alert('Out of Range!', title='Coords')
        if not pressed:
            if button == button.left:
                absolute_x, absolute_y = pyautogui.position()
                relative_x = absolute_x - loh.start_position()[0]
                relative_y = absolute_y - loh.start_position()[1]

                if relative_x >= 0 and relative_y >= 0:
                    right_bottom1 = (relative_x, relative_y)
                    print(f'Right Bottom: {right_bottom1}')
                    txt1 = f'Region({loh.size()[0]}, {loh.size()[1]}, {left_top1[0]}, {left_top1[1]}, {right_bottom1[0]}, {right_bottom1[1]})'
                    pyperclip.copy(txt1)
                    print("Coords Copied to clipboard!")
                else:
                    pyautogui.alert('Out of Range!', title='Coords')

            return False


    with Listener(on_click=is_clicked) as listener:
        listener.join()
elif TYPE == 'cancel':
    exit()
