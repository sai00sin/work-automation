import word
import excel

class Main():
    def __init__(self, word, excel):
        self.word = word.Word()
        self.excel = excel.Excel()

main = Main(word, excel)

main.excel.load_sheet('genkou.xlsx', '2018年1月〜')


file_dates = main.word.get_file_dates()
