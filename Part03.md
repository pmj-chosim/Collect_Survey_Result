# 파트 03: 설문조사 문서들에서 핵심 내용을 뽑아 낼 수 있는 AI 만들기

## * 문서에서 추출하고 싶은 부분에 라벨 붙여주기
  
[AI train용 설문조사 pdf](https://github.com/pmj-chosim/azureappdeploy/tree/main/filedown/train)  
  
#### (1) 위 링크에 있는 pdf 파일들을 다운받습니다.  

![image](https://github.com/pmj-chosim/azureappdeploy/assets/114579651/c9a78ec8-45d6-40f5-9587-1470e9c7c013)

각 파일에 들어 가서 우측의 다운 버튼을 누르면 됩니다.

  
#### (2) 다운받은 파일들을 클라우드 모양에 드래그해 업로드 합니다.  
![](https://github.com/pmj-chosim/azureappdeploy/raw/main/img/14.png)  
![](https://github.com/pmj-chosim/azureappdeploy/raw/main/img/15.png)    
![](https://github.com/pmj-chosim/azureappdeploy/raw/main/img/16.png)  

   <br>
아래 방법들을 통해 설문조사 문서에서 데이터 추출할 영역을 레이블해주겠습니다.  

#### (3) 레이블
run layout > Unanalyzed documents 버튼 클릭.


<br>

![image](https://github.com/pmj-chosim/azureappdeploy/assets/114579651/628bcf4e-e8c8-416d-ae79-4d7dad09448d)

  
  
우측 상단의 'Add a field'를 클릭 후, 필드를 선택합니다.  
'reason'라고 이름을 정하겠습니다. 이름을 적은 후, enter를 누릅니다.  

<br>
  
'Add a field'를 다시 클릭 후, 필드를 선택한 다음, 'learnt'라고 이름을 적습니다. 적은 후, enter를 누릅니다.

'Add a field'를 다시 클릭, 'Table'을 선택 후, 표 이름을 'information', 'Fixed', 'Column'을 선택 후 'Create' 버튼을 클릭합니다.  

'Add a field'를 다시 클릭, 'Table'을 선택 후, 표 이름을 'satis_survey', 'Dynamic', 'Row'를 선택 후 'Create' 버튼을 클릭합니다.  

<br>

레이블링할 요소 이름들을 등록해주었으니, 이제 레이블링을 하겠습니다.

<br>
    
## [유튜브 비디오(클릭)](https://youtu.be/CY-9vIM-8SE)
## 위 링크의 영상을 보고, 라벨링을 따라해주세요

![image](https://github.com/pmj-chosim/azureappdeploy/assets/114579651/5f8897a1-efbe-4e81-a880-9163c3c7a65b)  

다른 파일들도 동일하게 라벨링을 해줍니다.  
방법을 잘 모르겠다면 하단 링크의 영상을 참고해주세요.  
  
### [유튜브 비디오(클릭)](https://youtu.be/_lTPUlygmUI)
<br><br>

#### (4) Train을 클릭합니다.  
![image](https://github.com/pmj-chosim/azureappdeploy/assets/114579651/73522b3c-fc22-4e5c-be0d-e12a03dc87c1)  
model이름은 first_model, build mode는 templete을 선택합니다.


#### (5) Model이 학습 완료되길 기다립니다.


모델이 학습될 동안, 여러 설문조사 결과 문서들에서 추출할 수 있게 환경을 만들겠습니다.
