# 파트 05 : AI 모델 테스트하기  

## 1. AI 테스트하기 - Documetn Intelligence에서  
  
#### (1) 왼쪽 배너의 Test를 클릭합니다.  

#### (2) 마지막으로 다운받았던, 5번의 (5) 파일 중 하나를 업로드해봅니다.  
  
#### (3) Analysis 버튼을 눌러 AI로 설문조사 내용을 분석합니다.  

![image](https://github.com/pmj-chosim/azureappdeploy/assets/114579651/6c9ea7af-d09d-4b5f-a6f4-5f2bf0844b48)


## 2. API 형태로 사용해보기  
<br>

#### (1) 아래 주소 repository를 포크 후codespace를 생성해 vscode를 엽니다.
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

    # #blob에서 예제 1의 url : https://계정이름.blob.core.windows.net/gabs101/예제1.pdf 이렇게 되어 있는데 https://계정이름.blob.core.windows.net/gabs101/ 이걸 붙여넣기
    blob_url = f'https://gabs101.blob.core.windows.net/gabs101/{file_name}' # #메모했던 예제1  URL 일부 내용으로 수정. /{file_name}은 그대로 둬 주세요
  ```

*참고 : Code API로 바로 제공해주는 거는 blob SAS링크 사용해야함. blob 인증키 코드가 포함안돼서

#### (5) 두 번째, 세 번 박스(코드)를 실행합니다.  

![image](https://github.com/pmj-chosim/azureappdeploy/assets/114579651/92a412d0-01d3-4cff-be19-4365928f89b9)  

API를 호출해서도  다음 같이 설문조사 내용 분석 결과를 얻을 수 있는 것을 확인 가능합니다.  

하지만 결과에 굳이 필요하지 않은 정보들도 많습니다.  


#### (6) 네 번째, 다섯 번째, 여섯 번쨰 코드를 실행합니다.

![image](https://github.com/pmj-chosim/azureappdeploy/assets/114579651/444b377b-6865-41e2-95df-992f59d490a1)

실행 후 txt폴더의 txt 파일 내용들을 보면, 값이 더 간소하게 잘 추출된 것을 확인할 수 있습니다.

  <br>
    
#### (7) 나머지 코드들도 전부 실행합니다.
  
해당 코드들을 실행하고 나면 왼쪽 배너에 output.csv가 생길 것입니다. 이 파일 위에서 마우스 우 클릭 버튼을 누른 후, 다운로드 버튼을 선택해 다운합니다.
![image](https://github.com/pmj-chosim/azureappdeploy/assets/114579651/a358b7bd-903b-4e6c-b709-25ce0a00d3a8)


#### (8) 다운 받은 output.csv를 엑셀에서 열어서  설문조사 수합 결과를 확인합니다.

엑셀에 들어가 새 엑셀 파일을 만든 후, 데이터>텍스트/csv에서 버튼을 클릭해주세요.  
다운 받은 csv 파일을 선택한 후, 열어 줍니다.  
![image](https://github.com/pmj-chosim/azureappdeploy/assets/114579651/f3182f22-b3c8-4db9-b20a-3cdbc3f6492e)  

![image](https://github.com/pmj-chosim/azureappdeploy/assets/114579651/2fb02c3c-0a1e-4310-a5d8-f037e388c4c3)  
위와 같이 설문조사 수합 결과를 확인할 수 있습니다.
    
