import streamlit as st
import streamlit as st
import pandas as pd
import subprocess

# 애플리케이션 제목
st.title("경기과기대 201821018 음두령")

# 페이지 제목
st.header("제어공학 기말고사")
# 페이지 소제목
st.subheader("2번 문제")

# 파일 업로드 위젯
uploaded_file = st.file_uploader("파일을 업로드하세요.", type="ipynb")

if uploaded_file is not None:
    # 업로드된 파일을 로컬에 저장
    with open("uploaded.ipynb", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.write("파일이 성공적으로 업로드되었습니다.")

# 날짜 선택
date = st.date_input("날짜 선택")

# 시간 선택
time = st.time_input("시간 선택")