program = open("day10.txt").read().split("\n")

def part_one():
    cycle = 0
    register = 1

    signal = 0

    for instruction in program:
        if instruction == "noop":
            cycle += 1
            if (cycle - 20) % 40 == 0:
                signal += (cycle) * register
        elif instruction.startswith("addx"):
            cycle += 2
            if (cycle - 20) % 40 == 0:
                signal += (cycle) * register
            if (cycle - 1 - 20) % 40 == 0:
                signal += (cycle - 1) * register
            register += int(instruction.split(" ")[1])
    print(signal)

def part_two():
    CRT = [[], [], [], [], [], []]
    position = 1
    cycle = 0

    for instruction in program:
        if instruction == "noop":
            if cycle % 40 in [position + i for i in range(-1, 2)]:
                CRT[cycle // 40].append("#")
            else:
                CRT[cycle // 40].append(" ")
            cycle += 1
        elif instruction.startswith("addx"):
            for step in range(2):
                if cycle % 40 in [position + i for i in range(-1, 2)]:
                    CRT[cycle // 40].append("#")
                else:
                    CRT[cycle // 40].append(" ")
                cycle += 1
            position += int(instruction.split(" ")[1])
    for row in CRT:
        print(*row)

part_one()
part_two()