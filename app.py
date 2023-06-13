import streamlit as st
import os.path

# 애플리케이션 제목
st.title("경기과기대 201821018 음두령")

# 페이지 제목
st.header("제어공학 기말고사")
# 페이지 소제목
st.subheader("2번 문제")
'''
from nbconvert import PythonExporter

# 201821018_eum.ipynb 파일을 Python 코드로 변환
notebook_file = '201821018_eum.ipynb'

if os.path.isfile(notebook_file):
    exporter = PythonExporter()
    code, _ = exporter.from_filename(notebook_file)

    # streamlit 애플리케이션 실행
    st.code(code, language='python')
else:
    st.error("Notebook file not found.")
'''

import sympy

s = sympy.symbols('s')

G1 = 100/((s+2)*(s+3))

G4 = G1/(1+G1)

print(G4)
     
100/((1 + 100/((s + 2)*(s + 3)))*(s + 2)*(s + 3))

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

num = [100]
den = [1, 5, 6]  # (s+2)(s+3)의 계수

sys = signal.TransferFunction(num, den)  # 시스템 전달함수

t, y = signal.step(sys)  # unit step 입력에 대한 응답

plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Output')
plt.grid()
plt.show()
     


import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

G0 = signal.lti([100], [1])
G1 = signal.lti([1], [1, 2])
G2 = signal.lti([1], [1, 3])
G3 = signal.lti([100], [1, 3, 2])

frequencies = np.logspace(-2, 2, 500)

systems = [G0, G1, G2, G3]
labels = ['Proportional Element', 'Integral Element', 'First-Order Lag Element', 'Overall System']
colors = ['r', 'g', 'b', 'm']

plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
for sys, label, color in zip(systems, labels, colors):
    _, mag, _ = sys.bode(w=frequencies)
    plt.semilogx(frequencies, mag, color=color, label=label)
plt.title('Bode plot')
plt.ylabel('Magnitude [dB]')
plt.legend()

plt.subplot(2, 1, 2)
for sys, label, color in zip(systems, labels, colors):
    _, _, phase = sys.bode(w=frequencies)
    plt.semilogx(frequencies, phase, color=color)
plt.ylabel('Phase [degrees]')
plt.xlabel('Frequency [Hz]')

plt.show()
     
