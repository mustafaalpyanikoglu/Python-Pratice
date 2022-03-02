"""
Task
You have a non-empty set s, and you have to execute N commands given in N lines.
The commands will be pop, remove and discard.

Function Description
Complete the wrap function in the editor below.
wrap has the following parameters:
string string: a long string
int max_width: the width to wrap to

Input Format

The first line contains integer n, the number of elements in the set s.
The second line contains n space separated elements of set s. All of the elements are non-negative integers, less than or equal to 9.
The third line contains integer N, the number of commands.
The next N lines contains either pop, remove and/or discard commands followed by their associated value.

Constraints
0<n<20
0<N<20

Output Format
Print the sum of the elements of set s on a single line.

Sample Input 0
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5

Sample Output 0
4
"""
if __name__ == "__main__":
    n = int(input())
    s = set([int(s) for s in input().split()])
    N = int(input())
    for _ in range(N):
        name, *line = input().split()
        if(name == "discard"):
            s.discard(int(line[0]))
        elif name == "remove":
            s.remove(int(line[0]))
        elif name == "pop":
            s.pop()
    print(sum(s))
