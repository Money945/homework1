import turtle  
  
# 设置画布和画笔  
screen = turtle.Screen()  
screen.title("Complex Coin Drawing")  
pen = turtle.Turtle()  
pen.speed(0)  
  
# 绘制硬币的主体（大圆）  
pen.penup()  
pen.goto(0, -100)  
pen.pendown()  
pen.circle(100)  
  
# 绘制边缘的波浪线纹理  
pen.penup()  
pen.goto(0, -100)  
pen.setheading(90)  # 向上  
for _ in range(20):  # 绘制20段波浪  
    pen.forward(20)  
    pen.right(10)  
    pen.forward(20)  
    pen.left(20)  
pen.pendown()  
  
# 绘制中心的复杂图案（多边形代表）  
pen.penup()  
pen.goto(0, -50)  
pen.pendown()  
pen.begin_fill()  
for _ in range(6):  # 六边形  
    pen.forward(30)  
    pen.right(60)  
pen.end_fill()  
  
# 添加文字标签  
pen.penup()  
pen.goto(-30, -40)  
pen.write("1 Cent", font=("Arial", 12, "bold"))  
  
# 隐藏画笔  
pen.hideturtle()  
  
# 点击窗口时退出  
screen.exitonclick()
