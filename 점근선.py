import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# 페이지 기본 설정
st.set_page_config(page_title="유리함수 점근선 교과서", page_icon="📘", layout="wide")

st.title("📘 유리함수의 점근선 학습 앱")
st.markdown("유리함수의 **수직/수평/비스듬한 점근선**을 배워보고 직접 그래프를 확인해보세요!")

# 탭 구성
tab1, tab2, tab3 = st.tabs(["📖 이론 학습", "🧩 예제 풀이", "📈 그래프 시각화"])

# -----------------------------------------------------
# 1️⃣ 이론 학습 탭
# -----------------------------------------------------
with tab1:
    st.header("1️⃣ 유리함수의 개념")
    st.markdown(r"""
    유리함수란 **두 다항식의 나눗셈으로 이루어진 함수**입니다.

    \[
    f(x) = \frac{P(x)}{Q(x)}, \quad Q(x) \neq 0
    \]
    """)

    st.header("2️⃣ 점근선의 종류")
    st.markdown("""
    | 종류 | 형태 | 구하는 방법 |
    |------|------|-------------|
    | 수직 점근선 | x = a | 분모 = 0 (단, 분자 ≠ 0) |
    | 수평 점근선 | y = b | 차수 비교 후 계수비 계산 |
    | 비스듬한 점근선 | y = ax + b | 분자 차수 = 분모 차수 + 1 → 다항식 나눗셈 |
    """)

    st.header("3️⃣ 차수 비교에 따른 수평 점근선 정리")
    st.markdown("""
    | 분자의 차수 | 분모의 차수 | 수평 점근선 |
    |--------------|--------------|--------------|
    | 작다 | 크다 | y = 0 |
    | 같다 | 같다 | y = 계수비 |
    | 크다 | 작다 | 없음 (대신 비스듬한 점근선 가능) |
    """)

    st.info("💡 핵심 정리: 수직은 분모=0, 수평은 차수 비교, 비스듬한은 다항식 나눗셈!")

# -----------------------------------------------------
# 2️⃣ 예제 풀이 탭
# -----------------------------------------------------
with tab2:
    st.header("🧩 예제 풀이")

    example = st.selectbox("예제를 선택하세요", [
        "예제 1: f(x) = (x^2 + 1)/(x - 2)",
        "예제 2: f(x) = (x^2 + 1)/(x^2 + 3)",
        "예제 3: f(x) = (2x)/(x^2 + 1)"
    ])

    x = sp.Symbol('x')

    if "예제 1" in example:
        f = (x**2 + 1)/(x - 2)
    elif "예제 2" in example:
        f = (x**2 + 1)/(x**2 + 3)
    else:
        f = (2*x)/(x**2 + 1)

    st.latex(f"f(x) = {sp.latex(f)}")

    numer, denom = sp.fraction(sp.simplify(f))
    deg_num = sp.degree(numer)
    deg_den = sp.degree(denom)

    # 수직 점근선
    vertical = [v for v in sp.solve(denom, x) if numer.subs(x, v) != 0]

    # 수평 점근선
    if deg_num < deg_den:
        horizontal = 0
    elif deg_num == deg_den:
        horizontal = sp.LC(numer) / sp.LC(denom)
    else:
        horizontal = None

    # 비스듬한 점근선
    oblique = None
    if deg_num == deg_den + 1:
        oblique, _ = sp.div(numer, denom)

    st.subheader("🔹 점근선 결과")
    st.write("**수직 점근선:**", [f"x = {v}" for v in vertical] if vertical else "없음")
    st.write("**수평 점근선:**", f"y = {horizontal}" if horizontal is not None else "없음")
    st.write("**비스듬한 점근선:**", f"y = {sp.simplify(oblique)}" if oblique is not None else "없음")

# -----------------------------------------------------
# 3️⃣ 그래프 시각화 탭
# -----------------------------------------------------
with tab3:
    st.header("📈 그래프로 확인하기")

    expr_str = st.text_input("유리함수를 입력하세요 (예: (x**2+1)/(x-2))", "(x**2+1)/(x-2)")
    try:
        f = sp.sympify(expr_str)
        x = sp.Symbol('x')

        # 점근선 계산
        numer, denom = sp.fraction(sp.simplify(f))
        vertical = [v for v in sp.solve(denom, x) if numer.subs(x, v) != 0]
        deg_num = sp.degree(numer)
        deg_den = sp.degree(denom)

        if deg_num < deg_den:
            horizontal = 0
        elif deg_num == deg_den:
            horizontal = sp.LC(numer) / sp.LC(denom)
        else:
            horizontal = None

        oblique = None
        if deg_num == deg_den + 1:
            oblique, _ = sp.div(numer, denom)

        # 그래프 데이터 생성
        fx = sp.lambdify(x, f, "numpy")
        X = np.linspace(-10, 10, 1000)
        Y = fx(X)

        fig, ax = plt.subplots(figsize=(7, 5))
        ax.plot(X, Y, label="f(x)", color="blue")

        # 점근선 표시
        for v in vertical:
            ax.axvline(v, color="red", linestyle="--", label=f"x = {v}")
        if horizontal is not None:
            ax.axhline(float(horizontal), color="green", linestyle="--", label=f"y = {horizontal}")
        if oblique is not None:
            oblique_func = sp.lambdify(x, oblique, "numpy")
            ax.plot(X, oblique_func(X), color="orange", linestyle="--", label=f"y = {sp.simplify(oblique)}")

        ax.set_ylim(-10, 10)
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)

    except Exception as e:
        st.error(f"식이 잘못되었습니다: {e}")
