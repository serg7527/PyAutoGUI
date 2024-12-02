import os
import time
import pyautogui

# Открываем приложение Калькулятор
if os.name == 'nt':  # Windows
    os.system('start calc')
elif os.name == 'posix':  # macOS или Linux
    os.system('open -a Calculator')

# Даем время на открытие приложения
time.sleep(2)

# Определяем кнопки на экране
buttons = {
    '1': 'path/to/button_1_image.png',
    '2': 'path/to/button_2_image.png',
    '+': 'path/to/button_plus_image.png',
    '7': 'path/to/button_7_image.png',
    '=': 'path/to/button_equals_image.png'
}

# Функция для нажатия на кнопку
def press_button(button):
    position = pyautogui.locateOnScreen(buttons[button], confidence=0.9)
    if position is not None:
        pyautogui.click(position)
    else:
        print(f"Не удалось найти кнопку {button}")

# Выполняем операцию 12 + 7
press_button('1')
press_button('2')
press_button('+')
press_button('7')
press_button('=')