from Models.APIRequest import APIRequest


def main():

    api = APIRequest()
    api.data_loading()
    print(api.products_list)

if __name__ == "__main__":
    main()