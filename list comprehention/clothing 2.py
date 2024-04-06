print("\n+++Challenge for Python Masters")
print("List all label-codes except there is no X-size for females:")

colors = "B", "G", "W"
sizes = "S", "M", "L", "X"
sexes = "♂", "♀"

label_codes = [
    f"{sex}{size}{color}"
    for sex in sexes
    for size in sizes
    for color in colors
    if not (sex == "♀" and size == "X")]

print(f"{label_codes=}")
print(f"{len(label_codes)=}")
assert len(label_codes) == 21
