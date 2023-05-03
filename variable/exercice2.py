nom=input("entrez votre nom:")
postnom=input("entrez votre postnom: ")
age=int(input("entrez votre age: "))

if age < 10 :
    print(f"bonjour {nom} {postnom} tu as {age} ans tu es bebe")
elif age == 10 and age < 18:
    print(f"bonjour {nom} {postnom} tu as {age} ans tu es mineur")
elif age >= 18 and age < 50:
    print(f"bonjour {nom} {postnom} tu as {age} ans tu es majeur")
elif age >= 50 and age <= 100:
    print(f"bonjour {nom} {postnom} tu as {age} ans tu es vieux")
else:
    print(f"bonjour {nom} {postnom} tu as {age} ans tu es inconnu")

