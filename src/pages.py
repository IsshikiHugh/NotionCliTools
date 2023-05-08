from PyInquirer import prompt, Separator
from pprint import pprint
from config import conf
from datetime import date

from wc import WordCard, google_trans
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
    
    # Choose the translation mode.
    questions = [
        {
            'type': 'expand',
            'name': 'auto-translate',
            'message': 'Do you want to use auto translate or edit yourself?',
            'default': 'g',
            'choices': [
                {
                    'key': 'g',
                    'name': 'Use google translate.',
                    'value': 'google-translate'
                },
                {
                    'key': 'e',
                    'name': 'Edit yourself.',
                    'value': 'edit-yourself'
                }
            ]
        }
    ]
    
    trans_mode = prompt(questions)['auto-translate']
    if trans_mode == 'google-translate':
        questions = [
            {
                'type': 'list',
                'name': 'trans-lang',
                'message': 'Which is source language?',
                'default': 'English 👉 中文',
                'choices': [
                    {
                        'name': 'English 👉 中文',
                        'value': ['en', 'zh-CN'],
                    },
                    {
                        'name': '中文 👉 English',
                        'value': ['zh-CN', 'en'],
                    }
                ],
            }
        ]
        sl, tl = prompt(questions)['trans-lang']
        wc.definition = google_trans(sl, tl, wc.word)
        print('auto-translate result: ' + str(wc.definition))
    elif trans_mode == 'edit-yourself':
        questions = [
            {
                'type': 'editor',
                'name': 'definition',
                'message': 'Please give the definition of the word or phrase!',
                'default': '',
                'eargs': {
                    'editor':'vim',
                    'ext':'.cache'
                },
            },
        ]
        wc.definition = prompt(questions)['definition']

    # Choose the tag of the word.
    questions = [
        {
            'type': 'rawlist',
            'name': 'tags',
            'message': 'Please chose the tag of the word',
            'choices': conf.wc['tags-mem'],
        },
    ]
    
    wc.tags = prompt(questions)['tags']
    
    # Get the note data.
    wc.date = date.today().strftime("%Y-%m-%d")
    
    # Insert to database.
    wc.insert2db()