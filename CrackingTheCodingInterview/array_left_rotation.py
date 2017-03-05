_, rotations = map(int, input().split(' '))
array = list(map(int, input().split(' ')))

def rotate(array, shift):
    return (array[(i + shift) % len(array)] for i in range(len(array)))

print(*rotate(array, rotations), sep=' ')