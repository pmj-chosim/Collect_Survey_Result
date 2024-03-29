# 파트 06 : 더 자세히 알아보기

## 1. Azure 서비스 사용


![image](https://github.com/pmj-chosim/Collect_Survey_Result/assets/114579651/80320bb2-d1fd-4569-bc03-b0cca49b5f03)

1. Azure에서 서비스를 사용하려면, 먼저 Azure 계정에 가입해야 합니다.  
1. Azure에 가입해 계정이 생성되면, 구독을 만들어야 하는데요.  
1. 이 **구독**은 넷플릭스 구독같이, Azure 서비스를 사용한다고 구독하는 것입니다.  
 서비스를 사용할 때 어디서(카드, 통장 등) 서비스 요금이 부과될 지 등록해 구독을 만듭니다.  
1. 구독 및에서 리소스 그룹을 만들면, 드디어 Azure 서비스를 사용할 수 있습니다.  
   리소스 그룹은 직역하면, 자원을 모아놓은 것인데요. 이 뜻처럼 AI 서비스나, 보안 서비스나 기타 여러 Azure의 서비스와 컴퓨터 자원들을 담아 놓은 곳입니다.
    Azure의 모든 서비스는 리소스 그룹 및에서 생성되어야 합니다.  
  
1. 리소스 그룹이 만들어지면, 이 리소스 그룹 안에서 리소스를 만듭니다.
   리소스는 AI 서비스, 웹 앱 서비스같은 서비스나 컴퓨팅 자원 등 입니다.

   👉 _Azure 기본 개념(계정, 구독, 리소스 등)에 대해 더 자세히 알고 싶다면 아래 링크를 참고해 주세요._
   > [Azure 기본 개념](https://woowah.tistory.com/4)  
  
## 2. 설문 조사 한 큐에 수합하기

![image](https://github.com/pmj-chosim/Collect_Survey_Result/assets/114579651/026a0300-b228-42f9-acc8-2e474bfb754b)


 #### 설문 조사 한 큐에 수합하기 세션은 위와 같은 방법을 통해 진행합니다.

   * Azure에서는  Azure AI services(리소스)의 **Doucment Intelligence** (문서 추출 AI) 기능과  **Azure Blob Storage**(설문조사 파일 저장용)를 사용합니다.
           👉[Document Intelligence 알아보기](https://learn.microsoft.com/ko-kr/azure/ai-services/document-intelligence/overview?view=doc-intel-4.0.0)<br>
           👉[Azure Blob Storage 알아보기](https://learn.microsoft.com/ko-kr/azure/storage/blobs/storage-blobs-introduction) <br>
             
   * **Doucment Intelligence**와 **Azure Blob Storage** 정보를 **GitHub Codespaces**에서 전달받고(API 호출), <br>
           👉[Codespaces에 대해 알아보기](https://docs.github.com/ko/codespaces/overview)<br>
           👉[API 개념 알아보기](https://www.redhat.com/ko/topics/api/what-are-application-programming-interfaces)  
   * 이 정보에서 필요한 부분만 Python으로 추출해 엑셀 파일로 정리합니다.   

 ## 3. 내용 매칭해보기
 [Part1 ~ Part5 가이드 문서](https://github.com/pmj-chosim/Collect_Survey_Result/blob/main/sessionguide/Part01.md)를 다시 읽으며, <br>
 Part1 ~ Part5의 내용들과 위 1, 2번 설명 내용을 1대1 매칭해보세요.  
   
 (예 : Part1은 1번 사진에 있는 Azure 서비스의 리소스 그룹과 리소스를 만드는 과정입니다. )  
 (예 : Part5는 Codespaces에서 파이썬을 사용해 API 호출 결과를 엑셀 파일을 만드는 과정입니다. )


 ## 4. 코드 톺아보기
 **survey.ipynb**는 Azure 서비스 API 호출 결과를 엑셀에서 열 수 있는 CSV 파일이 되도록 정리하는 역할을 합니다.  
 이 코드의 **셀** 별로 **챗 GPT**나 **Bing Chat**에 설명해달라고 입력해보세요.  
 설명이 더 필요한 부분에 대해선, 자세히 설명해 달라고 하며 코드 내용을 이해해 보시길 바랍니다.  <br>
 ![image](https://github.com/pmj-chosim/Collect_Survey_Result/assets/114579651/7d5efff9-f2b8-4ecd-86e1-110c3fe69a83)
![image](https://github.com/pmj-chosim/Collect_Survey_Result/assets/114579651/4d9d678a-198e-4d09-aac1-f39c571a8e97)
![image](https://github.com/pmj-chosim/Collect_Survey_Result/assets/114579651/cf2b4b18-c33e-44f5-9c06-1267a15a4894)

   
## 5. 새로운 설문조사 수합해 보기.
새로운 설문조사 예제들을 만든 후, **Document Intelligence**로 학슴시켜, <br>
설문조사 내용들을 수합해 보세요.
