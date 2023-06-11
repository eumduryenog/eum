import streamlit as st
import streamlit as st
import subprocess

# 애플리케이션 제목
st.title("경기과기대 201821018 음두령")

# 페이지 제목
st.header("제어공학 기말고사")
# 페이지 소제목
st.subheader("2번 문제")

# 외부 파이썬 스크립트 실행
result = subprocess.run(['201821018_eum.py'], capture_output=True, text=True)

# 실행 결과 출력
st.write(result.stdout)