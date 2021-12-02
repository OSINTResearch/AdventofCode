increased = 0

with open("Day1_input1.txt", "r") as depth_file:
#    depths = depth_file.readlines()
    *depths, = map(int, depth_file.readlines())
    for i in range(3, len(depths)):
        if (depths[i - 3] + depths[i - 2] + depths[i - 1]) < (depths[i - 2] + depths[i - 1] + depths[i]):
            increased += 1
print(f"{increased}")
