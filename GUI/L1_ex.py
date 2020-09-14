# 처음 시작하는 파이썬 GUI 프로그래밍

# from tkinter import *
import tkinter as tk

win = tk.Tk()  # Tk 클래스를 이용해서 윈도우 창을 생성

# 파이썬 tkinter 위젯 클래스 중에 Label, Button을 사용
label = tk.Label(win, text = "welcome to python") # 라벨 생성
button = tk.Button(win, text = "클릭") # 버튼 생성

label.pack()
button.pack()

win.mainloop()  # 이벤트 루프를 생성 => 이벤트 발생 감지