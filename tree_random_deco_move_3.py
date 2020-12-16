# I did it!!!!!!!!!!!!!!!!!!!!!!!

from colorama import init
init()
from colorama import Fore, Back, Style
import numpy as np
import math
import os
import threading
import time


deco = np.array(['●', 'o', 'x', 'X', '+', '◆'])
colors = [91, 93, 94, 95, 96, 97] #bright red, bright yellow, bright blue, bright magenta, bright cyan, bright white

def make_tree(width, height):
    ret = []
    center = math.floor(width/2)

    for y in range(0, height):
        col = []

        for x in range(0, width):
            if y < height*(4/5): # 트리 윗부분
                temp = y/height*center
                if(x>=(center-temp) and x<=(center+temp)): # 대충 가운데로 모이게
                    normal = x%(y%(height/5)+2)
                    dec = math.floor(np.random.rand() * len(deco)) # 데코레이션 idx 임의 선택
                    color = math.floor(np.random.rand() * len(colors)) # 컬러 인덱스 임의 선택

                    if y==0: # 트리 꼭대기
                        col.append("\x1b[93m★\x1b[0m") # 노랑색 별

                    elif normal==0:
                        col.append("\x1b[" + str(colors[color]) + "m" + str(deco[dec]) + "\x1b[0m")
                    
                    else:
                        col.append("\x1b[92m*\x1b[0m") # 초록색 나뭇잎
                else:
                    col.append(" ") # 트리 범위에 해당하지 않는 구간
            
            else: # 트리 기둥
                if(x >= center-center/10 and x<=center+center/10): # 범위를 트리보다 좁게
                    col.append("\x1b[42m+\x1b[49m") #Background color : Green, 모양 +, reset
                else:
                    col.append(" ") # 기둥 범위에 해당하지 않는 구간
        
        ret.append("".join(col))
    ret.append(" "*8 + "\x1b[101mMerry Christmas\x1b[0m")
    
    return "\n".join(ret)


Stopped = False
def multi_threading(func, sec):
    while not Stopped:
        func()
        time.sleep(sec)
    print('Done!')

def print_tree():
    #os.system('clear') #linux
    os.system('cls') #window
    tree = make_tree(30,30)
    print(tree)


if __name__ == "__main__":
    #print_tree(make_tree(30,30))
    t = threading.Thread(target=multi_threading, args=(print_tree, 0.5))
    t.start()

    

    