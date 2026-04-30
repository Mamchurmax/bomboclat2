from app.repositories.category_repository import CategoryRepository


class CategoryService:
    def __init__(self):
        self.repository = CategoryRepository()

    def get_all_categories(self):
        return self.repository.get_all()

    def get_category_by_id(self, category_id):
        return self.repository.get_by_id(category_id)

    def create_category(self, data):
        return self.repository.create(data)

    def update_category(self, category_id, data):
        return self.repository.update(category_id, data)

    def delete_category(self, category_id):
        return self.repository.delete(category_id)
