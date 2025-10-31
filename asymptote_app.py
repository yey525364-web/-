import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

st.title("유리함수 점근선 계산기")

st.write("유리함수 f(x) = (분자)/(분모)의 수직/수평/사선 점근선을 계산합니다.")

# 사용자 입력
numerator = st.text_input("분자 입력 (예: x**2 + 1)", "x**2 + 1")
denominator = st.text_input("분모 입력 (예: x - 2)", "x - 2")

x = sp.Symbol('x')

try:
    num_expr = sp.sympify(numerator)
    den_expr = sp.sympify(denominator)
    f = num_expr / den_expr

    # 수직 점근선: 분모=0
    vertical_asymptotes = sp.solve(sp.denom(f), x)
    st.write("### 수직 점근선")
    if vertical_asymptotes:
        st.write(vertical_asymptotes)
    else:
        st.write("없음")

    # 수평/사선 점근선
    deg_num = sp.degree(num_expr)
    deg_den = sp.degree(den_expr)
    
    st.write("### 수평/사선 점근선")
    if deg_num < deg_den:
        st.write("y = 0 (수평점근선)")
    elif deg_num == deg_den:
        ratio = sp.LC(num_expr)/sp.LC(den_expr)
        st.write(f"y = {ratio} (수평점근선)")
    elif deg_num == deg_den + 1:
        quotient = sp.div(num_expr, den_expr)[0]
        st.write(f"y = {quotient} (사선점근선)")
    else:
        st.write("차수가 분모보다 2 이상 크면 사선 점근선 없음")

    # 그래프
    st.write("### 함수 그래프")
    f_lambdified = sp.lambdify(x, f, 'numpy')
    x_vals = np.linspace(-10, 10, 400)
    y_vals = f_lambdified(x_vals)

    plt.figure(figsize=(8,4))
    plt.plot(x_vals, y_vals, label='f(x)')
    plt.axhline(0, color='black', linewidth=0.5)
    for va in vertical_asymptotes:
        plt.axvline(float(va), color='red', linestyle='--', label=f'x={va}')
    plt.ylim(-10,10)
    plt.legend()
    st.pyplot(plt)
    
except Exception as e:
    st.write("오류 발생:", e)
