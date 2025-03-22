import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 한글 폰트 설정 (matplotlib 한글 깨짐 방지용)
matplotlib.rc("font", family="NanumGothic")

class TeenageMental: # 청소년 정신 건강 관련 데이터를 불러오고 전처리하는 클래스
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()     # 데이터 불러오기
        self.process_data()              # 데이터 전처리

    def load_data(self): # 엑셀 파일에서 필요한 열만 읽고, 컬럼명 지정하여 데이터프레임으로 반환
        col_name = [
            "스트레스", "스트레스_남학생", "스트레스_여학생",
            "우울감_경험률", "우울_남학생", "우울_여학생",
            "자살_생각률", "자살_남학생", "자살_여학생"
        ]
        return pd.read_excel(self.file_path, header=1, usecols="B:J", names=col_name)

    def process_data(self): # '그렇다', '아니다' 두 응답 비율로 구성된 pie chart용 데이터 생성
        self.data.loc[1] = 100.0 - self.data.loc[0]
        self.data["응답"] = ["그렇다", "아니다"]  # 응답 컬럼 추가
        self.data = self.data.set_index("응답")   # 응답을 인덱스로 설정

class TeenageMentalVisualizer: # 청소년 정신 건강 데이터를 시각화하는 클래스
    def __init__(self, data):
        self.data = data
        self.stress()
        self.depression()
        self.suicide()

    def plot_pie_chart(self, column, ax, title): # 개별 항목에 대해 pie chart를 그리고, 제목과 스타일을 설정합니다.
        self.data[column].plot.pie(
            explode=[0, 0.02],               # '아니다' 항목을 살짝 분리
            ax=ax,
            autopct="%1.1f%%",               # 퍼센트 표시
            textprops={"fontsize": 16, 'fontweight': 'bold'}
        )
        ax.set_title(title, fontsize=20, fontweight='bold')
        ax.set_ylabel("")                   # y축 라벨 제거

    def stress(self): # 스트레스 경험률 시각화: 전체, 남학생, 여학생
        fig, ax = plt.subplots(1, 3, figsize=(16, 8))
        self.plot_pie_chart("스트레스", ax[0], "스트레스를 받은 적이 있다")
        self.plot_pie_chart("스트레스_남학생", ax[1], "스트레스를 받은 적이 있는 남학생")
        self.plot_pie_chart("스트레스_여학생", ax[2], "스트레스를 받은 적이 있는 여학생")
        plt.savefig("images/stress.png")  # 결과 이미지 저장

    def depression(self):# 우울감 경험률 시각화: 전체, 남학생, 여학생
        fig, ax = plt.subplots(1, 3, figsize=(16, 8))
        self.plot_pie_chart("우울감_경험률", ax[0], "우울감을 경험한 적이 있다")
        self.plot_pie_chart("우울_남학생", ax[1], "우울감을 경험한 남학생")
        self.plot_pie_chart("우울_여학생", ax[2], "우울감을 경험한 여학생")
        plt.savefig("images/depression.png")

    def suicide(self): # 자살 생각률 시각화: 전체, 남학생, 여학생
        fig, ax = plt.subplots(1, 3, figsize=(16,8))
        self.plot_pie_chart("자살_생각률", ax[0], "자살을 생각한 적이 있다")
        self.plot_pie_chart("자살_남학생", ax[1], "자살을 생각한 남학생")
        self.plot_pie_chart("자살_여학생", ax[2], "자살을 생각한 여학생")
        plt.savefig("images/suicide.png")


if __name__ == "__main__":
    tm = TeenageMental("data/teenage_mental.xlsx")
    data = tm.data
    tmv = TeenageMentalVisualizer(data)
