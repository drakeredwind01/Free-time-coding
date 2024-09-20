import keyboard  # Install with `pip install keyboard`
import random

# Define the Greek letter mappings
greek_mappings = {
    "A": ("Α", "α", "Alpha"),
    "B": ("Β", "β", "Beta"),
    "C": ("Γ", "γ", "Gamma"),
    "D": ("Δ", "δ", "Delta"),
    "E": ("Ε", "ε, η", "Epsilon, Eta"),
    "F": ("Γ", "γ", "Gamma"),
    "G": ("Γ", "γ", "Gamma"),
    "H": ("Η", "η", "Eta"),
    "I": ("Ι", "ι", "Iota"),
    "J": ("Ι", "ι", "Iota"),
    "K": ("Κ", "κ", "Kappa"),
    "L": ("Γ", "γ", "Gamma"),
    "M": ("Μ", "μ", "Mu"),
    "N": ("Ν", "ν", "Nu"),
    "O": ("Ο", "ο", "Omicron"),
    "P": ("Π", "π", "Pi"),
    "Q": ("Δ", "δ", "Delta"),
    "R": ("Ρ", "ρ", "Rho"),
    "S": ("Σ", "σ", "Sigma"),
    "T": ("Τ", "τ", "Tau"),
    "U": ("Υ", "υ", "Upsilon"),
    "V": ("Β", "β", "Beta"),
    "W": ("Ψ", "ψ", "Psi"),
    "X": ("Χ", "χ", "Chi"),
    "Y": ("Υ", "υ", "Upsilon"),
    "Z": ("Ζ", "ζ", "Zeta")
}

def on_key_press(event):
    key = event.name.upper()
    if key in greek_mappings:
        capital, lower, name = greek_mappings[key]
        print(f"{key}")
        print(f"    {capital}, {lower}, {name}")

print("Keylogger running... Press ESC to exit.")

# Register the key press events
keyboard.on_press(on_key_press)

# Wait for the user to press ESC to exit
keyboard.wait('esc')




'''
next challenge

please use this list to list all of the possible greek letters a letter could be using the list below.
code"
import keyboard  # Install with pip install keyboard
import random

# Define the Greek letter mappings
greek_mappings = {
    "A": ("Α", "α", "Alpha"),
    "B": ("Β", "β", "Beta"),
    "C": ("Γ", "γ", "Gamma"),
    "D": ("Δ", "δ", "Delta"),
    "E": ("Ε", "ε, η", "Epsilon, Eta"),
    "F": ("Γ", "γ", "Gamma"),
    "G": ("Γ", "γ", "Gamma"),
    "H": ("Η", "η", "Eta"),
    "I": ("Ι", "ι", "Iota"),
    "J": ("Ι", "ι", "Iota"),
    "K": ("Κ", "κ", "Kappa"),
    "L": ("Γ", "γ", "Gamma"),
    "M": ("Μ", "μ", "Mu"),
    "N": ("Ν", "ν", "Nu"),
    "O": ("Ο", "ο", "Omicron"),
    "P": ("Π", "π", "Pi"),
    "Q": ("Δ", "δ", "Delta"),
    "R": ("Ρ", "ρ", "Rho"),
    "S": ("Σ", "σ", "Sigma"),
    "T": ("Τ", "τ", "Tau"),
    "U": ("Υ", "υ", "Upsilon"),
    "V": ("Β", "β", "Beta"),
    "W": ("Ψ", "ψ", "Psi"),
    "X": ("Χ", "χ", "Chi"),
    "Y": ("Υ", "υ", "Upsilon"),
    "Z": ("Ζ", "ζ", "Zeta")
}

def on_key_press(event):
    key = event.name.upper()
    if key in greek_mappings:
        capital, lower, name = greek_mappings[key]
        print(f"{key}")
        print(f"    {capital}, {lower}, {name}")

print("Keylogger running... Press ESC to exit.")

# Register the key press events
keyboard.on_press(on_key_press)

# Wait for the user to press ESC to exit
keyboard.wait('esc')

"

list"
A       Α, α - Alpha
B       Β, β - Beta
T,F,L    Γ, γ - Gamma
D,O,Q,A,G,    Δ, δ - Delta
E       Ε, ε - Epsilon
Z       Ζ, ζ - Zeta
E       Η, η - Eta
O,D,G    Θ, θ - Theta
I       Ι, ι - Iota
K       Κ, κ - Kappa
A       Λ, λ - Lambda
M       Μ, μ - Mu
N       Ν, ν - Nu
E       Ξ, ξ - Xi
O       Ο, ο - Omicron
N,      Π, π - Pi
P       Ρ, ρ - Rho
E,S       Σ, σ, ς - Sigma
A       σ: Used in the middle of words
S,Q     ς: Used at the end of words
T       Τ, τ - Tau
Y       Υ, υ - Upsilon
O       Φ, φ - Phi
X,CH       Χ, χ - Chi
Y,W     Ψ, ψ - Psi
N       Ω, ω - Omega
"

'''
