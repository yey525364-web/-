import streamlit as st
import random

# 앱 제목
st.title("🎨 캐릭터 생성기")

st.write("버튼을 눌러 무작위 캐릭터 조합을 생성해보세요!")

# 캐릭터 요소 정의
genders = ["여자", "남자"]
hair_lengths = ["장발", "단발", "숏컷"]
face_types = ["고양이상", "강아지상", "여우상", "늑대상"]
ages = ["아동기", "청소년기", "청년기", "중년기", "노년기"]

# 게임 수 입력 (1~5)
game_count = st.number_input("생성할 캐릭터 수를 입력하세요 (1~5)", 
                             min_value=1, max_value=5, value=1, step=1)

# 생성 버튼
if st.button("🎲 캐릭터 생성"):
    st.subheader(f"총 {game_count}개의 캐릭터 조합")

    for i in range(int(game_count)):
        gender = random.choice(genders)
        hair = random.choice(hair_lengths)
        face = random.choice(face_types)
        age = random.choice(ages)

        st.markdown(f"""
        **캐릭터 {i+1}**
        - 성별: {gender}  
        - 머리카락 길이: {hair}  
        - 얼굴상: {face}  
        - 나이: {age}
        """)

