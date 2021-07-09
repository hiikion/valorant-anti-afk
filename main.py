import time
import keyboard
import random

print('''
   __    _  _  ____  ____        __    ____  _  _     
  /__\  ( \( )(_  _)(_  _)      /__\  ( ___)( )/ )    
 /(  )\  )  (   )(   _)(_      /(  )\  )__)  )  (     
(__)(__)(_)\_) (__) (____)    (__)(__)(_)   (_)\_)    
            »»-by hkon aka hiikion -►
''')


def main():
    time.sleep(5)
    while True:
        rndint = random.randint(1, 6)
        rslp = random.random()
        if rndint == 1:
            keyboard.press('w')
            time.sleep(rslp)
            keyboard.release('w')
        elif rndint == 2:
            keyboard.press('a')
            time.sleep(rslp)
            keyboard.release('a')
        elif rndint == 3:
            keyboard.press('s')
            time.sleep(rslp)
            keyboard.release('s')
        elif rndint == 4:
            keyboard.press('d')
            time.sleep(rslp)
            keyboard.release('d')
        elif rndint == 5:
            keyboard.press('control')
            time.sleep(rslp)
            keyboard.release('control')
        elif rndint == 5:
            keyboard.press('space')
            time.sleep(rslp)
            keyboard.release('space')
        elif rndint == 90:
            print('stop, how the fuck is it 90')


if __name__ == '__main__':
    main()
