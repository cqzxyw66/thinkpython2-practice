import turtle

# 创建画笔并设置速度（0最快）
bob = turtle.Turtle()
bob.speed(1)
length = 10  # 基础长度，和原代码一致
angle = 50   # 转向角度，和原代码一致

# --------------- 手动复刻n=4时递归的所有操作 ---------------
# 注意：每一步都加了注释，对应原递归的执行逻辑
# 层级1：n=4的核心操作
bob.fd(length * 4)  # n=4前进：10*4=40
bob.lt(angle)       # 左转50°

# 层级2：n=3的核心操作（对应第一次draw(...,3)）
bob.fd(length * 3)  # n=3前进：10*3=30
bob.lt(angle)       # 左转50°

# 层级3：n=2的核心操作（对应第一次draw(...,2)）
bob.fd(length * 2)  # n=2前进：10*2=20
bob.lt(angle)       # 左转50°

# 层级4：n=1的核心操作（对应第一次draw(...,1)）
bob.fd(length * 1)  # n=1前进：10*1=10
bob.lt(angle)       # 左转50°
# n=0：无操作，直接返回
bob.rt(2 * angle)   # 右转100°（2*50）
# 再次调用draw(...,1)的n=0：无操作
bob.lt(angle)       # 左转50°
bob.bk(length * 1)  # n=1后退：10*1=10

# 回到层级3：n=2的后续操作
bob.rt(2 * angle)   # 右转100°
# 再次调用draw(...,2)的n=1操作（复刻一遍n=1的所有步骤）
bob.fd(length * 1)
bob.lt(angle)
bob.rt(2 * angle)
bob.lt(angle)
bob.bk(length * 1)

bob.lt(angle)       # 左转50°
bob.bk(length * 2)  # n=2后退：10*2=20

# 回到层级2：n=3的后续操作
bob.rt(2 * angle)   # 右转100°
# 再次调用draw(...,3)的n=2操作（复刻一遍n=2的所有步骤）
bob.fd(length * 2)
bob.lt(angle)
bob.fd(length * 1)
bob.lt(angle)
bob.rt(2 * angle)
bob.lt(angle)
bob.bk(length * 1)
bob.rt(2 * angle)
bob.fd(length * 1)
bob.lt(angle)
bob.rt(2 * angle)
bob.lt(angle)
bob.bk(length * 1)
bob.lt(angle)
bob.bk(length * 2)

bob.lt(angle)       # 左转50°
bob.bk(length * 3)  # n=3后退：10*3=30

# 回到层级1：n=4的后续操作
bob.rt(2 * angle)   # 右转100°
# 再次调用draw(...,4)的n=3操作（复刻一遍n=3的所有步骤）
bob.fd(length * 3)
bob.lt(angle)
bob.fd(length * 2)
bob.lt(angle)
bob.fd(length * 1)
bob.lt(angle)
bob.rt(2 * angle)
bob.lt(angle)
bob.bk(length * 1)
bob.rt(2 * angle)
bob.fd(length * 1)
bob.lt(angle)
bob.rt(2 * angle)
bob.lt(angle)
bob.bk(length * 1)
bob.lt(angle)
bob.bk(length * 2)
bob.rt(2 * angle)
bob.fd(length * 2)
bob.lt(angle)
bob.fd(length * 1)
bob.lt(angle)
bob.rt(2 * angle)
bob.lt(angle)
bob.bk(length * 1)
bob.rt(2 * angle)
bob.fd(length * 1)
bob.lt(angle)
bob.rt(2 * angle)
bob.lt(angle)
bob.bk(length * 1)
bob.lt(angle)
bob.bk(length * 2)
bob.lt(angle)
bob.bk(length * 3)

bob.lt(angle)       # 左转50°
bob.bk(length * 4)  # n=4后退：10*4=40

# 保持窗口打开
turtle.mainloop()