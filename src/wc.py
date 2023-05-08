import _thread

from config import conf
import notion

class WordCard:
    def __init__(self):
        self.word = ''
        self.definition = ''
        self.tags = ''
        self.date = ''
        pass
        
    def insert2db(self):
        # Lack documents. Check this issue to help understand: https://github.com/ramnes/notion-sdk-py/discussions/161
        prop = conf.wc['db_properties']
        data = {
            prop['word']: {
                'title': [{
                    'type': 'text',
                    'text': {
                        'content': self.word
                    }
                }]
            },
            prop['definition']: {
                'rich_text': [{
                    'type': 'text',
                    'text': {
                        'content': self.definition
                    }
                }]
            },
            prop['tags']: {
                'multi_select': [{
                    'name': self.tags
                }]
            },
            prop['date']: {
                'date': {
                    'start': self.date
                }
            }
        }
        
        notion.insert_record(conf.wc['db_id'], data)