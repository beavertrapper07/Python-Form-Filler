#! python3
# formFiller.py - Automatically fills in the form.

import pyautogui, time, csv
# https://docs.google.com/forms/d/e/1FAIpQLScSVDFU76rZvbO_tiIwSt6d9sOK0CZyS9KKMCP6cP5O5W5lVQ/viewform
# Set these to the correct coordinates for your particular computer.
nameField = (1862, 513)
submitButton = (1851, 718)
submitButtonColor = (69, 132, 239)
submitAnotherLink = (1885, 490)

# Open csv data
with open('testbrad.csv', 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)


pyautogui.PAUSE = 0.5

for person in your_list:
    # Give the user a chance to kill the script.
    print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(5)

    # Wait until the form page has loaded.
    while not pyautogui.pixelMatchesColor(submitButton[0], submitButton[1], submitButtonColor):
        time.sleep(0.5)


    pyautogui.click(nameField[0], nameField[1])

    # Fill out the Name field.
    pyautogui.typewrite(person[0] + '\t')

    # Fill out the Email field.
    pyautogui.typewrite(person[2] + '\t')


    # Click Submit.
    pyautogui.press('enter')

    # Wait until form page has loaded.
    print('Clicked Submit.')
    time.sleep(5)

    # Click the Submit another response link.
    pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])