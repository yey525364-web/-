import streamlit as st
import random
import time

# 앱 제목
st.title("🎰 로또 번호 추첨기")

st.write("1부터 45까지의 숫자 중 6개를 무작위로 뽑아요! 🎱")

# 게임 수 입력 (1~10)
game_count = st.number_input("생성할 게임 수를 입력하세요 (1~10)", 
                             min_value=1, max_value=10, value=1, step=1)

# 번호별 색상 구분 (시각적 재미)
def get_ball_color(number):
    if number <= 10:
        return "#f94144"  # 빨강
    elif number <= 20:
        return "#f3722c"  # 주황
    elif number <= 30:
        return "#f9c74f"  # 노랑
    elif number <= 40:
        return "#43aa8b"  # 초록
    else:
        return "#577590"  # 파랑

# 공 스타일 HTML
def render_ball(number):
    color = get_ball_color(number)
    return f"""
    <div style='
        display:inline-flex;
        justify-content:center;
        align-items:center;
        width:55px; height:55px;
        border-radius:50%;
        background-color:{color};
        color:white;
        font-size:22px;
        font-weight:bold;
        margin:5px;
        box-shadow:2px 2px 6px rgba(0,0,0,0.3);
    '>{number}</div>
    """

# 생성 버튼 클릭 시
if st.button("🎲 번호 생성"):
    st.subheader(f"총 {game_count}개의 로또 조합 🎟️")

    for i in range(int(game_count)):
        numbers = sorted(random.sample(range(1, 46), 6))

        st.markdown(f"### 🏷️ 게임 {i+1}")
        placeholder = st.empty()

        # 하나씩 공이 뽑히는 효과
        drawn_balls = ""
        for n in numbers:
            drawn_balls += render_ball(n)
            placeholder.markdown(drawn_balls, unsafe_allow_html=True)
            time.sleep(0.4)  # 공이 하나씩 등장하는 시간 간격

        st.markdown("<hr>", unsafe_allow_html=True)
