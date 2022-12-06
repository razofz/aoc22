import string

COMPARTMENT_CUT = 0.5

letters = string.ascii_letters
PRIORITIES = {k: v for k, v in zip(letters, range(1, len(letters) + 1))}

toy_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
toy_input = toy_input.split("\n")

with open("input", "r") as f:
    in_data = f.read()
in_data = in_data.split("\n")[:-1]

data = in_data

foo = [(x[:int(len(x)/2)], x[int(len(x)/2):]) for x in data]
assert (len(foo[0][0]) + len(foo[0][1])) == len(data[0])

commons = [set(foo[i][0]).intersection(set(foo[i][1])) for i in range(len(foo))]
assert all([len(x) == 1 for x in commons])
commons = ["".join(x) for x in commons]

scores = [PRIORITIES[x] for x in commons]

# print(scores)
print(sum(scores))

################################################################################
#                                    Part 2                                    #
################################################################################

# data = toy_input
data = in_data
assert len(data) % 3 == 0

data = [data[i*3:i*3+3] for i in range(int(len(data) / 3))]
commons = [set(x[0]).intersection(set(x[1])).intersection(set(x[2])) for x in data]
assert all([len(x) == 1 for x in commons])
commons = ["".join(x) for x in commons]

scores = [PRIORITIES[x] for x in commons]

print(sum(scores))
