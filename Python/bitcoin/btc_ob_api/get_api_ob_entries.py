import sys

API_OB_FILE_NOT_FOUND    = 1
API_OB_TOKEN_NOT_IN_FILE = 'TOKEN NOT FOUND'

class getApiObEntries:
    def __init__(self):
        # The API requires to have api.ob file in home directory(assuming the repo was cloned to the home as well)
        self.file = '../../../api.ob'
        try:
            with open(self.file) as file:
                self.apiObEntries = file.readlines()
        except FileNotFoundError:
            print('Couldn\'t open api.ob file. Aborting...')
            sys.exit(API_OB_FILE_NOT_FOUND)
        
    def getEntry(self, token):
        token += ':='
        self.entry = ''
        
        for line in self.apiObEntries:
            if token in line:
                self.entry = line[len(token) : -1]
                break
        
        if self.entry == '':
            print('Could not retrieve token {} from the api.ob file. Handling in next steps...'.format(token[:-2]))
            return API_OB_TOKEN_NOT_IN_FILE
        
        return self.entry
