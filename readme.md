# 1. Azure portal 로그인
<url> https://azure.microsoft.com/ko-kr/get-started/azure-portal
위의 Azure portal 링크에 접속한 후, 로그인을 해주세요.

# 2. 리소스 만들기

(1)Azure portal 좌측상단의 '리소스 만들기(+)'를 클릭합니다.
(2) 좌측의 범주 배너에서 'AI+기계 학습'을 클릭합니다.
(3) 'Azure AI services'를 클릭합니다.
(4) 리소스 이름 등등 짓고 가격 책정하기
(5) '검토 + 만들기' 클릭 후 대기합니다.
(6) '만들기' 버튼을 클릭합니다.
(7) '리소스로 이동'을 클릭합니다.
(8) 'Document Intelligent'를 선택합니다.
(9) 'Document Intelligent Studio'의 '스튜디오로 이동'을 클릭합니다.


# 3. 작업 환경 만들기
(1)마우스로 스크롤해 화면의 맨 밑으로 이동합니다.
(2) 'Custom extraction model'을 클릭합니다.
(3) 마우스 스크롤을 내리면 보이는 My Projects 글자 밑의 '+ Create a project'를 클릭합니다.
(4) 프로젝트 이름을 마음대로 지어 준 후, 하단의 'Continue' 버튼을 클릭합니다.
(5)구독(Subscription)에 자동으로 뜨는 값 또는 사용하기 원하는 구을 선택합니다.
(6) 2번(작업 환경 만들기)에서 만들었던 리소스이름을 클릭합니다.
(7) Document Intelligence or Cognitive Service Resource에 이미 있는 값을 선택합니다.
(8) Continue 버튼을 클릭합니다.
--blob
(9) 해당하는 구독과 2번에서 만들었던 리소스이름 값을 선택합니다.
(10) Create new stroage account 버튼을 클릭후, 스토리지 계정 이름(Storage account name)을 정해줍니다.
(11) Location(위치)는 아무것이나 선택해도 상관없나, 스토리지 가격이 저렴한 'Central India'를 선택하겠습니다.
(12) Pricing Tier(가격)는 Standard_GRS Standard를 선택합니다.
(13) Blob Container name(데이터 저장 컨테이너 이름)을 마음대로 지어 줍니다.
(14) Folder Path에는 아무것도 입력하지 않고, 'Continue'버튼을 누릅니다.
(15) Create project를 선택합니다.

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


