# from Models.APIRequest import APIRequest
from Models.Database import Database

def main():

    db = Database()
    # api = APIRequest(db)
    # api.data_loading()
    # api.data_recording()
    db.db_connexion()
    db.db_creation()

if __name__ == "__main__":
    main()