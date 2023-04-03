import random


def random_choice():  # Renvoi un mot au hazard
    word_list = [
        "age",
        "aller",
        "ami",
        "amour",
        "animaux",
        "appareil",
        "apprendre",
        "arbre",
        "argent",
        "art",
        "attention",
        "avant",
        "avenir",
        "avis",
        "beau",
        "besoin",
        "bon",
        "bout",
        "bruit",
        "cadeau",
        "campagne",
        "caractere",
        "carte",
        "cause",
        "celebre",
        "changement",
        "chanson",
        "choix",
        "chute",
        "cigarette",
        "ciel",
        "cinema",
        "client",
        "cœur",
        "coin",
        "colere",
        "compte",
        "copain",
        "corps",
        "couleur",
        "coup",
        "courir",
        "creer",
        "crise",
        "danger",
        "decouvrir",
        "decision",
        "dehors",
        "depart",
        "developper",
        "difficile",
        "diriger",
        "discussion",
        "droit",
        "durer",
        "echec",
        "ecole",
        "ecrire",
        "effet",
        "enfance",
        "enfants",
        "environ",
        "esprit",
        "essayer",
        "etat",
        "etudiant",
        "excellent",
        "faire",
        "famille",
        "fête",
        "fois",
        "français",
        "froid",
        "garder",
        "genre",
        "gouvernement",
        "grand",
        "gratuit",
        "habitude",
        "heure",
        "histoire",
        "hiver",
        "homme",
        "idee",
        "image",
        "impossible",
        "interessant",
        "jardin",
        "jeu",
        "joie",
        "journee",
        "laisser",
        "leçon",
        "lire",
        "livre",
        "loin",
        "longtemps",
        "main",
        "malheureux",
        "manquer",
        "mari",
        "matin",
        "mauvais",
        "mieux",
        "monde",
        "mot",
        "musique",
        "nouveau",
        "nuit",
        "objectif",
        "oeil",
        "oiseau",
        "oncle",
        "oublier",
        "parler",
        "partir",
        "passe",
        "pays",
        "penser",
        "personne",
        "peur",
        "photo",
        "pied",
        "plan",
        "plupart",
        "pouvoir",
        "premier",
        "prix",
        "probleme",
        "professeur",
        "quitter",
        "rapport",
        "regarder",
        "rester",
        "salle",
        "sante",
        "savoir",
        "sentiment",
        "seul",
        "silence",
        "soir",
        "sortir",
        "souffrir",
        "souvenir",
        "temps",
        "travailler",
        "trouver",
        "type",
        "vacances",
        "vent",
        "verite",
        "ville",
        "vivre",
        "voiture",
        "voix",
    ]

    random_index = random.randint(0, len(word_list) - 1)
    random_word = word_list[random_index]
    return random_word


def ask_a_word():  # Demander un mot à l'utilisateur si le premier n'est pas valide : Renvoi le mot choisi
    print("Choisissez un mot valide.")
    return input()


def check_lenght(
    word, random_word
):  # Vérifier que la longueur du mot de l'user est égal à la longueur du mot à trouver
    return len(word) == len(random_word)  # Renvoi Bool


def check_word(
    word,
):  # Vérifier que le mot contient uniquement des lettres : Renvoie Bool
    verif = False
    for chr in word:
        if chr.isalpha():
            verif = True
            continue
        else:
            return False
    return True


def letter_in_word(
    letter, random_word
):  # Vérifie que la lettre est bien dans le mot a trouvé et renvoi un bool
    return letter in random_word


def letter_is_well_placed(
    letter, index_letter, random_word
):  # Vérifier si la lettre est bien placé ou mal placé Renvoi : Bool
    return index_letter == random_word.find(letter)


def Motus():
    random_word = random_choice()
    letters_in_word = 0
    letters_misplaced = 0
    user_word = ""
    index_user_word = -1
    for chance in range(len(random_word) + 5):
        print(f"La longueur du mot est de {len(random_word)}")
        letters_in_word = 0
        letters_misplaced = 0
        index_user_word = -1
        user_word = ask_a_word()
        print(random_word)
        while (
            check_lenght(user_word, random_word) != True
            or check_word(user_word) != True
        ):
            print("Mauvaise saisi !")
            user_word = ask_a_word()
        user_word = user_word.lower()
        for letter in user_word:
            index_user_word += 1
            if letter_in_word(letter, random_word):
                if letter_is_well_placed(letter, index_user_word, random_word):
                    letters_in_word += 1
                else:
                    letters_misplaced += 1
        if letters_in_word == len(random_word):
            return True
        print(
            f"Il y a {letters_in_word} lettres bien placé et {letters_misplaced} lettres mal placé."
        )
        print("--------------------------------------------")
    return False


if Motus():
    print("Bravo!!")
else:
    print("Perdu!!")
