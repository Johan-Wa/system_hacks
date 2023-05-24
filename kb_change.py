import os

layout_info = []

path = '/home/dracul/programing/python/system_hacks/'

def change_kb():
    '''This Fuction search the keyboard layout and toggle bettewn english a spanish'''
    os.system(f'setxkbmap -query > {path}la_temp.txt')

    with open(f'{path}la_temp.txt', 'r') as f:
        for line in f:
            layout_info.append(line)

    layout = layout_info[2]
    layout = layout[-3:-1]
    print(layout)
    if layout == 'us':
        os.system('setxkbmap -layout es')
        os.system('setxkbmap -query')
    elif layout == 'es':
        os.system('setxkbmap -layout us')
        os.system('setxkbmap -query')
    os.system(f'rm {path}la_temp.txt')

change_kb()
