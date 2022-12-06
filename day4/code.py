################################################################################
#                                  Load data                                   #
################################################################################

toy_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
toy_input = toy_input.split("\n")

with open("input", "r") as f:
    in_data = f.read()
in_data = in_data.split("\n")[:-1]

# data = toy_input
data = in_data

################################################################################
#                              Massage input data                              #
################################################################################

pairs = list()
for row in data:
    row = row.split(",")
    row = [(int(x.split("-")[0]), int(x.split("-")[1])) for x in row]
    pairs.append(row)

################################################################################
#                                    Part 1                                    #
################################################################################

checks = list()
for pair in pairs:
    p1 = pair[0]
    p2 = pair[1]
    checks.append(
        (p1[0] <= p2[0] and p1[1] >= p2[1])
        or (p1[0] >= p2[0] and p1[1] <= p2[1])
    )
# print(f"{checks=}")
print(f"{sum(checks)=}")

################################################################################
#                                    Part 2                                    #
################################################################################

test_against = [False, False, True, True, True, True]

checks = list()
for pair in pairs:
    p1 = pair[0]
    p2 = pair[1]
    # print(
    #     p1,
    #     p2,
    #     p1[1] >= p2[0],
    #     p1[0] <= p2[1],
    #     (p1[1] >= p2[0] or p1[0] <= p2[1])
    # )
    # checks.append(p1[1] >= p2[0])
    checks.append(p1[1] >= p2[0] and p1[0] <= p2[1])

# print(f"{checks=}")
if data == toy_input:
    assert checks == test_against
print(f"{sum(checks)=}")
