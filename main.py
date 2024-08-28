# --- Imports --- #

import math
from typing import Tuple


# --- Number Type --- #

type number = int | float


# --- Test --- #

def calcDistance(a: Tuple[number], b: Tuple[number]) -> float:
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
    
def lawOfCosines(d1: float, d2: float, d3: float):
    return math.degrees(math.acos((d1**2 + d2**2 - d3**2) / (2*d1*d2)))

def main():
    SCREEN_SIZE = (1280,720)

    A = (0,0)
    B = (640,360)
    C = (640,0)
    print(A,B,C)

    D1 = calcDistance(B,A) ##Should be hypotense
    D2  = calcDistance(C,B)
    D3  = calcDistance(A,C)
    print(D1,D2,D3)

    answer_degrees = lawOfCosines(D1,D2,D3)
    answer2_degrees = lawOfCosines(D1,D3,D2)

    answers_degrees = (answer_degrees,answer2_degrees,90)
    print(*answers_degrees)

    sum_of_angles = sum(answers_degrees)
    print(sum_of_angles == 180)
    

if __name__ == "__main__":
    main()
