import os

choice = os.environ.get('HBNB_TYPE_STORAGE')

print(choice)
if choice == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
