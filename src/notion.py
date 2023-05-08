import notion_client

from config import conf

def get_client():
    """Initialize the notion client.
    """
    client = notion_client.Client(auth=conf.token)
    return client

def insert_record(db:str, data):
    """Insert a record into the database.

    Args:
        db (str): The database id.
        data (dict): The data to be inserted.
    """
    conf.client.pages.create(**{
        "parent": {
            "database_id": db
        }, 
        "properties": data
    })
    print("Success!")