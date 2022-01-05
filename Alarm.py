import time
import winsound

def alarme_min(n):
    n *= 60
    while n:
        m, s = divmod(n, 60)
        print('{:02}:{:02}'.format(m, s), end='\r')
        time.sleep(1)
        n -= 1
        
    winsound.Beep(440, 2000)

def main():
    print('Simple Alarm')
    n = int(input('How many minutes? '))
    alarme_min(n)

if __name__ == '__main__':
    main()
