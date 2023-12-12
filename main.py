from tkinter import *
from PyKakao import Karlo
import ssl
import random
ssl._create_default_https_context = ssl._create_unverified_context

api = Karlo("727f2b0c5a6770bfbbd0a3536c899ca0")

random_list = ['cat', 'dog', 'duck', 'bird']
ran = random.choice(random_list)

# 프롬프트에 사용할 제시어
prompt = ran
negative_prompt = "sleeping cat, dog, human, ugly face, cropped, worst quality, bad atonomy"

# 이미지 생성하기 REST API 호출
response = api.text_to_image(prompt, negative_prompt)

# 응답의 첫 번째 이미지 생성 결과 출력하기
img = api.get_first_image_from_response(response)

img.save(f"./{ran}.png")

tk = Tk() 

tk.geometry("900x600")       # 창 크기설정
tk.title("동물 이름 맞추기")    # 창 제목설정
tk.option_add("*Font","맑은고딕 25") # 폰트설정
tk.resizable(True, True)  # x, y 창 크기 변경 불가

# 2. 텍스트 표시
label = Label(tk, text='버튼을 눌러 고양이를 생성하세요',fg='black',font=40) # fg는 글자 색 지정, font로 글자 설정
label2 = Label(tk, text='냐옹',font=3)
photo = PhotoImage(file='/Users/yujiwon/python3/project/hello/original.png')
label3 = Label(tk, image=photo)

ent = Entry(tk) # root라는 창에 입력창 생성
ent.config(width=30)              # 입력창 크기 설정
ent.config(fg="black", bg="light gray") # 입력창 배경, 글자색 설정
ent.insert(0, "정답을 맞춰주세요!")    # 처음 입력창에 첫번째 자리(0)에 텍스트를 입력
dab = ent.get()

# 3. 레이블 배치 실행
label.pack()
label2.pack()
label3.pack()
ent.pack()

# 4. 메인루프 실행


def event():
    response = api.text_to_image(prompt, negative_prompt)
    # 응답의 첫 번째 이미지 생성 결과 출력하기
    img = api.get_first_image_from_response(response)
    img.save(f"./{ran}.png")
    photo.config(file=f"/Users/yujiwon/python3/project/hello/{ran}.png")
    label3.pack()
    if dab == ran:
        label.config(tk, text='정답입니다!',fg='red',font=40)
        label.pack()

    else :
        label.config(tk, text='틀렸습니다!',fg='red',font=40)
        label.pack()

button = Button(tk,text='다음 문제',command=event,width=10,padx=10,pady=10)
button.pack() 



tk.mainloop()




