import yaml
import os

import notion

def get_db_id_from_link(link:str):
    """Abstract the database id from the link.

    Args:
        link (str): Copy from notion database, check the link below for details.
        
        https://developers.notion.com/docs/working-with-databases @ "Where can I find my database's ID?"

    Returns:
        str: The database id.
    """
    return (link.split('/')[-1]).split('?')[0]




class Config:
    """Parse the config files and organize the data.
    """
    def __init__(self):
        self.has_data = False
        pass
    
    def parse(self, file_path:str = 'config.yaml'):
        """Parse the config file.

        Args:
            file_path (str): The path of the config file. Defaults to 'config.yaml'.
        """
        self.has_data = True
        with open(file_path, 'r', encoding="utf-8") as file:
            config = yaml.load(file, Loader=yaml.FullLoader)

            # Store the original data.
            self.path = file_path
            self.meta = config
            
            # Notion things.
            self.token = config['notion-token']
            self.client = notion.get_client()
            
            # Word cards app.
            conf_wc = config['word-cards']
            self.wc = {
                'db_id': get_db_id_from_link(conf_wc['db']['link']),
                'db_properties': {
                    'word': conf_wc['db']['properties']['word'],
                    'definition': conf_wc['db']['properties']['definition'],
                    'tags': conf_wc['db']['properties']['tags'],
                    'date': conf_wc['db']['properties']['date'],
                },
                'tags-mem': conf_wc['tags-mem'],
            }
    def update_config(self):
        with open(self.path, 'w', encoding="utf-8") as file:
            # Update word cards tags.
            self.meta['word-cards']['tags-mem'] = self.wc['tags-mem']
            yaml.dump(self.meta, file, allow_unicode=True)
conf = Config()