import os
import random

walkp_path = '/home/dracul/Images/Walkpapers/'
nitro_path = '/home/dracul/.config/nitrogen/'

im_list = [i.name for i in os.scandir(walkp_path)]

def run():


    screen1 = random.choice(im_list)
    screen2 = random.choice(im_list)
    back_config = f'''
[xin_0]
file={walkp_path}{screen1}
mode=4
bgcolor=#000000
[xin_1]
file={walkp_path}{screen2}
mode=4
bgcolor=#000000
        '''
    os.system(f'echo "{back_config}" > {nitro_path}bg-saved.cfg')

if __name__ == "__main__":
    run()
