# 21.07.10 완성
import tkinter
import winsound

tk = tkinter.Tk()
tk.title("MAZE")                  # title
canvas = tkinter.Canvas(width=800, height=650, bg="black")
#canvas.create_rectangle(50, 50, 200, 200, fill="red", outline="green", width=10)                 #좌층상단, 우측상단 좌표
#create_rectangle(x1, y1, x2, y2, fill=fullColour, outline=lineColour, width=lineWidth)
canvas.pack()

#position 초기값
posX = 1
posY = 1                 # 챔프 위치 변수
pa=50
px=25
py=25
mushX = 1                  
mushY = 1               # 아이템 위치 변수
ma=50
mx=25
my=325
#itemX = 0, itemY = 0
isItem = 0                  

keyInput = ""               # 키 입력 전역변수 선언

def key_Down(i):            #키 누를 때
       global keyInput
       keyInput = i.keysym         # 입력한 키에 이름
       print(keyInput)

def key_Up(i):                   #키 뗐을 때
       global keyInput          
       keyInput = ""               # 키 값을 다시 초기화
       print(keyInput)

def playerMove():
       global posX, posY

       if keyInput == "Up" and gameMap[posY-1][posX] != 1:
              posY -= 1
       if keyInput == "Down" and gameMap[posY+1][posX] != 1:
              posY += 1
       if keyInput == "Left" and gameMap[posY][posX-1] != 1:
              posX -= 1
       if keyInput == "Right" and gameMap[posY][posX+1] != 1:
              posX += 1
       canvas.coords("player", posX * pa + px, posY * pa + py)        #플레이어 이동
       tk.after(60, playerMove)                         #0.2초 후에 실행

       if mushX * ma + mx-50 <= posX * pa + px <= mushX * ma + mx+50:        # 아이템 삭제 범위 x좌표
              if mushY * ma + my-30 <= posY * pa + py <= mushY * ma + my+30:        # 아이템 삭제 범위 y좌표
                     canvas.delete("item")                     # 아이템 삭제
                     winsound.PlaySound("coin.way", winsound.SND_ASYNC)      # 소리 재생

gameMap = [
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
       [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
       [1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
       [1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
       [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
       [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
       [1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1],
       [1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
for y in range(12):
       for x in range(16):
              if gameMap[y][x] == 1:                    #1인 부분만 블럭 생성
                     canvas.create_rectangle(x * 50,y * 50,x * 50 + 50, y * 50 + 50,
                     fill="pink", outline="red", width=5)
              # elif gameMap[y][x] == 2:
              #        canvas.create_image(mushX * ma + mx, mushY * ma + my, image=img1, tag="item")
#create_rectangle(x1, y1, x2, y2, fill=fullColour, outline=lineColour, width=lineWidth)

img = tkinter.PhotoImage(file="ch.png")           #플레이어 지정
canvas.create_image(posX * pa + px, posY * pa + py, image=img, tag="player")        #플레이어배치
tk.bind("<KeyPress>", key_Down)
tk.bind("<KeyRelease>", key_Up)
playerMove()                       #플레이어 이동 함수

img1 = tkinter.PhotoImage(file="sue.png")
canvas.create_image(mushX * ma + mx, mushY * ma + my, image=img1, tag="item")

tk.mainloop()
