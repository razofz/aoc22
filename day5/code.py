import re

# in_data = "toy_input"
in_data = "input"

with open(in_data, "r") as f:
    in_data = [x[:-1] for x in f.readlines()]

data = in_data
# data = in_data.split("\n")


def prepare_data(data):
    """Split input data into stacks and instructions.

    :in_data: TODO
    :returns: stacks, instructions, moves, froms, tos

    """
    toy = False
    if data == "toy_input":
        toy = True
    split_index = data.index("")

    stack = data[:split_index]
    stack.reverse()
    stack = stack[1:]
    instructions = data[split_index+1:]

    moves = [re.search(r"move \d+", x).group() for x in instructions]
    froms = [re.search(r"from \d+", x).group() for x in instructions]
    tos = [re.search(r"to \d+", x).group() for x in instructions]
    moves = [int(re.search(r"\d+", x).group()) for x in moves]
    froms = [int(re.search(r"\d+", x).group()) for x in froms]
    tos = [int(re.search(r"\d+", x).group()) for x in tos]
    assert min(moves) == min(froms) == min(tos) == 1
    tos = [x - 1 for x in tos]
    froms = [x - 1 for x in froms]

    if toy:
        assert moves == [1, 3, 2, 1]
        assert froms == [2, 1, 2, 1]
        assert tos == [1, 3, 1, 2]

    stacks = [[x[i:i+1] for x in stack] for i in range(1, len(stack[0]), 4)]
    stacks = [[y for y in x if y not in ("", " ")] for x in stacks]
    return stacks, instructions, moves, froms, tos


################################################################################
#                                    Part 1                                    #
################################################################################

stacks, instructions, moves, froms, tos = prepare_data(in_data)
# print(stacks)

for i in range(len(moves)):
    # print(moves[i], froms[i], tos[i])
    for j in range(moves[i]):
        stacks[tos[i]].append(stacks[froms[i]].pop())

# print(stacks)

if in_data == "toy_input":
    assert stacks == [["C"], ["M"], ["P", "D", "N", "Z"]]

print("part 1: ", "".join([x[-1] for x in stacks]))

################################################################################
#                                    Part 2                                    #
################################################################################

stacks, instructions, moves, froms, tos = prepare_data(in_data)
# print(stacks)

for i in range(len(moves)):
    # print(moves[i], froms[i], tos[i])
    length = len(stacks[froms[i]])
    container = []
    if length > 0 and not length < moves[i]:
        for j in range(moves[i]):
            container.append(stacks[froms[i]].pop())
    container.reverse()
    stacks[tos[i]] = stacks[tos[i]] + container
    # print(stacks)

# print(stacks)
result = "".join([x[-1] for x in stacks])
print("part 2: ", result)
if in_data == "toy_input":
    assert result == "MCD"
