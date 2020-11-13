# MyData_for_Adverse_reaction
2020년 한국연구재단 기본연구 

2020-10-08
1) '첨가물_app.md' : 첨가물 DB 구축 관련 정보 update 정보 확인 가능한 공공데이터포털 URL & operation 상세메뉴얼 첨부

2) 다음 파일럿 프로젝트를 참고해주세요

주소: https://github.com/irreversibly/CPBMI1-
이 프로젝트는 혈압약 선정하는데 있어 1) 환자가 가지고 있는 질환을 고려해서 추천약제를 선정하는 알고리즘과, 2) 약을 먹은 이후 혈압 측정 결과에 따라 내가 사용한 약제별 가점/감점을 하는 부분이 알고리즘화 되어 있습니다. 지난번 말했던 약물 복용에 따른 부작용 발생여부를 capture에서 score에 반영하는 부분과 관련이 있습니다. 

3) SIDER 4.1 DB 

주소: http://sideeffects.embl.de/
자료: http://sideeffects.embl.de/download/
설명: README.md 파일

4) NIPA 고성능 GPU

221.160.191.58/32:8888 -> Jupyter notebook
221.160.191.58/32:3389 -> xrdp 용 주소

서버접속 정보
1) IP Address: 101.101.169.172
2) SSH port: 16022
3) ID: ubuntu
4) PW: nipa2019-0562
5) Jupyter Notebook PW: N#S-=iB9{:CKi6.

백업이 필요한 정보는 없지만, 선생님 폴더 만들고 작업하시면 될 것 같아요

2020-10-13
1) openAPI 요청이 안되는 약제의 경우, 다음 site (https://biz.kpis.or.kr/kpis_biz/index.jsp)에 가보면 중간에 전체건수 다운로드 엑셀파일이 1-4까지 있는데, 이 파일들 중에서 L열의 제품코드(개정후)에 값이 있는 경우 해당 값으로 작업을 진행해볼 수 있을 것 같아요. (약제를 찾는 경우 M열의 주성분코드값과 drug_template.xlsx 파일의 A열 주성분 코드 값이 같은 변수인데, 이게 같은 값 중에서.. drug_template.xlsx의 C열 제품명 자료를 전처리해서 숫자로 시작하는 부분 이전의 제품명이 BarCodeData.xlsx 파일의 A열과 같은지? 같으면 drug_template.xlsx의 C열 제품명 자료의 뒷쪽 한글로 15밀리그람.. 이런 부위가 BarcodeData.xlsx의 C열 정보와 같으면 같은 약제로 판단.. 이렇게 해보면 될 것 같아요.

2) openAPI 요청이 안되는 약제의 경우, 9자리 의약품표준코드의 끝자리가 잘못된 경우가 있을 수 있습니다. 해당 약제의 경우 마지막 자리를 0-5 정도까지 변경시키면서 작업을 하고, openAPI에서 찾아지는 경우 변경된 code 값을 따로 저장해주세요. 추후 확인해보겠습니다. 

3) operation 작업의 횟수가 정해져있는 openAPI의 경우, data.go.kr에서 선생님 계정을 따로 만들어도 좋습니다.

2020-10-19

1) 첨가물 DB 관련 진행사항 확인
2) 국가연구개발비로 만든 앱을 '저작권위원회' 저작권 등록(https://www.cros.or.kr/psnsys/cmmn/infoPage.do?w2xPath=/ui/twc/req/sw/regGidTxt.xml), sw 자산등록https://www.swbank.kr/rnd/swResultRegist.do) 절차 관련 확인
3) 첨가물 app을 가급적이면 별도의 app으로 개발했으면 좋겠음 (연구결과 성과 등록 관련..)
4) 미국 fda drug list 관련 db https://www.fda.gov/drugs/drug-approvals-and-databases/national-drug-code-directory)
5) additives list 들어있는 주소: https://www.fda.gov/drugs/drug-approvals-and-databases/inactive-ingredients-database-download 근데 어떤 약제에 어떤 첨가물이 들어가 있는지 나와있지는 않네?
6) 김미혜 교수님 contact 관련 문의
7) 김미혜 교수님 헝 박사님 OCR 관련 기술 사용 가능할지 확인
8) 홍대 미대 학생과 조인해서 UX/UI 디자인 - 약물 app 기능 설계
9) 부작용 DB 자연어 차리가 가능할지 확인
10) MedDRA 데이터베이스를 받을 수 있는지? 확인
11) SIDER 4.1 database 구조 둘러보기

2020-11-03

1) MeDDRA 한국어 version download -> postgresql import done
2) SIDER 4.1 version download -> postgresql import done
3) 'Network analysis of drug side effects and indication' 논문 읽어보기  http://studentsrepo.um.edu.my/9478/6/Yousoff_Effendy_Mohd_Ali_-_Thesis.pdf
4) biz.kpis.or.kr 데이터 import하기
5) 건강보험급여되는 약제 pattern 처리후 파일 import 하기
6) 미국 UMLS database import하기
7) 미국 FAERS database import: https://github.com/ltscomputingllc/faersdbstats , https://www.nature.com/articles/sdata201626

김대식 선생님
1) 첨가물 DB 작업 success : 약 15000개, fail: 10000개 (첫번째 숫자가 0인 경우 숫자형으로 변환되면 오류!! -> 수정 예정) 

- '약제급여목록및급여상한금액표(2020.7.1.)(25,608)_6.30.수정.xlsx' 파일로부터 추출한 의약품표준코드가 opendata.go.kr 사이트에서 'MdcinPrductPrmisnInfoService/getMdcinPrductItem'에서 'Barcode'를 서비스 키로 자료를 요청했을 때 ping 값이 없는 값이 약 10000개 정도 됨. 
- 데이터를 들여다보면 'MdcinPrductPrmisnInfoService/getMdcinPrductItem' 오퍼레이션에는 'ITEM_SEQ', 'BAR_CODE', 'EDI_CODE' 이렇게 세가지 코드값이 있음. 
- 이중에서 '약제급여목록및급여상한금액표(2020.7.1.)(25,608)_6.30.수정.xlsx' 파일에는 'EDI_CODE' 변수값만 있고, 'BarCodeData_202010.txt' 파일에는 '품목기준코드', '전문/일반	대표코드', '표준코드', '제품코드(개정후)' 값이 있음. 
- 오퍼레이션의 'ITEM_SEQ' = '품목기준코드', 'BAR_CODE' = '표준코드', 'EDI_Code' = '제품코드(개정후)' 로 매핑됨

2020-11-09

1) 이전 만들었던 python 코드를 수정해서 다음의 내용을 수행할 수 있도록 해주세요. 

- 'data' 폴더의 'BarCodeData_202010.txt' 파일의 '품목기준코드'를 기준으로 'MdcinPrductPrmisnInfoService/getMdcinPrductItem' 오퍼레이션 데이터를 저장했으면 좋겠습니다.
- 파싱한 파일 자체를 다음의 규칙으로 naming : '품목기준코드_한글상품명_업체명_약품규격.xmls' 
-- 단 '한글상품명'은 정규표현식 처리를 해서 '한글상품명' 필드값 중에서 첫번째 '('가 나오기 전까지 값을 추출해서 xlms 파일 naming에 사용
- 추출가능한 모든 값을 저장 (밑의 변수를 대상으로 해주세요)

    ITEM_SEQ
    ITEM_NAME
    ENTP_NAME
    ITEM_PERMIT_DATE
    CNSGN_MANUF
    ETC_OTC_OCDE
    CLASS_NO
    CHART
    BAR_CODE
    MATERIAL_NAME
    EE_DOC_ID
    UD_DOC_ID
    NB_DOC_ID
    INSERT_FILE
    STORAGE_METHOD
    VALID_TERM
    REEXAM_TARGET
    REEXAM_DATE
    PACK_UNIT
    EDI_CODE
    DOC_TEXT
    PERMIT_KIND_NAME
    ENTP_NO
    MAKE_MATERIAL_FLAG
    NEWDRUG_CLASS_NAME
    INDUTY_TYPE
    CANCEL_DATE
    CANCEL_NAME
    CHANGE_DATE
    NARCOTIC_KIND_CODE
    GBN_NAME
    EE_DOC_DATA
    UD_DOC_DATA
    NB_DOC_DATA
    PN_DOC_DATA
    MAIN_ITEM_INGR
    INGR_NAME

-- EE_DOC_DATA, UD_DOC_DATA, NB_DOC_DATA, PN_DOC_DATA에는 긴 text 값을 우선 저장하고, 다음과 같이 각각 변수를 분리.
--- EE_DOC_DATA: 예를들면 'ARTICLE title=' 뒷부분, '<![CDATA[ '  뒷부분 값을 파싱. 각각 여러 값일 수 있음. '<![CDATA[ 류마티스관절염, 강직척추염, 골관절염(퇴행관절염) 및 견갑상완골의 관절주위염, 치통, 외상 후 생기는 염증, 요통, 좌골통, 비관절성 류머티즘으로 인한 통증 ]]>' 이부분 중에서 '류마티스관절염' 부터 '통증' 부분까지 잡아내면 됨. 해당 파트가 여러개일 수 있으나 모두 한 필드에 저장
--- US_DOC_DATA: EE_DOC_DATA와 동일하게 처리
--- NB_DOC_DATA: 복잡함. '1.  경고', 	'2. 다음 환자(경우)에는 투여하지 말 것.', '3. 다음 환자에는 신중히 투여할 것.', 	'4. 이상반응'. '5. 일반적 주의'. '6. 상호작용', '7. 임부 및 수유부에 대한 투여', '8. 소아에 대한 투여', '9. 고령자에 대한 투여', '10. 과량투여 시의 처치', '11. 보관 및 취급상의 주의사항', '10. 기타' 등이 있음. 각각의 값들은 '<ARTICLE title="1. 다음 환자에게는 투여하지 말 것">'처럼 되어 있는데, 'ARTICLE title='으로 잡은 다음에 '1. '같은 숫자 부분은 제외하고, 다음 값들을 별도의 변수명으로 잡아서, 하위에 해당하는 갑들 중 '<!CDATA[ ' 뒷부분을 각각 있는만큼 추출. 각 변수들은 'NB_DOC_DATA_(경고)', 'NB_DOC_DATA_(다음 환자(경우)에는 투여하지 말 것' 등으로 명명. 
 
2) 데이터 저장 공간 등이 문제가 될 것 같으면, 
  
- IP: 221.160.191.58
- PORT: 3389
- ID: mingyu, PW: lemonpa2 또는 ID: kdy, PW: kdykdy
- DBeaver나 PgAdmin으로 접속
- DB_name = 'drug_db' 등에서 작업을 해도 됩니다. 아마 접속 PW: postgre 일겁니다. 

https://biz.kpis.or.kr/kpis_biz/index.jsp

** 파일 이메일 보내기 / git push 확인하기
** UI는 홍대 교수님 / 학생 연계할 수 있는 방법 상의
** Smart_DUR app 화면 display 중 한가지 변경 요청
** 사용자 역할: 최고관리자/의사/환자 (보호자?용이 의미가 있을지는 물어봐서 결정)
## 개원의사용 인터페이스는 어떻게 하면 편할지? 별도의 페이지를 구성하는게 좋을지? 인증에 대한 부분이 있을텐데? 어떤식으로 접근하는게 좋을지?
## QR 코드 또는 JSON 등으로 파일 import, export할 수 있는지?

## OCR 관련 회사 / 김미혜 교수님 확인

##
## 금기약제에 해당할 경우, 유사 성분 중 첨가물 정보가 없는 
