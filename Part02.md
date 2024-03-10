# 파트 02 : AI 작업 환경 셋팅하기

<br>
파트 2에서는 AI 작업 환경을 셋팅하겠습니다.  
<br>
<br>
<br>

## 1. 작업 환경 만들기
  

#### (1)마우스로 스크롤해 화면의 맨 밑으로 이동합니다.    
#### (2) 'Custom extraction model'을 클릭합니다.  
![](https://github.com/pmj-chosim/azureappdeploy/raw/main/img/9.png)  
  
#### (3) 마우스 스크롤을 내리면 보이는 My Projects 글자 밑의 '+ Create a project'를 클릭합니다.    
![](https://github.com/pmj-chosim/azureappdeploy/raw/main/img/10.png)  
  
#### (4) 프로젝트 이름을 마음대로 지어 준 후, 하단의 'Continue' 버튼을 클릭합니다.  
![](https://github.com/pmj-chosim/azureappdeploy/raw/main/img/11.png)   

#### (5)AI 서비스 리소스를 생성
#### 아래 사진과 같이, 리소스 그룹, 서비스 리소스, API 버전을 클릭하세요.  
<br>

![](https://github.com/pmj-chosim/azureappdeploy/raw/main/img/12.png)    

<br>
리소스 그룹은 **'GAB-S1-XX'**(XX는 자기 번호)를 선택하고,  <br>
서비스 리소스는 **'GlobalAIBootCamp-S1-XX'를 선택합니다.  <br>
API 버전은 **'2023-07-31'** version을 선택한 후,  <br>
Continue 버튼을 클릭합니다.  <br>
<br><br>

### (9) 데이터 저장소(blob)를 만들겠습니다.
### 해당하는 구독과 2번에서 만들었던 리소스이름 값을 선택합니다.
![](https://github.com/pmj-chosim/azureappdeploy/raw/main/img/13.png)    

<br>  

Create new stroage account 버튼을 클릭후, 스토리지 계정 이름(Storage account name)을 정해줍니다.  
Location(위치)는 아무것이나 선택해도 상관없나, 'East US'를 선택하겠습니다.  
Pricing Tier(가격)는 Standard_GRS Standard를 선택합니다.  
Blob Container name(데이터 저장 컨테이너 이름)을 마음대로 지어 줍니다.  
Folder Path에는 아무것도 입력하지 않고, 'Continue'버튼을 누릅니다.  
Create project를 선택합니다.  

<br>

  
