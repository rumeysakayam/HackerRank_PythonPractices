# Task: Print Function 
# HackerRank link: https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true


if __name__ == '__main__':
    n = int(input())
    num = 1
    myStr = ""
    while num <= n:
        x = num
        myStr = myStr + str(x)
        num = num + 1
    print(myStr)
