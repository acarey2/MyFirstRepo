import pyautogui as pg
import time

pg.hotkey('winleft', 'cnrl', 'd')
pg.hotkey('winleft')
pg.typewrite ('chrome\n', .05)


website= pg.prompt('What website do you want to visit?')
pg.typewrite ((website + "\n"),0.5)

answer= pg.confirm('Do you want to open a new tab')
if answer == 'OK':
    pg.hotkey('cnrl','t')
