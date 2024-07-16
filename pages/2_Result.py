import streamlit as st

st.title('허온의 퀴즈쇼 :basketball:')

st.write(f'{st.session_state.name}님')
st.write(f'지금 현재 점수는 : {st.session_state.total}')