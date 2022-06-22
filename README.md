# analysis_Pitch_Accuracy_Librosa
Analyze the accuracy of vocal tones between songs using ribrosa.
## 🛠 프로젝트 구성 안내
# - 프로젝트 개요

> 저희들은 평소에 노래를 연습할 때, 자식이 부른 노래가 어떤 부분에서 음정이 맞지 않는지 일일이 파악하기가 어렵습니다. 노래 연습을 할 때 사용자가 부른 노래의 음원 파일을 대상으로 반주와 음원을 불리하고, 사용자의 음정과 음원의 음정을 시각화된 그래프로써 비교해서 보여주는 서비스를 제공하고자 이 프로젝트를 진행했습니다.

## 📌 사용 언어, 툴 및 라이브러리
Python Librosa, Spleeter, mathplotlib 라이브러리를 활용해 pitch analysis, Graph Diagramming, Voice Seperation 등의 기능을 구현했습니다.

## 오픈소스 활용
> 바이브레이션 비율 – Zero Crossing Rate 활용 : 음파의 양/음 비율 빈도수
> Librosa를 통해 입력받은 주파수를 mathplotlib 그래프나 스펙트럼 그래프로 표시하여 사용자로 하여금 직관적으로 이를 파악할 수 있게 도와줌
> Spleeter 라이브러리를 통해 노래의 반주와 사용자의 목소리를 분리하여 Librosa에 활용할 계획
> 파일 저장 및 음원 추출 – pydub, pytube Module 활용

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

#### 코드실행 화면
![image](https://user-images.githubusercontent.com/97078660/175094539-c17731ff-6579-4b49-add6-7d5ecd9b603f.png)

#### spleeter를 사용해서 음원을 분리하기 전의 주파수 분석 사진입니다.
![image](https://user-images.githubusercontent.com/97078660/175095270-2e0143af-1f21-4eb4-888c-786ba9e4de42.png)

#### spleeter를 사용해서 음원을 분리한 후의 주파수 분석 사진입니다.
![image](https://user-images.githubusercontent.com/97078660/175095367-c35ffccb-1253-4e80-be63-80dfc413a585.png)

#### > 잡음이 없는 경우의 주파수 분석 사진입니다.
![image](https://user-images.githubusercontent.com/97078660/174974328-cb777aca-7722-4848-bd02-9babba09a1ee.png)




- 만든 사람
> <a href="https://github.com/Damnun">이재헌
  ```
  분리된 음원 그래프로 가시화, 전체적인 코드 최적화 및 정리
  ```
> <a href="https://github.com/kkkkkk0312">강재영
  ```
  mp3에서 wav로의 변환, readme 파일 작성
  ```
> <a href="https://github.com/korean0106">남효천
  ```
  음원을 악기 및 목소리로 분리
  ```
