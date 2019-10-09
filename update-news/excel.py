import openpyxl
import pprint

class Excel():
    '''
    def __init__(self):
        print('init')
    '''

    def load_file(self, file):
        wb = openpyxl.load_workbook(file)
        return wb

    def load_sheet(self, file, sn):
        wb = self.load_file(file)
        sheet = wb[sn]
        print(sheet)

        '''
        ws = wb['2018年1月〜']
        print(ws)
        '''
