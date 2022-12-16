MARKER_LENGTH = 4

# in_data = "toy_input"
in_data = "input"

with open(in_data, "r") as f:
    data = [x[:-1] for x in f.readlines()]
    if in_data != "toy_input":
        data = "".join(data)

# print(data)


def find_marker(buffer, marker_length=MARKER_LENGTH):
    for i in range(marker_length - 1, len(buffer)):
        potential_marker = set(buffer[i - marker_length : i])
        # print(foo)
        if len(potential_marker) == marker_length:
            return i


################################################################################
#                                    Part 1                                    #
################################################################################

if in_data == "toy_input":
    result = [find_marker(x) for x in data]
else:
    result = find_marker(data)

print(result)

if in_data == "toy_input":
    assert result == [7, 5, 6, 10, 11]

################################################################################
#                                    Part 2                                    #
################################################################################

if in_data == "toy_input":
    result = [find_marker(x, 14) for x in data]
else:
    result = find_marker(data, 14)

print(result)

if in_data == "toy_input":
    assert result == [19, 23, 23, 29, 26]
