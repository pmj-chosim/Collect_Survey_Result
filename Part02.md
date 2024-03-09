# 파트 02 : AI 작업 환경 셋팅하기

<br>
파트 2에서는 AI 작업 환경을 셋팅하겠습니다.  
<br>
<br>
<br>

## 3. 작업 환경 만들기
  

#### (1)마우스로 스크롤해 화면의 맨 밑으로 이동합니다.    
#### (2) 'Custom extraction model'을 클릭합니다.  
![](https://github.com/pmj-chosim/azureappdeploy/raw/main/img/9.png)  
  
#### (3) 마우스 스크롤을 내리면 보이는 My Projects 글자 밑의 '+ Create a project'를 클릭합니다.    
![](https://github.com/pmj-chosim/azureappdeploy/raw/main/img/10.png)  
  
#### (4) 프로젝트 이름을 마음대로 지어 준 후, 하단의 'Continue' 버튼을 클릭합니다.  
![](https://github.com/pmj-chosim/azureappdeploy/raw/main/img/11.png)   

### (5)AI 서비스 리소스를 생성
### 아래 사진과 같이, 리소스 그룹, 서비스 리소스, API 버전을 클릭하세요.  
<br>

![](https://github.com/pmj-chosim/azureappdeploy/raw/main/img/12.png)    
리소스 그룹은 **'GAB-S1-XX'**(XX는 자기 번호)를 선택하고,  
서비스 리소스는 **'GlobalAIBootCamp-S1-XX'를 선택합니다.  
API 버전은 ~~를 선택한 후,  
Continue 버튼을 클릭합니다.  
<br><br>

### (9) 데이터 저장소(blob)를 만들겠습니다.
### 해당하는 구독과 2번에서 만들었던 리소스이름 값을 선택합니다.
![](https://github.com/pmj-chosim/azureappdeploy/raw/main/img/13.png)    
  
Create new stroage account 버튼을 클릭후, 스토리지 계정 이름(Storage account name)을 정해줍니다.  
Location(위치)는 아무것이나 선택해도 상관없나, 스토리지 가격이 저렴한 'Central India'를 선택하겠습니다.  
Pricing Tier(가격)는 Standard_GRS Standard를 선택합니다.  
Blob Container name(데이터 저장 컨테이너 이름)을 마음대로 지어 줍니다.  
Folder Path에는 아무것도 입력하지 않고, 'Continue'버튼을 누릅니다.  
Create project를 선택합니다.  

<br>

# 4. 설문조사 문서들에서 핵심 내용을 뽑아 낼 수 있는 AI 만들기

* 문서에서 추출하고 싶은 부분에 라벨 붙여주기
링크~~~
(1) 위 링크에 있는 pdf 파일을 다운받습니다.
(2) 다운받은 파일을 클라우드 모양에 드래그해 업로드 합니다.
run layout 실행
(3) 'Add a field'를 클릭 후, 필드를 선택합니다. 'FirstAnswer'라고 이름을 정하겠습니다. 이름을 적은 후, enter를 누릅니다.
(4)  'Add a field'를 다시 클릭 후, 필드를 선택한 다음, 'SecondAnswer'라고 이름을 적습니다. 적은 후, enter를 누릅니다.
(5) 표1
(6) 표2
(7) 드래그 리전을 선택 후, 네모 박스를 친다음, 네모 박스가 해당하는 내용의 라벨을 선택합니다.
여러 가지....

(8) Train을 클릭합니다.

(9) Model이 학습 완료되길 기다립니다.


- 모델이 학습될 동안, 여러 설문조사 결과 문서들에서 추출할 수 있게 환경을 만들겠습니다.

# 5. AI API에 필요한 엔드포인트와 Key 찾기
(1) Azure portal에 재접속합니다.
(2) 탐색>리소스 클릭 후, 2(리소스 만들기)과정에서 만들었던 리소스 그룹 명을 선택합니다.
(3) 리소스 그룹 안의 그림 모양(Blob)을 클릭합니다.
(4) 왼쪽 배너의 데이터스토리지>컨테이너를 클릭한 후, 2번째 요소를 클릭합니다.
(5) 링크의 파일들을 다운 받고, 컨테이너에 업로드합니다.
(6) 액세스키 클릭 후, 스토리지 계정 이름과 key1의 키 값을 메모장에 메모해 둡니다.
(7) azure ai 리소스를 클릭후, 리소스관리> 키 및 엔드포인트를 클릭합니다. 키1과 엔드포인트값을 복사 후, 메모장에 메모해주세요.
(8)다시 Document Intelligence Studio 로 돌아갑니다.
(9) 왼쪽 배너의 Models를 클릭 후, 생성된 모델명의 이름도 메모장에 메모해주세요.

# 6. AI 테스트하기
(1) 왼쪽 배너의 Test를 클릭합니다.
(2) 마지막으로 다운받았던, 5번의 (5) 파일 중 하나를 업로드해봅니다.
(3) Analysis 버튼을 눌러 AI로 설문조사 내용을 분석합니다.

# 7. API 형태로 사용해보기
(1) 해당 repository를 포크 후codespace를 생성해 vscode를 엽니다.
(2) ~~~.ipynb의 첫 번째 박스(코드)의 실행 버튼(세모)을 클릭합니다.
(3) 두 번째 박스(코드) 부분에 해당하는 값을 채워넣습니다.(메모장에 복사해뒀것들)
*참고 : Code API로 바로 제공해주는 거는 blob SAS링크 사용해야함. blob 인증키 코드가 포함안돼서
(4) 두 번째 박스(코드)를 실행합니다.
출력 잘 되는지 확인하기

# 8. API 호출 결과 메모파일들 생성하고, 키워드 뽑기
(1) API 호출 결과 프린트 대신 txt 생성 및 txt로 출력
(2) for문으로 메모장들 열어서 content 값 뽑아서 csv 만들기
(3) 엑셀에서 csv 파일 열어 확인하기
