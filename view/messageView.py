from model.messageModel import messageModel

class messageView():
    """Manage all the logic related to the message entity
    Allow to see messages and write a new one
        Gérer toute la logique liée à l'entité de message
     Autoriser à voir les messages et à en écrire un nouveau"""

    def __init__(self):
        pass

    def index(self):
        """Display all messages from the database
            Afficher tous les messages de la base de données"""
        model = messageModel()
        # get the messages from the model
        # récupère les messages du modèle
        messages = model.get_messages()
        print('Bonjour et bienvenue sur le forum, voici les derniers messages : ')
        if messages:
            for message in messages:
                print("\nmessage {} : {}".format(message['id'], message['content']))
                print("Posté par {} le {} à {}".format(
                message['author'],
                message['publishing_date'].strftime("%d/%m/%Y"),
                message['publishing_date'].strftime("%H:%M")
                ))
                print("\n------------------------------")
        else:
            print("Aucun message pour le moment")

    def new_message(self):
        """Display input for the user to write a message and store values in database"""
        author = input("Quel est votre nom : ")
        content = input("Votre message : ")
        model = messageModel()
        # add the message in database thanks to the model
        model.add_message(author, content)




