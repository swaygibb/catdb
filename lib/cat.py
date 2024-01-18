from lib.database import Database

class Cat:
    def get_cats(self):
        db = Database()

        with db.driver.session() as session:
            cats = session.read_transaction(self._get_cats)
            db.close()
            return cats

    def get_cat(self, cat_id):
        db = Database()

        with db.driver.session() as session:
            cat = session.read_transaction(self._get_single_cat, cat_id)
            db.close()
            return cat

    @staticmethod
    def _get_cats(tx):
        result = tx.run("MATCH (cat:Cat) RETURN ID(cat) AS id, cat.name AS name, cat.status AS status")
        return [{"id": record["id"], "name": record["name"], "status": record["status"]} for record in result]

    @staticmethod
    def _get_single_cat(tx, cat_id):
        result = tx.run("MATCH (cat:Cat) WHERE ID(cat) = $cat_id RETURN cat", cat_id=cat_id)
        return result.single()["cat"] if result else None