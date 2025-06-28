import cv2
import numpy as np
import pyautogui
import mss
import time
import keyboard

# إعدادات اللون الأحمر في الفضاء HSV (يمكنك تعديلها لأي لون)
LOWER_COLOR = np.array([0, 120, 70])
UPPER_COLOR = np.array([10, 255, 255])

MONITOR = {"top": 100, "left": 100, "width": 800, "height": 600}

def smooth_move_to(x, y, speed=0.2):
    current_x, current_y = pyautogui.position()
    new_x = current_x + (x - current_x) * speed
    new_y = current_y + (y - current_y) * speed
    pyautogui.moveTo(new_x, new_y, duration=0.05)

def main():
    with mss.mss() as sct:
        print("اضغط F8 لتفعيل/إيقاف Aim Assist")
        enabled = False

        while True:
            if keyboard.is_pressed('F8'):
                enabled = not enabled
                print(f"Aim A
