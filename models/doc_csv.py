# mongo-engine packages
from mongoengine import Document, StringField, FloatField

class Csv(Document):
    """
    Template for a monogengine csv document, which represents the given data.

    :param: date
    :param: location
    :param: iso_code


    :Example:

    >>> import mongoengine
    >>> from app import default_config

    >>> mongoengine.connect(**default_config['MONGODB_SETTINGS'])
    MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True, read_preference=Primary())

    >>> new_csv = Csv()
    >>> new_meal.save()
    <Csv: csv object>
    """

    date = StringField(required=True)
    location = StringField(required=True)
    iso_code = StringField(required=True)
