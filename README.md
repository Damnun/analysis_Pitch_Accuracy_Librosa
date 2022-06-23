# analysis_Pitch_Accuracy_Librosa
Analyze the accuracy of vocal tones between songs using ribrosa.

## 🛠 프로젝트 구성 안내

# - 프로젝트 개요
> 평소 노래를 연습할 때 본인이 부른 노래가 어떤 부분에서 음정이 맞지 않는지 일일이 파악하기란 쉽지 않다.

> 사용자가 부른 노래의 음원 파일을 반주와 음원으로 분리하고, 사용자와 음원간의 주파수(음정)값 차이를 그래프로 나타내는 프로그램을 제작하였다.

> “https://github.com/librosa/librosa“ 내의 librosa를 포함, spleeter, matplotlib 등의 모듈을 활용하여 사용자가 부르는 노래의 음정을 반주/목소리로 분할한 후 기존의 음원파일 내 가수의 음정과 함께 각각의 주파수로 인식하여 높낮이를 가시화

> 노래를 연습할 때 기준 음원 파일을 대상으로 반주/음원 분리, 음정 정확도 분석, 분석된 음정 그래프 시각화 서비스를 제공하고자 함.

## 📌 사용 언어, 툴 및 라이브러리
Python Librosa, Spleeter, matplotlib 라이브러리를 활용해 pitch analysis, Graph Diagramming, Voice Seperation 등의 기능을 구현.

## 오픈소스 활용
+ 바이브레이션 비율 – Zero Crossing Rate 활용 : 음파의 양/음 비율 빈도수
+ Librosa를 통해 입력받은 주파수를 matplotlib로 그래프나 스펙트럼 그래프 형태로 표시하여 사용자로 하여금 직관적으로 이를 파악할 수 있게 도와줌
+ Spleeter 라이브러리를 통해 노래의 반주와 사용자의 목소리를 분리하여 Librosa에 활용할 계획
+ 파일 저장 및 음원 추출 – pydub, pytube Module 활용

## 개선사항 및 향후 계획
+ 음원의 mr분리를 통해 목소리를 직관적인 형태의 그래프로 추출해냈지만 두 그래프를 효과적으로 비교하여 그래프화 하는 데에는 시간적인 어려움이 있었음.
+ 주파수 영역에서 드러나는 잡음을 제한하는 연구를 통해 효과적인 비교 그래프 생성을 목적으로 함.

## ⏰ 개발 기간
2022년 04월 12일 ~ 2022년 06월 22일

## 필수 설치 요소
```
pip install pydub  
```

★ ffmpeg 설치 필수 ★

## 사용시 이미지
#### > 확인해 보고 싶은 mp3파일을 src에 넣으면 이를 wav파일(스펙트럼화 시킬 수 있는)로 변환해 줍니다.
![image](https://user-images.githubusercontent.com/97078660/174974974-94954cde-1745-442b-befa-6874b84f881d.png)

#### spleeter를 사용해서 음원을 분리하기 전의 주파수 분석 사진입니다.
![image](https://user-images.githubusercontent.com/97078660/175095270-2e0143af-1f21-4eb4-888c-786ba9e4de42.png)

#### spleeter를 사용해서 음원을 분리한 후의 주파수 분석 사진입니다.
![image](https://user-images.githubusercontent.com/97078660/175095367-c35ffccb-1253-4e80-be63-80dfc413a585.png)

#### > 잡음이 없는 경우의 주파수 분석 사진입니다.
![image](https://user-images.githubusercontent.com/97078660/174974328-cb777aca-7722-4848-bd02-9babba09a1ee.png)




- 만든 사람
> <a href="https://github.com/Damnun">이재헌
  ```
  librosa - 분리된 음원 그래프로 가시화, 전체적인 코드 최적화 및 정리
  ```
> <a href="https://github.com/kkkkkk0312">강재영
  ```
  mp3에서 wav로의 변환, readme 파일 작성
  ```
> <a href="https://github.com/korean0106">남효천
  ```
  spleeter - 음원을 악기 및 목소리로 분리
  ```
