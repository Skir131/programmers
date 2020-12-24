def solution(s, n):
    answer = ''
    for c in s:
        if c == " ":
            answer += c
        # if c is lowercase
        elif ord(c) >= ord('a'):
            # if asciicode of c + n > asciicode of 'z'
            if ord(c) + n > ord('z'):
                answer +=  chr(ord('a') + (ord(c) + n - ord('z')) -1)
            else:
                answer += chr(ord(c) + n)
        # if c is uppercase
        else:
            # if asciicode of c + n > asciicode of 'Z'
            if ord(c) + n > ord('Z'):
                answer += chr(ord('A') + (ord(c) + n - ord('Z')) -1)
            else:
                answer += chr(ord(c) + n)
    return answer