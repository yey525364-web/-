import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# 배경색: 연한 핑크 (#FFD1DC)
st.markdown(
    """
    <style>
    .stApp {
        background: #FFD1DC;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("유리함수 개념과 점근선 계산")

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

x_vals = np.linspace(-10,10,400)

# 예시 1: f(x) = 1/x
x1 = x_vals[x_vals != 0]
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
x2 = x_vals[x_vals != 1]
y2 = (x2 + 1)/(x2 - 1)
plt.figure(figsize=(6,4))
plt.plot(x2, y2, label='f(x) = (x+1)/(x-1)')
plt.axhline(1, color='green', linestyle='--', label='y=1 (수평점근선)')
plt.axvline(1, color='red', linestyle='--', label='x=1 (수직점근선)')
plt.title("f(x) = (x+1)/(x-1)")
plt.grid(True)
plt.legend()
st.pyplot(plt)

# 4️⃣ 사용자 입력으로 점근선 계산
st.header("점근선 계산기")
st.write("유리함수 f(x) = 분자 / 분모 형태를 입력하면 점근선을 계산합니다.")

numerator = st.text_input("분자 입력 (예: x**2 + 1)", "x**2 + 1")
denominator = st.text_input("분모 입력 (예: x - 2)", "x - 2")

x = sp.Symbol('x')

try:
    num_expr = sp.sympify(numerator)
    den_expr = sp.sympify(denominator)
    f = num_expr / den_expr

    # 수직 점근선
    vertical = sp.solve(sp.denom(f), x)
    st.subheader("수직 점근선")
    if vertical:
        st.write(vertical)
    else:
        st.write("없음")

    # 수평/사선 점근선
    deg_num = sp.degree(num_expr)
    deg_den = sp.degree(den_expr)
    st.subheader("수평/사선 점근선")
    if deg_num < deg_den:
        st.write("y = 0 (수평점근선)")
    elif deg_num == deg_den:
        ratio = sp.LC(num_expr)/sp.LC(den_expr)
        st.write(f"y = {ratio} (수평점근선)")
    elif deg_num == deg_den + 1:
        quotient = sp.div(num_expr, den_expr)[0]
        st.write(f"y = {quotient} (사선점근선)")
    else:
        st.write("차수가 분모보다 2 이상 크면 사선점근선 없음")

    # 그래프
    st.subheader("사용자 함수 그래프")
    f_lambdified = sp.lambdify(x, f, 'numpy')
    x_vals_graph = np.linspace(-10,10,400)
    # 수직점근선 근처 값 제거
    for v in vertical:
        x_vals_graph = x_vals_graph[x_vals_graph != float(v)]
    y_vals_graph = f_lambdified(x_vals_graph)

    plt.figure(figsize=(6,4))
    plt.plot(x_vals_graph, y_vals_graph, label='f(x)')
    plt.axhline(0, color='black', linewidth=0.5)
    for va in vertical:
        plt.axvline(float(va), color='red', linestyle='--', label=f'x={va}')
    plt.ylim(-10,10)
    plt.title("사용자 함수 그래프")
    plt.grid(True)
    plt.legend()
    st.pyplot(plt)

except Exception as e:
    st.error(f"오류 발생: {e}")
