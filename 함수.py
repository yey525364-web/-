import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="이차함수 그래프 학습", page_icon="📈", layout="wide")

st.title("📘 이차함수의 표준형 y = a(x - p)² + q 학습 앱")

st.write("""
이 앱은 이차함수의 표준형 그래프가 **p**와 **q** 값에 따라 어떻게 이동하는지 시각적으로 학습하도록 도와줍니다.
""")

# -------------------------
# 1단계: p 변화 관찰
# -------------------------
st.header("1️⃣ y = a(x - p)² 에서 p 변화에 따른 그래프 이동")

a = st.slider("a 값 (그래프의 모양)", -3.0, 3.0, 1.0, 0.5)
p = st.slider("p 값 (x축 방향 이동)", -5.0, 5.0, 0.0, 0.5)

x = np.linspace(-10, 10, 400)
y1 = a * (x ** 2)
y2 = a * (x - p) ** 2

fig, ax = plt.subplots()
ax.plot(x, y1, label="y = a·x²", linestyle="--", color="gray")
ax.plot(x, y2, label=f"y = {a}(x - {p})²", color="orange")
ax.axhline(0, color="black", linewidth=1)
ax.axvline(0, color="black", linewidth=1)
ax.legend()
ax.grid(True)
st.pyplot(fig)

st.info("👉 p의 값이 바뀔수록 그래프가 **x축 방향으로 p만큼 평행이동**함을 확인하세요!")

# -------------------------
# 2단계: q 변화 관찰
# -------------------------
st.header("2️⃣ y = a·x² + q 에서 q 변화에 따른 그래프 이동")

q = st.slider("q 값 (y축 방향 이동)", -5.0, 5.0, 0.0, 0.5)

y3 = a * (x ** 2) + q

fig2, ax2 = plt.subplots()
ax2.plot(x, a * (x ** 2), label="y = a·x²", linestyle="--", color="gray")
ax2.plot(x, y3, label=f"y = {a}x² + {q}", color="green")
ax2.axhline(0, color="black", linewidth=1)
ax2.axvline(0, color="black", linewidth=1)
ax2.legend()
ax2.grid(True)
st.pyplot(fig2)

st.info("👉 q의 값이 바뀔수록 그래프가 **y축 방향으로 q만큼 평행이동**함을 확인하세요!")

# -------------------------
# 3단계: p, q 동시 조절
# -------------------------
st.header("3️⃣ y = a(x - p)² + q 에서 p, q 동시 변화 관찰")

col1, col2 = st.columns(2)
with col1:
    p2 = st.slider("p (x축 이동)", -5.0, 5.0, 0.0, 0.5, key="p2")
with col2:
    q2 = st.slider("q (y축 이동)", -5.0, 5.0, 0.0, 0.5, key="q2")

y4 = a * (x - p2) ** 2 + q2

fig3, ax3 = plt.subplots()
ax3.plot(x, a * (x ** 2), label="y = a·x²", linestyle="--", color="gray")
ax3.plot(x, y4, label=f"y = {a}(x - {p2})² + {q2}", color="red")
ax3.axhline(0, color="black", linewidth=1)
ax3.axvline(0, color="black", linewidth=1)
ax3.legend()
ax3.grid(True)
st.pyplot(fig3)

st.success("✅ p, q를 함께 바꿔보세요. 그래프가 x축과 y축 방향으로 동시에 평행이동함을 확인할 수 있습니다!")

# -------------------------
# 4단계: 간단한 퀴즈
# -------------------------
st.header("🧠 개념 확인 퀴즈")

quiz = st.radio(
    "Q1. y = 2(x - 3)² + 4 의 그래프는 y = 2x² 그래프를 어떻게 이동한 것일까요?",
    (
        "① 오른쪽으로 3, 위로 4 이동",
        "② 왼쪽으로 3, 위로 4 이동",
        "③ 오른쪽으로 3, 아래로 4 이동",
        "④ 왼쪽으로 3, 아래로 4 이동",
    )
)

if st.button("정답 확인"):
    if quiz == "① 오른쪽으로 3, 위로 4 이동":
        st.success("🎉 정답입니다! p=3 → 오른쪽 3, q=4 → 위로 4 이동이에요.")
    else:
        st.error("❌ 오답입니다. p=3이면 오른쪽으로, q=4이면 위쪽으로 이동합니다!")

st.markdown("---")
st.caption("💡 제작: ChatGPT 학습 도우미 — 이차함수의 이동 개념 시각화")
