# 파트 05 : AI 모델 테스트하기  

## 1. AI 테스트하기 - Documetn Intelligence에서  
  
#### (1) 왼쪽 배너의 Test를 클릭합니다.  

#### (2) 마지막으로 다운받았던, 5번의 (5) 파일 중 하나를 업로드해봅니다.  
  
#### (3) Analysis 버튼을 눌러 AI로 설문조사 내용을 분석합니다.  

![image](https://github.com/pmj-chosim/azureappdeploy/assets/114579651/6c9ea7af-d09d-4b5f-a6f4-5f2bf0844b48)


## 2. API 형태로 사용해보기  
<br>


[레포지토리 주소](https://github.com/pmj-chosim/azureappdeploy)   

#### (1) 위 주소에 접속해 로그인 후,  repository를 포크한 다음, codespace를 생성해 vscode를 엽니다.
![image](https://github.com/pmj-chosim/azureappdeploy/assets/114579651/ca71d2c0-b41b-4317-bc98-b48f6b9872b6)  
  ![image](https://github.com/pmj-chosim/azureappdeploy/assets/114579651/e3362e01-514b-4023-ac9b-553fd9a150a3)  
![image](https://github.com/pmj-chosim/azureappdeploy/assets/114579651/bf6b95f4-6914-4a51-a7f7-6e52c8bbcd8f)  

<br>

#### (2)survey.ipynb을 왼쪽 배너에서 찾아서 클릭합니다.
![image](https://github.com/pmj-chosim/azureappdeploy/assets/114579651/674ed631-039a-4f77-99d9-93ab4ecd3aae)


파이썬 확장을 설치해줍니다  
![image](https://github.com/pmj-chosim/azureappdeploy/assets/114579651/9b0d6f8b-ea1d-4fea-9e6b-4404a81d9ac5)
  
<br>
  

#### (3) survey.ipynb의 첫 번째 박스(코드)의 실행 버튼(세모)을 클릭합니다.  
![image](https://github.com/pmj-chosim/azureappdeploy/assets/114579651/e39fa061-a9b4-4c69-ad0c-65b5cc4193a9)  




#### (4) 두 번째 박스(코드) 부분에 # #로 수정이 필요하다고 명시한 값들을 수정합니다.(메모장에 복사해두었던 내용을 바탕으로 수정하세요)  
아래는 예시입니다. 
   ```
    form_recognizer_endpoint = "https://globalaibootcamp-s1-01.cognitiveservices.azure.com/" # #메모했던 내용으로 수정
    form_recognizer_key = "75b7320edf304e52981f453cfda924ad" # #메모했던 내용으로 수정
    model_id = "first_model" #메모했던 내용으로 수정
    
    blob_account_name = "gabs101" #메모했던 내용으로 수정
    blob_account_key = "BP3TFJ+rMuxxCq/zDutEjqVCuuAfjijzEaUEe07wwsofI2XTpZ/+w0hRxMEV2wQYYIlCDvV7Ubez+AStoDXWeA==" # #메모했던 내용으로 수정

    # #blob에서 예제 1의 url : https://계정이름.blob.core.windows.net/gabs101/예제1.pdf 이렇게 되어 있는데 h더 자세히 알아 보고 싶다면?  
[더 자세히 알아보기](https://github.com/pmj-chosim/Collect_Survey_Result/blob/main/sessionguide/More.md)


