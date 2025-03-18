import pandas as pd

class TeenageMental:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()
        self.process_data()
    
    def load_data(self):
        col_name = ["스트레스","스트레스_남학생","스트레스_여학생","우울감_경험률","우울_남학생","우울_여학생","자살_생각률","자살_남학생","자살_여학생"]
        return pd.read_excel(self.file_path, header=1, usecols="B:J", names=col_name)
    
    def process_data(self):
        self.data.loc[1] = 100.0 - self.data.loc[0]
        self.data["응답"] = ["그렇다", "아니다"]
        self.data = self.data.set_index("응답")
    
if __name__ == "__main__":
    tm = TeenageMental("data/teenage_mental.xlsx")
    print(tm.data)