from pywallet.infrastructure.database.models import ModelBase
from pywallet.infrastructure.database.connections import engine

ModelBase.metadata.create_all(engine)