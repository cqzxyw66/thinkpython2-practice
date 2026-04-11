import turtle

# ==========================================
# 1. 定义所有动漫造型的核心坐标 (100% 都是 tuple)
# ==========================================

# 葫芦娃头部轮廓 (动漫方脸)
HEAD = (
    (-25, 20), (25, 20), (30, 0), (25, -20),
    (-25, -20), (-30, 0), (-25, 20)
)

# 头顶的葫芦叶子 (动漫特征叶子)
LEAF = (
    (0, 20), (15, 40), (30, 35), (20, 25), (10, 30),
    (0, 20), (-15, 40), (-30, 35), (-20, 25), (-10, 30), (0, 20)
)

# 眼睛 (大而圆的动漫眼)
EYE_L = (-12, 5)
EYE_R = (12, 5)
EYE_PUPIL = (-12, 5, -4, 10), (12, 5, 4, 10)  # 眼珠高光轨迹

# 嘴巴 (微笑动漫嘴)
MOUTH = ((-10, -10), (10, -10))

# 身体 (简单方块)
BODY = ((-20, -20), (-20, -50), (20, -50), (20, -20))

# 七个葫芦娃的 X 轴位置
BROTHERS_POS = (-240, -160, -80, 0, 80, 160, 240)

# ==========================================
# 2. 画图工具函数
# ==========================================
def draw_path(points, offset_x):
    """根据 tuple 坐标画线"""
    turtle.penup()
    # 处理单个点 tuple 或连续坐标 tuple
    if isinstance(points[0], (int, float)):
        turtle.goto(offset_x + points[0], points[1])
    else:
        turtle.goto(offset_x + points[0][0], points[0][1])
    turtle.pendown()
    for p in points:
        if isinstance(p, (int, float)):
            turtle.goto(offset_x + p, points[1])
            break
        turtle.goto(offset_x + p[0], p[1])

# ==========================================
# 3. 绘制单个葫芦娃
# ==========================================
def draw_calabash(offset_x):
    # 叶子
    draw_path(LEAF, offset_x)
    
    # 头部轮廓
    draw_path(HEAD, offset_x)
    
    # 眼睛 (单独画圆点)
    turtle.penup()
    turtle.goto(offset_x + EYE_L[0], EYE_L[1])
    turtle.pendown()
    turtle.circle(3)  # 左眼
    turtle.penup()
    turtle.goto(offset_x + EYE_R[0], EYE_R[1])
    turtle.pendown()
    turtle.circle(3)  # 右眼
    
    # 眼珠高光 (用短线表示)
    draw_path(EYE_PUPIL[0], offset_x)
    draw_path(EYE_PUPIL[1], offset_x)

    # 嘴巴
    draw_path(MOUTH, offset_x)

    # 身体
    draw_path(BODY, offset_x)

# ==========================================
# 4. 主程序运行
# ==========================================
turtle.speed(0)  # 最快速度
turtle.hideturtle()

# 循环画出七个葫芦娃
for x in BROTHERS_POS:
    draw_calabash(x)

turtle.done()