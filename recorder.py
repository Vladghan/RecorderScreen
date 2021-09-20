import os
import uuid

import cv2
import keyboard
import numpy as np
import pyautogui
import winsound

# разрешение экрана дисплея, получите его в настройках вашей ОС
SCREEN_SIZE = (1280, 720)

# координаты дисплея
X1 = 352
Y1 = 237
# определяем кодек
fourcc = cv2.VideoWriter_fourcc(*"H264")
# создаем объект записи видео
if not os.path.exists('data'):
    os.mkdir('data')
keyboard.wait('shift')
winsound.Beep(400, 1000)
while True:
    out = cv2.VideoWriter(f"data/{str(uuid.uuid4())}.mp4", fourcc, 24.0, SCREEN_SIZE)

    for _ in range(240):
        # сделать скриншот
        img = pyautogui.screenshot(region=(X1, Y1, 1280, 720))
        # преобразовываем эти пиксели в правильный массив numpy для работы с OpenCV
        frame = np.array(img)
        # конвертировать цвета из BGR в RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # пишем фрейм
        out.write(frame)
        # показать рамку
        cv2.imshow("screenshot", frame)
        # если пользователь нажимает q, он выходит

    # убедитесь, что все закрыто при выходе
    cv2.destroyAllWindows()
    out.release()
    winsound.Beep(400, 1000)
    keyboard.wait('shift')
