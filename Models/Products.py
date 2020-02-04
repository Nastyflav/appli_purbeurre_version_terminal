class Products:
    """Product class used by the 'Pur Beurre' application.
    Data come from Open Food Facts french database.
    """
    def __init__(self, id, name, description, category_id,
                 stores, nova_group, code, url):
        self.id = id
        self.name = name
        self.description = description
        self.category_id = category_id
        self.stores = stores
        self.nova_group = nova_group
        self.code = code
        self.url =url
