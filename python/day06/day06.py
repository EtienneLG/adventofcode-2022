datastream = open("day06.txt").read()

def find_marker(length):
    return next(x for x in range(len(datastream)-length) if len(set(datastream[x:x+length])) == length) + length

print(find_marker(4))
print(find_marker(14))