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
