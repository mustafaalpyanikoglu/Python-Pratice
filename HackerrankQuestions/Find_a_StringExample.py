"""
Task
In this challenge, the user enters a string and a substring. 
You have to print the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left.

Input Format
The first line of input contains the original string. The next line contains the substring.

Constraints
1<=len(string)<=200
Each character in the string is an ascii character.

Output Format
Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input 0
ABCDCDC
CDC

Sample Output 0
2
"""


def count_substring(string, sub_string):
    l = len(sub_string)
    count = 0
    for i in range(len(string)-len(sub_string)+1):
        if(string[i:i+len(sub_string)] == sub_string):
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
