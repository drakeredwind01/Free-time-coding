print( "\n+++Challenge for Python Masters" )
print( "List all label-codes except there is no X-size for females:" )

colors =  "B", "G", "W"
sizes = "S", "M", "L", "X"
sexes = "♂", "♀"

label_codes = []

for sex in sexes:
    for size in sizes:
        if sex == "♀" and size == "X":
            continue
        for color in colors:
            label_codes.append( sex+size+color )

print( f"{label_codes=}" )
print( f"{len( label_codes )=}" )
assert len( label_codes ) == 21