input_file = "Day2_input1.txt"
position = 0
depth = 0

with open(input_file, "r") as f:
    moves = [line for line in f]

for move in moves:
    pos,am = move.split(" ")
    match pos:
        case "forward":
            position += int(am)
        case "up":
            depth -= int(am)
        case "down":
            depth += int(am)
print(f"Depth = {depth}, Position = {position}")
print(f"Result: {depth * position}")
