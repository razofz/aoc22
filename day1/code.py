with open("input", "r") as f:
    s = f.read()

elves = dict()
i = 0
for cal in s.split("\n"):
    if not i in elves.keys():
        elves[i] = list()
    if cal != "":
        elves[i].append(int(cal))
    else:
        i += 1

sums = {k: sum(v) for k, v in elves.items()}

max_idx = max(sums, key=sums.get)
print(max_idx, sums[max_idx])

throwaway_sums = sums

tops = 0
for i in range(3):
    max_idx = max(throwaway_sums, key=throwaway_sums.get)
    print(max_idx, throwaway_sums[max_idx])
    tops += throwaway_sums[max_idx]
    del throwaway_sums[max_idx]

print(tops)
