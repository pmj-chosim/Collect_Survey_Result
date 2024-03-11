# Par04. AI API에 필요한 엔드포인트와 Key 찾기

### API란 무엇일까요?
API는 소프트웨어 사이에서 원하는 정보를 쉽게 주고 받을 수 있게 하는 것입니다.  
지금 만드는 AI 기능을 사용해 얻은 정보를 다른 곳(코드나 소프트웨어)에서도 쉽게 얻을 수 있게 하는 것입니다.
<br>
<br>
  
지금 만드는 AI의 API를 만들기 위해 아래 정보 수집 과정을 따라 주세요.  
  
#### (1) Azure portal에 재접속합니다. 
👉 [Azure portal 주소](https://azure.microsoft.com/ko-kr/get-started/azure-portal)    
  
#### (2) 탐색>리소스 클릭 후, 2(리소스 만들기)과정에서 만들었던 리소스 그룹 명을 선택합니다.  
![](https://github.com/pmj-chosim/azureappdeploy/raw/main/img/21.png)  
  
#### (3) 리소스 그룹 안의 림 모양(Blob)을 클릭합니다.
![](https://github.com/pmj-chosim/azureappdeploy/raw/main/img/24.png)  
  
#### (4) 액세스키 클릭 후, 스토리지 계정 이름과 key1의 키 값을 메모장에 메모해 둡니다.
  
 ![](https://github.com/pmj-chosim/azureappdeploy/raw/main/img/25.png)  
  
#### (5) 링크의 파일들을 다운 받습니다.
  
 [Test용 파일](https://github.com/pmj-chosim/azureappdeploy/tree/main/filedown/test)    
  
각 파일에 들어가 우측 상단의 다운 버튼을 눌러 다운받습니다.


#### (6) 왼쪽 배너의 데이터스토리지>컨테이너를 클릭한 후, 2번째 요소를 클릭합니다.  
  
![](https://github.com/pmj-chosim/azureappdeploy/raw/main/img/26.png)  

<br>

업로드를 클릭한 후, 다운 받은 파일들을 업로드합니다.  
  
![](https://github.com/pmj-chosim/azureappdeploy/raw/main/img/26.png)  

<br>

업로드된 파일 중 '예제1'을 클릭한 후, **URL을메모** 해 둡니다.  
  
![](https://github.com/pmj-chosim/azureappdeploy/raw/main/img/28.png)  

<br>
    
#### (7) 리소스 그룹에서 azure ai 리소스를 클릭후, 리소스관리> 키 및 엔드포인트를 클릭합니다. 키1과 엔드포인트값을 복사 후, 메모장에 메모해주세요.  
*리소스 그룹에 접속하는 방법을 모르겠다면 마우스 스크롤을 올려 (1)~(2)번 내용를 다시 참고해주세요.   
<br>  

![](https://github.com/pmj-chosim/azureappdeploy/raw/main/img/22.png)  
![](https://github.com/pmj-chosim/azureappdeploy/raw/main/img/23.png)  

   
#### (8)다시 Document Intelligence Studio 로 돌아갑니다.
#### (9) 왼쪽 배너의 Models를 클릭 후, 생성된 모델명의 이름도 메모장에 메모해주세요.

![image](https://github.com/pmj-chosim/azureappdeploy/assets/114579651/f3c114a5-e884-43b0-a12a-7cedd4e7a8c0)  
<br>
first_model을 메모해주면 됩니다.




<br>

### >>>>> 파트 5 ->  [Part5](https://github.com/pmj-chosim/azureappdeploy/blob/main/sessionguide/Part05.md) 

