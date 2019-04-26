"""飞机大战雏形"""

import pygame as pg
from planeGame.plane_sprites import *

# 必不可少的代码，游戏的初始化
pg.init()

screen = pg.display.set_mode((480, 700))

# 绘制背景图像
# 1.加载图像的数据
bg = pg.image.load("./images/background.png")
# 2.屏幕对象调用bilt 绘制图像
screen.blit(bg, (0, 0))

# 绘制飞机
plane = pg.image.load("./images/me1.png")
screen.blit(plane, (200, 500))

# 3.更新屏幕显示
pg.display.update()

# 创建时钟对象
clock = pg.time.Clock()

# a. 定义rect记录飞机的初始位置
hero_rect = pg.Rect(150, 300, 102, 126)


# 创建敌机的精灵
enemy = GameSprite("./images/enemy1.png")
# 创建敌机的精灵组
enemy_group = pg.sprite.Group(enemy)

#游戏循环
while True:

    # 设置屏幕刷新帧率
    clock.tick(60)

    #捕获事件
    for event in pg.event.get():
        # 判断用户是否点击了关闭按钮
        if event.type == pg.QUIT:
            print("退出游戏。。。。")

            pg.quit()
            # 直接退出系统
            exit()

#     b. 修改飞机的位置
    hero_rect.y -= 1

    # 判断飞机的位置
    if hero_rect.y <= -126:
        hero_rect.y = 700

#     c. 调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(plane, hero_rect)

#     让精灵组调用两个方法
#     update -- 让组中的所有精灵更新位置
    enemy_group.update()
#     draw -- 在screen绘制所有精灵
    enemy_group.draw(screen)


#     d. 调用update方法更新显示
    pg.display.update()
# 必不可少的代码，游戏代码的结束
pg.quit()