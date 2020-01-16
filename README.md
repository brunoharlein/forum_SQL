Un forum
Dans cet exercice, vous réaliserez une application simulant le fonctionnement d’un forum. Votre application sera développée en orienté objet. L’application présentera les fonctionnalités suivantes :
- Quand l’utilisateur lance l’application, la page d’accueil lui affiche l’ensemble des messages contenus dans la base de données
- Un message est présenté avec le nom de celui qui l’a écrit, la date de publication, l’heure de publication et son id
- L’utilisateur peut choisir entre voir les messages (action par défaut), écrire un message ou quitter l’application
- Quand l’utilisateur écrit un message, on lui demande successivement le pseudo qu’il souhaite utiliser et le message qu’il souhaite poster
Bien entendu pour stocker les messages écrits par les utilisateurs et pouvoir les retrouver par la suite, vous allez les sauvegarder dans une base de données PostgreSQL.
Cette base de données ne contiendra qu’une seule table : message, dont voici la structure.
id(integer, clé primaire)
content(text, non nul) publishing_date(timestampz, non nul) author(varchar maximum 50 caractères, non nul)
Pour vous aider, voici l’ordre des étapes que vous pouvez suivre. Ce n’est pas la seule manière de faire mais cela peut vous aider si vous êtes perdu :
- Créer la table message via la ligne de commande en veillant à respecter la structure demandée
- Tenter de se connecter à la BDD grâce à la librairie Psycopg2, vérifier que la connexion peut s’établir avant de passer à la suite en exécutant le script
- Écrire dans un fichier main.py un code capable de récupérer l’action utilisateur et d’effectuer une action spécifique selon la commande rentrée
- Créer un fichier de vues contenant deux méthodes, une pour l’affichage des messages et une pour l’écriture d’un message. Pour l’instant, ces commandes ne font rien de particulier si ce n’est un print d’un message de test
- Vérifiez que lorsque l’utilisateur demande à voir les message ou à écrire un message ce soit la bonne méthode de la vue qui est appelée dans le fichier main.py
- Créer un fichier de modèle contenant deux méthodes, une pour récupérer tous les messages en base de données et une pour enregistrer un message en base de données. Attention cette méthode attend au moins deux arguments, le nom de l’auteur et le contenu de son message
- Appeler chaque méthode du modèle dans la méthode correspondante de la vue et vérifier son fonctionnement
- Mettre en forme l’affichage des messages
- Mettre en forme les inputs pour récupérer les informations nécessaires à la rédaction d’un nouveau message