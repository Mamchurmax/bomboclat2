from app.extensions import db
from app.models.category import Category


class CategoryRepository:
    def get_all(self):
        return Category.query.all()

    def get_by_id(self, category_id):
        return db.session.get(Category, category_id)

    def get_by_name(self, name):
        return Category.query.filter_by(name=name).first()

    def create(self, data):
        name = data.get('name') if isinstance(data, dict) else data
        category = Category(name=name)
        if isinstance(data, dict) and 'description' in data:
            category.description = data['description']
        db.session.add(category)
        db.session.commit()
        return category

    def update(self, category_id, data):
        category = self.get_by_id(category_id)
        if category:
            for key, value in data.items():
                setattr(category, key, value)
            db.session.commit()
        return category

    def delete(self, category_id):
        category = self.get_by_id(category_id)
        if category:
            db.session.delete(category)
            db.session.commit()
            return True
        return False
