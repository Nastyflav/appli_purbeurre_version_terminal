from Models.APIRequest import APIRequest
from Models.Database import Database

def main():

    db = Database()
    api = APIRequest(db)
    # db.db_connexion()
    # db.insert()
    api.data_loading()
    # print(api.products_list)
    api.data_recording()
    # db.db_creation()

if __name__ == "__main__":
    main()