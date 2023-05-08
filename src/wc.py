import requests

from config import conf
import notion

def google_trans(src_lang:str, to_lang:str, text:str):
    base_url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl={}&tl={}&dt=t&q={}'
    url = base_url.format(src_lang, to_lang, text)
    resp = requests.get(url)
    res = resp.json()[0][0][0]
    return res

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