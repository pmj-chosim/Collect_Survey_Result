import json
import re

def parse_file(file_path):
    with open(file_path, "r") as file:
        memo = file.read()
        #print(memo)

        reason_section = re.search(r"reason: '(.*?)'", memo)
        learnt_section = re.search(r"learnt: '(.*?)'", memo)
        information_section_match = re.search(r"information: '{(.+?)}'", memo) 
        satis_survey_section = re.search(r"satis_survey:\s*'\[(.*?)\]'", memo) 

        information_data = {}

        print(0)
        print(str(information_section_match))
        if information_section_match:
                    information_text = information_section_match.group(1)  # Extract key
                    print("txt : "+str(information_section_match))

                    # Improved regex for nested dictionaries
                    info_pattern = r"'(\w+)': DocumentField\(value_type=dictionary, value={'ROW1': DocumentField\(value_type=string, value='(.*?)', content=(.*?),"

                    

                    # Use information_text directly in finditer
                    for match in re.finditer(info_pattern, information_text):
                        key = match.group(1)
    
                        content = match.group(3).strip(",")
                        information_data[key] = {'content': content}
                
                #print(value)

        satis_survey_data = []
        if satis_survey_section:
            satis_survey_text = satis_survey_section.group(1)
            for match in re.finditer(r"\{.*?\}", satis_survey_text):
                value = match.group()
                satis_match = re.search(r"'satis':\s*DocumentField.*?value='(.*?)'", value)
                dissatis_match = re.search(r"'dissatis':\s*DocumentField.*?value='(.*?)'", value)
                satis = satis_match.group(1).strip() if satis_match else None
                dissatis = dissatis_match.group(1).strip() if dissatis_match else None
                satis_survey_data.append({'satis': satis, 'dissatis': dissatis})

    return {
        'reason': reason_section.group(1) if reason_section else None,
        'learnt': learnt_section.group(1) if learnt_section else None,
        'information': information_data,
        'satis_survey': satis_survey_data
    }


test_files=["예제1", "예제2"]
for i in test_files:
    txt_file_path = "./txt/"+str(i)+".txt"

    # 함수 호출 및 결과 출력
    parsed_data = parse_file(txt_file_path)
    print(parsed_data)
    '''
    # 딕셔너리를 JSON 형식의 문자열로 변환
    json_data = json.dumps(parsed_data, ensure_ascii=False)

    # 파일을 쓰기 모드로 열기 (파일이 없으면 생성됨)
    with open(txt_file_path, "w", encoding="utf-8") as file:
        # JSON 형식의 문자열을 파일에 쓰기
        file.write(json_data)'''