import pandas as pd

OUTCOMES = {
    "win": 6,
    "draw": 3,
    "loss": 0,
}
HAND_POINTS = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}
CODES = {
    "A": "rock",
    "X": "rock",
    "Y": "paper",
    "B": "paper",
    "Z": "scissors",
    "C": "scissors",
}

# in_file = "toy_input"
in_file = "input"

df = pd.read_csv(in_file, header=None, names=["them_code", "me_code"], sep=" ")
df["outcome"] = "loss"

# df.loc[
#     df.two.map(CODES).map(HAND_POINTS) > df.one.map(CODES).map(HAND_POINTS), "outcome"
# ] = "win"
# df.loc[
#     df.two.map(CODES).map(HAND_POINTS) == df.one.map(CODES).map(HAND_POINTS), "outcome"
# ] = "draw"

df["them"] = df.them_code.map(CODES)
df["me"] = df.me_code.map(CODES)

df.loc[df.them == df.me, "outcome"] = "draw"
df.loc[(df.me == "rock") & (df.them == "scissors"), "outcome"] = "win"
df.loc[(df.me == "scissors") & (df.them == "paper"), "outcome"] = "win"
df.loc[(df.me == "paper") & (df.them == "rock"), "outcome"] = "win"

df["score"] = df.me.map(HAND_POINTS) + df.outcome.map(OUTCOMES)

print(df)
print(f"\n> Total sum is {df.score.sum()}")

################################################################################
#                                    Part 2                                    #
################################################################################

CODES_THEM = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
}
CODES_ME = {
    "X": "loss",
    "Y": "draw",
    "Z": "win",
}
WIN_CONDITIONS = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock",
}
LOSS_CONDITIONS = {v: k for k, v in WIN_CONDITIONS.items()}

df["me_part2"] = df.me_code.map(CODES_ME)

df["me_hand_part2"] = "wat"

df.loc[(df.me_part2 == "win"), "me_hand_part2"] = df.loc[
    (df.me_part2 == "win")
].them.map(WIN_CONDITIONS)
df.loc[(df.me_part2 == "loss"), "me_hand_part2"] = df.loc[
    (df.me_part2 == "loss")
].them.map(LOSS_CONDITIONS)
df.loc[(df.me_part2 == "draw"), "me_hand_part2"] = df.loc[(df.me_part2 == "draw")].them

df["score_part2"] = df.me_hand_part2.map(HAND_POINTS) + df.me_part2.map(OUTCOMES)

print(df)
print(f"\n> Total sum is {df.score_part2.sum()}")
