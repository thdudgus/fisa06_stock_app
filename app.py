import streamlit as st

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

# text input을 활용해서 검색창을 만든다.
# 이 검색창에 ani_list 단어 일부가 일치하면 img_list의 해당 이미지를 출력하는 로직을 만들어주세요.
# if / for 활용

st.title('검색창')

user_input = st.chat_input(placeholder="애니 제목을 입력하세요.",)
# st.write(user_input) # 검색한 거 확인 가능

for i, ani in enumerate(ani_list):
    if user_input and user_input in ani:
        st.image(img_list[i])