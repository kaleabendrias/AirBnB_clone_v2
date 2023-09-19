import os

storageType = os.environ.get('HBNB_TYPE_STORAGE')

if storageType == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
