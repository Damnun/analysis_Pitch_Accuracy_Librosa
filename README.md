# analysis_Pitch_Accuracy_Librosa
Analyze the accuracy of vocal tones between songs using ribrosa.
## 🛠 프로젝트 구성 안내
- 목적

> 저희들은 평소에 노래를 연습할 때, 자식이 부른 노래가 어떤 부분에서 음정이 맞지 않는지 일일이 파악하기가 어렵습니다. 노래 연습을 할 때 사용자가 부른 노래의 음원 파일을 대상으로 반주와 음원을 불리하고, 사용자의 음정과 음원의 음정을 시각화된 그래프로써 비교해서 보여주는 서비스를 제공하고자 이 프로젝트를 진행했습니다.

## 📌 사용 언어, 툴 및 라이브러리
Python Librosa, Spleeter, mathplotlib 라이브러리를 활용해 pitch analysis, Graph Diagramming, Voice Seperation 등의 기능을 구현했습니다.

## ⏰ 개발 기간
2022년 04월 12일 ~ 2022년 06월 22일

## 필수 설치 요소
```
pip install pydub  
```
★ ffmpeg 설치 필수 ★

## 사용시 이미지
> 확인해 보고 싶은 mp3파일을 src에 넣으면 이를 wav파일(스펙트럼화 시킬 수 있는)로 변환해 줍니다.
![image](https://user-images.githubusercontent.com/97078660/174974974-94954cde-1745-442b-befa-6874b84f881d.png)
> 이를 spleeter를 활용해서 보컬과 mr파일을 분리한 뒤 보컬의 음정을 스펙트럼화 시켜 사용자에게 보여줍니다.
![image](https://user-images.githubusercontent.com/97078660/174974328-cb777aca-7722-4848-bd02-9babba09a1ee.png)




- 만든 사람
> <a href="https://github.com/Damnun">이재헌
> <a href="https://github.com/kkkkkk0312">강재영
> <a href="https://github.com/korean0106">남효천
