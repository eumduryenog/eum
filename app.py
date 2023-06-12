import streamlit as st
import streamlit as st
import pandas as pd
import nbformat
import subprocess

from nbconvert import PythonExporter

# 애플리케이션 제목
st.title("경기과기대 201821018 음두령")

# 페이지 제목
st.header("제어공학 기말고사")
# 페이지 소제목
st.subheader("2번 문제")

# 201821018_eum.ipynb 파일을 Python 코드로 변환
notebook_file = '201821018_eum.ipynb'
exporter = PythonExporter()
code, _ = exporter.from_filename(notebook_file)

# streamlit 애플리케이션 실행
st.code(code, language='python')