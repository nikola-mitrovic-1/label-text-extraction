# Educational exercise: extracts age ranges from sample label sentences.
# Fictional/sample text only. Not for clinical use.
import re
redovi = ["Children 6 to 12 years: 250 mg every 6 hours.",
          "Adults and children over 12 years: 500 mg.",
          "Not recommended for children under 6 years.",
          "Not for children aged 6 months.",
          "Children from 2 to 5 years: 125 mg."] 

def izvuci_uzrast(red):
    raspon = re.findall(r"(\d+) to (\d+)", red)
    jedan = re.findall(r"(\d+) years", red)
    meseci = re.findall(r"(\d+) months", red)
    
    if raspon:
        return "od " + raspon[0][0] + " do " + raspon[0][1] + " godina"
    elif "over" in red and jedan:
        return "preko: " + jedan[0] + " godina"
    elif meseci:
        return "uzrast: " + meseci[0] + " meseci"
    elif "under" in red and jedan:
        return "ispod: " + jedan [0] + " godina"
    elif jedan:
        return "uzrast: " + jedan[0] + " godina"
    else:
        return "nema uzrasta"

for red in redovi:
    print(red, "->", izvuci_uzrast(red))
