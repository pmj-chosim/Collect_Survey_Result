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
