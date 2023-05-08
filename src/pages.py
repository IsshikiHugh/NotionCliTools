from PyInquirer import prompt, Separator
from pprint import pprint
from config import conf
from datetime import date

from wc import WordCard
import notion

def welcome_page():
    # Check if the config file is valid.
    if not conf.has_data:
        print('Configuration file is not loaded!')
        exit(-1)
        
    questions = [
        {
            'type': 'expand',
            'name': 'welcome',
            'message': 'What do you want to do?',
            'default': 'i',
            'choices': [
                {
                    'key': 'i',
                    'name': 'Insert a new word.',
                    'value': 'insert'
                },
                {
                    'key': 'q',
                    'name': 'Quit the application.',
                    'value': 'quit'
                }
            ]
        }
    ]
    answer = prompt(questions)['welcome']
    return answer

def wc_insert_page():
    # Check if the config file is valid.
    if not conf.has_data:
        print('Configuration file is not loaded!')
        exit(-1)
        
    # The word card object 
    wc = WordCard()
    
    questions = [
        {
            'type': 'input',
            'name': 'word',
            'message': 'Please input the word or phrase you want to insert!',
        },
    ]
    wc.word = prompt(questions)['word']
    
    questions = [
        {
            'type': 'editor',
            'name': 'definition',
            'message': 'Please give the definition of the word or phrase!',
            'default': '\n\n Definition of ' + wc.word + '.\n',
            'eargs': {
                'editor':'vim',
                'ext':'.cache'
            },
        },
        {
            'type': 'rawlist',
            'name': 'tags',
            'message': 'Please chose the tag of the word',
            'choices': conf.wc['tags-mem'],
        },
    ]
    answers = prompt(questions)
    wc.definition = answers['definition']
    wc.tags = answers['tags']
    wc.date = date.today().strftime("%Y-%m-%d")
    wc.insert2db()