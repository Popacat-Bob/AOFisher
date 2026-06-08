import mss 
import numpy as np 
import cv2 as cv
import time
from pyautogui import click, press
from Structs import *

DELAY = 0.75 
CLICK_INTERVAL = 0.25
FISH_KEY = "1"
LURE_KEY = "2"
RAND_KEY = "3"

class FishEventLoop:
    """ Logic handling the fishing loop """
    def __init__(self, fish_prompt_region: Rect, tolerance: int, clicks: int, color: RGB):
        self.fish_region = fish_prompt_region
        self.tol = tolerance
        self.clicks = clicks
        self.color = np.array([color.b, color.g, color.r])
        self.is_fishing = False
    
    def set_rect(self, region: Rect):
        self.fish_region = region 

    def set_is_fishing(self, status: bool):
        self.is_fishing = status 

    def detect_color(self, color: np.ndarray, region: Rect, tol: int) -> bool:
        with mss.MSS() as sc:  
            monitor = {
                "left":   region.x0,
                "top":    region.y0,
                "width":  region.x1 - region.x0,
                "height": region.y1 - region.y0,
            }
            frame = sc.grab(monitor)
 
        frame = np.array(frame)[:, :, :3]  
        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
 
        gray_color = int(0.114 * color[0] + 0.587 * color[1] + 0.299 * color[2])
 
        return bool(np.any(np.abs(gray_frame.astype(int) - gray_color) <= tol))


    def start(self):
        while self.is_fishing:
            click()
            while not self.detect_color(self.color, self.fish_region, self.tol):
                time.sleep(DELAY)

            click(interval = CLICK_INTERVAL) 
            time.sleep(DELAY)
            press(LURE_KEY)
            time.sleep(DELAY)
            click()
            time.sleep(DELAY)
            press(FISH_KEY)
            time.sleep(DELAY)
