import re
import sys

# Enter your code here. Read input from STDIN. Print output to STDOUT

def s_parse(p, t):
    t_no_parenth = t.replace('(', '').replace(')', '')
    
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', t_no_parenth).lower()


def c_parse(p, t):
    parts = t.split(' ')
    
    if p == 'C':
        result = ''.join(word.capitalize() for word in parts)
    else:
        result = parts[0] + ''.join(word.capitalize() for word in parts[1:])
    
    if p == 'M':
        result += '()'
    
    return result


if __name__ == '__main__':
    for line in sys.stdin:
        msg = line.strip().split(';')

        if msg[0] == 'S':
            text = s_parse(msg[1], msg[2])
        else:
            text = c_parse(msg[1], msg[2])
            
        print(text)
