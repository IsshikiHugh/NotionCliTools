from PyInquirer import prompt, Separator
from pprint import pprint

import notion
import pages
from config import conf


if __name__ == '__main__':
    # Parse config from config files.
    conf.parse('config.yaml')
    
    # Application starts here.
    while (True):
        next = pages.welcome_page()
        if next == 'quit':
            break
        elif next == 'insert':
            # Maybe another page to check if user want to continue.
            pages.wc_insert_page()
    conf.update()