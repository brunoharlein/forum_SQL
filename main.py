import os

from view.messageView import messageView

# The action the user wants to do, by default nothing
# L'action que l'utilisateur veut faire, par défaut rien
action = ""

# ask the user for an action, if it is q leave the program
# demander à l'utilisateur une action, si c'est q quitter le programme
while action != "q":
    os.system('cls' if os.name == 'nt' else 'clear')
    # Some kind of routing system (check what routing means when programming !)
    # Une sorte de système de routage (vérifiez ce que signifie le routage lors de la programmation!)
    if action == "e":
        view = messageView()
        view.new_message()
    else:
        view = messageView()
        view.index()
    print("\nQue souhaitez-vous faire ?")
    print("(v : voir les messages, e : écrire un message, q : quitter)")
    action = input(": ")

# leave the program
# quitter le programme
exit()
