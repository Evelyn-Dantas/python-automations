import pyautogui
import time

pyautogui.alert(text='The automation code is starting DO NOT touch your mouse or keyboard. Just wait till the end of the code.', title='WARNING!')
pyautogui.PAUSE = 0.8

pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')

time.sleep(1)
pyautogui.write('https://drive.google.com/drive/u/0/my-drive')
pyautogui.press('enter')

pyautogui.hotkey('winleft', 'd')
time.sleep(1)

# Pegando valor da posição do cursor do mouse na tela onde o arquivo Vendas.xlsx está
# pyautogui.position()
# print(pyautogui.position())

pyautogui.moveTo(42, 246)
pyautogui.mouseDown()
time.sleep(1)

pyautogui.moveTo(870, 493)
time.sleep(0.5)
pyautogui.hotkey('alt', 'tab')
time.sleep(1.5)

pyautogui.mouseUp()
time.sleep(5)

delete_file = pyautogui.confirm(text='Would you like to delete this file now?', title='WARNING!', buttons=['Yes', 'No']);

if delete_file == 'Yes': 
    time.sleep(1)
    pyautogui.moveTo(98, 374)
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.moveTo(379, 388)
    pyautogui.leftClick()
    time.sleep(2)
    pyautogui.leftClick() 
    time.sleep(1)
    pyautogui.press('del', presses=2)
    time.sleep(1.5)
    pyautogui.alert(text='The file has been deleted successfully!', title='SUCCESS!')
    time.sleep(2.5)
            
    pyautogui.alert(text='The automation finished now you can use your computer normally. Thanks for your patience :)', title='WARNING!')

else:
    time.sleep(1);   
    pyautogui.alert('The automation finished now you can use your computer normally. Thanks for your patience :)', title='WARNING!')
    exit(404)
