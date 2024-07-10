# Task: Write A Function
# HackerRank link: https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true

def is_leap(year):
    leap = False
    
    if year % 4 == 0 and year % 25 != 0:
        leap = True
    elif year % 100 == 0 and year % 4 != 0:
        leap = False
    elif year % 400 == 0:
        leap = True
    
    return leap

year = int(input())
