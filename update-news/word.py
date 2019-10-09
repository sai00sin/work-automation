import docx
import os

class Word():
    '''
    def __init__(self):
        print('init')
    '''

    def get_file_dates(self):
        dates = []        
        for file in os.listdir():
            base, ext = os.path.splitext(file)
            if ext == '.docx':                
                dates.append(base[:8])
        return dates

    def load_file(self, file):
        doc = docx.Document(file)





