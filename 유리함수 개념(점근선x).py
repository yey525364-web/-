import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 배경색 CSS 적용 (딸기우유색)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFD1DC;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("유리함수 개념")

# 1️⃣ 정의
st.header("유리함수의 정의")
st.write("""
유리함수는 두 다항식의 비로 정의되는 함수입니다.

$$ f(x) = \\frac{P(x)}{Q(x)} $$

여기서 P(x), Q(x)는 다항식이고, Q(x) ≠ 0 입니다.
""")

# 2️⃣ 성질
st.header("유리함수의 성질")
st.write("""
- 정의역: 분모가 0이 아닌 모든 실수  
- 그래프에는 수직, 수평, 사선 점근선이 나타날 수 있음  
- 분자의 차수와 분모의 차수에 따라 점근선이 달라집니다
""")

# 3️⃣ 기본형 그래프
st.header("유리함수 기본형 그래프 예시")

x = np.linspace(-10, 10, 400)

# 예시 1: f(x) = 1/x
x1 = x[x != 0]  # x=0 제외
y1 = 1 / x1
plt.figure(figsize=(6,4))
plt.plot(x1, y1, label='f(x) = 1/x')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title("f(x) = 1/x")
plt.grid(True)
plt.legend()
st.pyplot(plt)

# 예시 2: f(x) = (x+1)/(x-1)
x2 = x[x != 1]  # 분모 0 제외
y2 = (x2 + 1)/(x2 - 1)
plt.figure(figsize=(6,4))
plt.plot(x2, y2, label='f(x) = (x+1)/(x-1)')
plt.axhline(1, color='green', linestyle='--', label='y=1 (수평점근선)')
plt.axvline(1, color='red', linestyle='--', label='x=1 (수직점근선)')
plt.title("f(x) = (x+1)/(x-1)")
plt.grid(True)
plt.legend()
st.pyplot(plt)
