import requests


call = requests.get("https://restcountries.com/v3.1/all?fields=name,borders,languages,continents,population").json()

# 1: Poišči državo z največ sosedi (borders)
# Namig: Nekatere države so otoki in nimajo ključa "borders"!
print(call[0])

max_b=0
max_bord_country= ""
for c in call:
    bord=len(c.get("borders",[]))
    name=c["name"]["common"]
    if bord > max_b:
        max_b=bord
        max_bord_country=name

print(max_b,max_bord_country)

# 2: Poišči države kjer govorijo največ jezikov (languages)
# Namig: Nekatere države nimajo ključa "languages"
max_j=0
max_jezik_country= ""
for c in call:
    jezik=len(c.get("languages",[]))
    name=c["name"]["common"]
    if jezik > max_j:
        max_j=jezik
        max_jezik_country=name

print(max_j,max_jezik_country)


# 3: Izračunaj povprečno število prebivalcev (population) po celinah (continents)
# Namig: Vedno preveri, če je population večji od 0



# 4: Poišči državo z največ časovnimi pasovi (timezones)
# Namig: Vsaka država ima vsaj en timezone

# 5: Izpiši vse države, ki imajo v imenu presledek
# Namig: Uporabi ["name"]["common"] za ime države

# 6: Izpiši število držav, ki imajo za uradni jezik angleščino

# 7: V katerem časovnem pasu (timezone) je največ držav?
# Namig: Ena država ima lahko več timezone-ov

# 8: Katera črka se največkrat pojavi kot prva črka v imenu države?
# Namig: Za ime uporabi ["name"]["common"].lower()

# 9: Katera država ima najdaljše ime?

# 10: Izračunaj še eno statistiko po želji.