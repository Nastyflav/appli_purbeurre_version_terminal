from Models.APIRequest import APIRequest
from Models.Database import Database

def main():

    api = APIRequest()
    db = Database(api)
    api.data_loading()
    db.database_connexion()
    db.data_recording(api)
    # print(api.products_list)
    # db.database_creation()

    # launch = LaunchApp()
    # launch.regular_start()

if __name__ == "__main__":
    main()