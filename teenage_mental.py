import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rc("font", family="NanumGothic")

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

class TeenageMentalVisualizer:
    def __init__(self, data):
        self.data = data
        self.stress()
        self.depression()
        self.suicide()
    
    def plot_pie_chart(self, column, ax, title):
        self.data[column].plot.pie(explode=[0,0.02], ax=ax, autopct="%1.1f%%", textprops={"fontsize": 16, 'fontweight': 'bold'})
        ax.set_title(title, fontsize=20, fontweight='bold')
        ax.set_ylabel("")
    
    def stress(self):
        fig, ax = plt.subplots(1, 3, figsize=(16, 8))
        self.plot_pie_chart("스트레스", ax[0], "스트레스를 받은 적이 있다")
        self.plot_pie_chart("스트레스_남학생", ax[1], "스트레스를 받은 적이 있는 남학생")
        self.plot_pie_chart("스트레스_여학생", ax[2], "스트레스를 받은 적이 있는 여학생")
        plt.savefig("images/stress.png")
    
    def depression(self):
        fig, ax = plt.subplots(1, 3, figsize=(16, 8))
        self.plot_pie_chart("우울감_경험률", ax[0], "우울감을 경험한 적이 있다")
        self.plot_pie_chart("우울_남학생", ax[1], "우울감을 경험한 적이 있는 남학생")
        self.plot_pie_chart("우울_여학생", ax[2], "우울감을 경험한 적이 있는 여학생")
        plt.savefig("images/depression.png")
    
    def suicide(self):
        fig, ax = plt.subplots(1, 3, figsize=(16,8))
        self.plot_pie_chart("자살_생각률", ax[0], "자살을 생각한 적이 있다")
        self.plot_pie_chart("자살_남학생", ax[1], "자살을 생각한 적이 있는 남학생")
        self.plot_pie_chart("자살_여학생", ax[2], "자살을 생각한 적이 있는 여학생")
        plt.savefig("images/suicide.png")
    
if __name__ == "__main__":
    tm = TeenageMental("data/teenage_mental.xlsx")
    data = tm.data
    tmv = TeenageMentalVisualizer(data)
   