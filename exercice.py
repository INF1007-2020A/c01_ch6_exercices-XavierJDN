#!/usr/bin/env python
# -*- coding: utf-8 -*-

""""
def order(values: list = None) -> bool:
    if len(values) == 10:
        return True, values == sorted(values)
        # TODO: Demander les valeurs ici
    values.append(input("Entre une valeur"))
    return False


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: Demander les mots ici
        words = [input(f"Quelles est ton {n} mot ") for n in range(0, 2)]

    for i in range(0, len(words)):
        if words[1][i] != words[2][len(words) - i]:
            return False
        else:
            return True


def contains_doubles(items: list) -> bool:
    my_set = set(items)
    return (my_set) == len(items)


def best_grades(student_grades: dict) -> str:
    sum_grades = 0
    for grades in student_grades:
        for grade in grades:
            sum_grades += grade
    average = sum_grades / len(grades)
    student_grades[grades] = average

    if student_grades["BOB"] > student_grades["Alice"]:
        return "BOB"
    else:
        return "Alice"

    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne


def histogram(sentence: str) -> tuple:
    # TODO: Créer l'histogramme a l'aide d'un dictionnaire
    letter_dict = {}
    list_letter = []
    for all_letter in sentence:
        nb_letter = 0
        for letter in sentence:
            if all_letter == letter:
                nb_letter += 1
        if nb_letter >= 5:
            letter_dict[letter] = nb_letter

    for letter, nb_letter in letter_dict.items():
        list_letter.append((letter, nb_letter))
    for index, letter in enumerate(list_letter):
        if letter[index][1] < letter[index + 1][1]:
            temp = letter[index][1]
            letter[index][1] = letter[index + 1][1]
            letter[index + 1][1] = temp

    #       Afficher l'histogramme et les lettres les plus fréquentes
    #       Retourner l'histogramme et le tableau de lettres

    return letter_dict, list_letter
"""

def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingrédients et enregsitrer dans une structure de données
    recette_dict = {}
    finish_recette = False
    while not finish_recette:
        list_ingredient = []
        finish_ingredient = False
        nom_recette = input("Quelle est la recette: ")
        print("Quelle sont les ingredient de ta recette: ")

        while not finish_ingredient:
            list_ingredient.append(input("Quelle est votre ingredient "))
            finish_temp = input("As-tu finit ta recette(y/n) ")
            if finish_temp == "y":
                finish_ingredient = True

        finish_tempb = input("As-tu finit de lister toute tes recette(y/n) ")

        if finish_tempb == "y":
            finish_recette = True
        recette_dict[nom_recette] = list_ingredient

    return recette_dict


def print_recipe(ingredients: dict) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    no_problem = True
    nom_recette = input("Quelle recette cherche-tu ")
    answer = ingredients.get(nom_recette)
    while answer is None:
        nom_recette = input("Peux-tu me donner une autre recette ")
        answer = ingredients.get(nom_recette)
    return answer
def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    while False:
        order()
        pass
    print(f"On vérifie les anagrammes...")
    #anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    #print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    #name, result = best_grades(grades)
    #print(f"{name} a la meilleure moyenne: {result}")

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print(print_recipe(recipes))


if __name__ == '__main__':
    main()
