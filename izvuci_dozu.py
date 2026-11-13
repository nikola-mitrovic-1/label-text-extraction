import re
redovi = ["Take 500 mg every 6 hours.",
          "Maximum 4000 mg in 24 hours.",
          "Take one tablet."]

def izvuci_dozu(red):
    doza = re.findall(r"(\d+) mg", red)
    if doza:
        if "Maximum" in red:
            return "maksimalna dnevna doza " + doza[0] + " mg"
        else:
            return "doza: " + doza[0] + " mg"
    else:
        return "nema doze"

for red in redovi:
    print(red, "->", izvuci_dozu(red))
