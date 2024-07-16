import streamlit as st
# firebase연결
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import json

key_dict = json.loads(st.secrets["textkey"])
cred = credentials.Certificate(key_dict)

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://campweb-84246-default-rtdb.firebaseio.com/'
    })


if 'total' not in st.session_state:
    st.session_state.total = 0
if 'id' not in st.session_state:
    st.session_state.id = 'NULL'
if 'name' not in st.session_state:
    st.session_state.name = 'NULL'

st.title('허온의 퀴즈쇼 :basketball:')

def food_check(food):
    if food == '뿌링클 콤보 닭다리 허벅지 부분':
        st.write('정답입니다!')
        st.session_state.total += 60
    else:
        st.write('오답입니다!')
        st.write('정답은 : 뿌링클 콤보 닭다리 허벅지 부분 이였습니다.')

def hate(plot_type):
    if plot_type == "세진이와 비슷하게 생긴 바퀴벌레":
        st.write('정답입니다!')
        st.session_state.total += 40
    else:
        st.write('오답입니다!')
        st.write('정답은 세진이와 비슷하게 생긴 바퀴벌레 였습니다.')

def quiz():
    st.header('첫번째 문제 : 주관식 (60점)')
    food = st.text_input('허온이 가장 좋아하는 음식은 ?')
    if st.button("제출"):
        food_check(food)

    st.header('두번째 문제 : 객관식 (40점)')
    plot_type = st.radio(
        "허온이 가장 싫어하는 것을 고르시오",
        ("세진이와 비슷하게 생긴 바퀴벌레", "매일 허온에게 피파를 지는 허세진", "시도때도 없이 나오는 날파리", "방에서 계속 노래부르는 김현호", "html과 같이 근본없는 언어")
    )
    if st.button("확인"):
        hate(plot_type)

ref_id = db.reference('users/user/id')
ref_name = db.reference('users/user/name')
st.header('로그인')
st.session_state.id = st.text_input('학번')
st.session_state.name = st.text_input('이름')
if st.button("확인", key=1):
    if int(st.session_state.id) == ref_id.get() and st.session_state.name == ref_name.get():
        quiz()
    else:
        st.header('학번 이름이 잘못되었습니다.')