import streamlit as st
import random

st.title("🎰 로또 번호 생성기")

st.write("대한민국 로또: 1부터 45까지의 숫자 중 6개를 무작위로 뽑아요!")

# 게임 수 입력 (1~10)
game_count = st.number_input("생성할 게임 수를 입력하세요 (1~10)", min_value=1, max_value=10, value=1, step=1)

# 생성 버튼
if st.button("🎲 번호 생성"):
    st.subheader(f"총 {game_count}개의 로또 번호 조합")
    
    for i in range(int(game_count)):
        numbers = sorted(random.sample(range(1, 46), 6))
        st.write(f"**게임 {i+1}:** 🎟️ {', '.join(map(str, numbers))}")
