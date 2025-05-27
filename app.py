signs_conversions = {
    "ari": "Aries",
    "tau": "Taurus",
    "gem": "Gemini",
    "can": "Cancer",
    "leo": "Leo",
    "vir": "Virgo",
    "lib": "Libra",
    "sco": "Scorpio",
    "sag": "Sagittarius",
    "cap": "Capricorn",
    "aqu": "Aquarius",
    "pis": "Pisces"
}

print(signs_conversions)
print(signs_conversions["can"])
print(signs_conversions.get("vir"))
print(signs_conversions.get("mano", "super sign"))