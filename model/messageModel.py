from .connection import connection

class messageModel():
    """Class to handle queries on the message table from the database
        Classe pour gérer les requêtes sur la table des messages à partir de la base de données"""

    def __init__(self):
        # Instanciate a connection with the database
        # Instancier une connexion avec la base de données
        self.db = connection()

    def get_messages(self):
        """Retrieve all message from the database as a list of dictionnaries
            Récupérer tous les messages de la base de données sous forme de liste de dictionnaires"""
        self.db.initialize_connection()
        self.db.cursor.execute("SELECT * FROM message")
        # Use fetchall to get a list
        # Utilisez fetchall pour obtenir une liste
        messages = self.db.cursor.fetchall()
        self.db.close_connection()
        return messages

    def add_message(self, author, content):
        """Save a message in the databas with author, content and date
            Enregistrer un message dans la base de données avec l'auteur, le contenu et la date"""
        self.db.initialize_connection()
        self.db.cursor.execute("INSERT INTO message (content, publishing_date, author) VALUES(%s, NOW(), %s)", (content, author))
        self.db.connection.commit()
        self.db.close_connection()


