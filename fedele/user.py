# import marshmallow as ma

# # Definiamo una classe Python che vogliamo serializzare e deserializzare
# class User:
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email

# # Definiamo uno schema Marshmallow per la classe User
# class UserSchema(ma.Schema):
#     class Meta:
#         # Campi che vogliamo serializzare/deserializzare
#         fields = ("username", "email")

# # Creiamo un'istanza User
# user = User(username="fedele", email="fedeleorlando056@gmail.com")

# # Creiamo uno schema Marshmallow per il nostro utente
# user_schema = UserSchema()

# # Serializziamo l'utente in JSON
# user_json = user_schema.dump(user)
# print(user_json)

# # Deserializziamo un JSON in un oggetto User
# data = {"username": "fedele", "email": "fedeleorlando056@gmail.com"}
# user_from_json = user_schema.load(data)
# print(user_from_json)






# import marshmallow as ma
# from pymongo import MongoClient
# # Definiamo una classe Python che vogliamo serializzare e deserializzare
# class User:
#     def __init__(self, username, email, age):
#         self.username = username
#         self.email = email
#         self.age = age

# # Definiamo uno schema Marshmallow per la classe User
# class UserSchema(ma.Schema):
#     class Meta:
#         # Campi che vogliamo serializzare/deserializzare
#         fields = ("username", "email", "age")

# # Creiamo un'istanza User con dati personalizzati
# username_input = input("Inserisci il nome utente: ")
# email_input = input("Inserisci l'indirizzo email: ")
# age_input = input("Inserisci l'età: ")
# user = User(username=username_input, email=email_input, age=age_input)

# # Creiamo uno schema Marshmallow per il nostro utente
# user_schema = UserSchema()

# # Serializziamo l'utente in JSON
# user_json = user_schema.dump(user)
# print(user_json)

# # Deserializziamo un JSON in un oggetto User
# data_input = {
#     "username": input("Inserisci il nome utente per la deserializzazione: "),
#     "email": input("Inserisci l'indirizzo email per la deserializzazione: "),
#     "age": input("Inserisci l'età per la deserializzazione: ")
# }
# user_from_json = user_schema.load(data_input)
# print(user_from_json)













import marshmallow as ma
from pymongo import MongoClient

# Definiamo una classe Python che vogliamo serializzare e deserializzare
class User:
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

# Definiamo uno schema Marshmallow per la classe User
class UserSchema(ma.Schema):
    class Meta:
        # Campi che vogliamo serializzare/deserializzare
        fields = ("username", "email", "age")

    # Funzione per la validazione dell'email
def valida_email(email):
    if "@gmail.com" not in email:
        raise ValueError("L'indirizzo email deve contenere il simbolo '@gmail.com'.")

    # Validazione personalizzata per l'età
    def validate_age(self, age):
        if age < 18:
            raise ma.ValidationError("L'età deve essere maggiore o uguale a 18 anni.")

# Chiedi all'utente di inserire l'indirizzo email con la validazione
while True:
    email_input = input("Inserisci l'indirizzo email: ")
    try:
        valida_email(email_input)
        break
    except ValueError as e:
        print(e)

# Continua con la creazione dell'oggetto User come prima
username_input = input("Inserisci il nome utente: ")
while True:
    try:
        age_input = int(input("Inserisci l'età: "))
        if age_input >= 18:
            break
        else:
            print("L'età deve essere maggiore o uguale a 18 anni.")
    except ValueError:
        print("Inserisci un valore numerico per l'età.")

user = User(username=username_input, email=email_input, age=age_input)

# Creiamo uno schema Marshmallow per il nostro utente
user_schema = UserSchema()

# Serializziamo l'utente in JSON
user_json = user_schema.dump(user)
print(user_json)

# Connessione a MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Modifica l'URL di connessione se necessario
db = client.user # Sostituisci "mydatabase" con il nome del tuo database

# Inseriamo l'oggetto deserializzato in MongoDB
users_collection = db.users
inserted_user = users_collection.insert_one(user_json)

print(f"Utente inserito con ID: {inserted_user.inserted_id}")