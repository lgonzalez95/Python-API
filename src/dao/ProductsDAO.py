from src.utilities.DBUtility import DBUtility


class ProductsDAO:
    def __init__(self):
        self.db_helper = DBUtility()

    def get_all_products(self):
        sql = "SELECT * FROM test_api_db.product;"
        return self.db_helper.execute_select(sql)
