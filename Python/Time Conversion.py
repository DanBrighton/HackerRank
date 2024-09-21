import os


def timeConversion(s):
    hour = int(s[:2])
    body = s[2:8]
    identity = s[8]
    
    if identity == 'P':
        t = str(hour % 12 + 12) + body
    else:
        t = f"{(hour % 12):02}" + body
    
    print(t)
    return t


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()