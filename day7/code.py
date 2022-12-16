in_data = "toy_input"
# in_data = "input"

with open(in_data, "r") as f:
    data = [x[:-1] for x in f.readlines()]

################################################################################
#               Gather commands and their outputs, for neatness                #
################################################################################

def extract_commands(data):
    commands = []
    i = 0
    while i < len(data):
        # print(i)
        # print(data[i])
        command = {"input": [], "output": []}
        # print(data[i])
        if data[i][0] == "$":
            command["input"] = data[i][2:]
            i += 1
            while i < len(data) and data[i][0] != "$":
                # print(data[i])
                command["output"].append(data[i])
                if i < len(data):
                    i += 1
            commands.append(command)
    return commands


commands = extract_commands(data)
[print(x) for x in commands]

################################################################################
#                            Interpret the commands                            #
################################################################################

cwd = "/"


def traverse(commands):
    ...


