import pyautogui
import time

def find_and_click_button(image_filename, confidence=0.75, retry_count=2, pause=0.1):
    """
    Attempts to find and click a button on the screen based on an image.
    Retries a specified number of times with a delay between each attempt.
    """
    for attempt in range(retry_count):
        location = pyautogui.locateCenterOnScreen(image_filename, confidence=confidence)
        if location:
            pyautogui.moveTo(location)
            pyautogui.click()
            time.sleep(pause)
            return True
        time.sleep(0.5)  # Delay between retries
    return False

def remove_friends(number_of_friends, steps):
    """
    Automates the process of removing a specified number of friends.
    """
    for _ in range(number_of_friends):
        for step in steps:
            if not find_and_click_button(step['image'], step['confidence'], step['retry_count'], step['pause']):
                return  # Stop the process if a step fails
            print("Done removing friends.")

number_of_friends = 50  # Number of friends to remove
steps = [
    {'image': 'screenshot1.png', 'confidence': 0.75, 'retry_count': 2, 'pause': 0.1},
    {'image': 'screenshot2.png', 'confidence': 0.75, 'retry_count': 2, 'pause': 0.1},
    {'image': 'screenshot3.png', 'confidence': 0.75, 'retry_count': 2, 'pause': 0.1},
    {'image': 'screenshot4.png', 'confidence': 0.75, 'retry_count': 2, 'pause': 0.25},
    {'image': 'screenshot1.png', 'confidence': 0.75, 'retry_count': 2, 'pause': 0.1},
    {'image': 'screenshot1.png', 'confidence': 0.75, 'retry_count': 2, 'pause': 0.1}
]

remove_friends(number_of_friends, steps)
