import streamlit as st
import pandas as pd
import time

st.title('허온의 여름방학 계획표 :beach_with_umbrella:')
st.write(pd.DataFrame({
    '계획': ['직원 업무 관리 프로젝트 완료하기', '파이썬 공부하기', 'JS 공부하기', '웹페이지 클론코딩하기', '필리핀 세부 가족여행가기', '알고리즘 자료구조 공부하기'],
    '상태': ['진행중', '진행전', '진행전', '진행전', '진행전', '진행중'],
}))

str = "이번에 화면구현 대회를 하면서 개발하게 되었던 직원업무관리 프로그램에 직원페이지를 개발할것이다. 이번 대회에서는 사장님페이지를 개발하였는데 이번 방학때 직원페이지를 개발하여 빠른 시간내에 개발을 완료하여 사용할수있도록 할것이다.github의 pages를 사용하여 웹사이트를 배포하였지만 pages는 html,css,js등 간단한 웹사이트만 구동이되고 내가 개발하면서 사용한 php서버는 작동되지 않는다. 그리고 데이터 베이스와 연결도 되지않아 데이터를 불러올수도 없다. 따라서 이번 방학때 곽상미 선생님께서 추천해주신 firebase를 조금 배워 php와 DB를 연동하여 실제로 사용할수있도록 배포 할것이다.위에 내용을 공부 및 개발하면서 velog에 글을 쓰는것 처럼 이 노션에 기록할것이다.그리고 이 프로젝트는 방학이 끝난후로도 누나의 의견을 받으며 기능을 추가하고 수정하면서 전국의 사장님 모두가 사용할수 있는 웹사이트로 발전시킬것이다."

def stream_data():
    for word in str.split(" "):
        yield word + " "
        time.sleep(0.02)
    st.write('노션링크 : https://www.notion.so/afb64411ed7145569d5c7f6ddf422a1f?pvs=4')
    st.write('피그마링크 : https://www.figma.com/design/yDhzeGblwHHsy9RENnQSsa/%EC%A7%81%EC%9B%90-%EC%97%85%EB%AC%B4-%EA%B4%80%EB%A6%AC-%ED%8E%98%EC%9D%B4%EC%A7%80-%EB%94%94%EC%9E%90%EC%9D%B8-%EC%88%98%EC%A0%95?node-id=0-1&t=PKHy9Jo6WqkqTr0F-1')
    #st.write('')

if st.button("직원 업무 관리 프로젝트 완료하기 계획	:earth_africa:"):
    st.write_stream(stream_data)
