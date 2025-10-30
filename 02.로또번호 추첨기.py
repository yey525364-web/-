import streamlit as st
import random
import time

st.set_page_config(page_title="로또 번호 추첨기", page_icon="🎱", layout="centered")

st.title("🎰 로또 번호 추첨기")
st.write("1부터 45까지의 숫자 중 6개를 무작위로 뽑아요! 🎱")

# 게임 수 입력
game_count = st.number_input("생성할 게임 수를 입력하세요 (1~10)", 
                             min_value=1, max_value=10, value=1, step=1)

# 속도 슬라이더
speed = st.slider("공이 나오는 속도 (초)", 0.3, 2.0, 1.0, 0.1)

# 색상 구분
def get_ball_color(number):
    if number <= 10:
        return "#f94144"
    elif number <= 20:
        return "#f3722c"
    elif number <= 30:
        return "#f9c74f"
    elif number <= 40:
        return "#43aa8b"
    else:
        return "#577590"

# 공 CSS (굴러나오는 효과)
BALL_STYLE = """
<style>
@keyframes rollIn {
  0% { transform: translateX(-100px) rotate(-720deg); opacity: 0; }
  80% { opacity: 1; }
  100% { transform: translateX(0) rotate(0deg); opacity: 1; }
}
.ball {
  display: inline-flex;
  justify-content: center;
  align-items: center;
  width: 55px;
  height: 55px;
  border-radius: 50%;
  color: white;
  font-size: 22px;
  font-weight: bold;
  margin: 5px;
  box-shadow: 2px 2px 6px rgba(0,0,0,0.3);
  animation: rollIn 0.8s ease-out;
}
</style>
"""
st.markdown(BALL_STYLE, unsafe_allow_html=True)

# 공 생성 함수
def render_ball(number):
    color = get_ball_color(number)
    return f"<div class='ball' style='background-color:{color};'>{number}</div>"

# 생성 버튼
if st.button("🎲 번호 생성"):
    st.subheader(f"총 {game_count}개의 로또 조합 🎟️")

    for i in range(int(game_count)):
        numbers = sorted(random.sample(range(1, 46), 6))

        st.markdown(f"### 🏷️ 게임 {i+1}")
        placeholder = st.empty()

        drawn_balls = ""
        for n in numbers:
            drawn_balls += render_ball(n)
            placeholder.markdown(drawn_balls, unsafe_allow_html=True)
            time.sleep(speed)  # 속도 조절 (느리게 뽑히는 느낌)

        st.markdown("<hr>", unsafe_allow_html=True)
