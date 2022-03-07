"""
Task
You are given a string S and width w.
Your task is to wrap the string into a paragraph of width w.

Function Description
Complete the wrap function in the editor below.
wrap has the following parameters:
string string: a long string
int max_width: the width to wrap to

Returns
string: a single string with newline characters ('\n') where the breaks should be

Input Format
The first line contains a string, string.
The second line contains the width, max_width.

Constraints
0<len(string)<1000
0<max_width<len(string)

Sample Input 0
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output 0
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
"""
import textwrap
import math


def wrap(string, max_width):
    i = 0
    j = max_width
    myList = []
    if((len(string) > 0 and len(string) < 1000) and (max_width > 0 and max_width < len(string))):
        sayac = math.ceil(len(string)/max_width)
        while(i < len(string)):
            myList.append(string[i:j])
            i += max_width
            j += max_width
        for k in myList:
            print(k)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
