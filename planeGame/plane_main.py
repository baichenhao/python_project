
import pygame
from planeGame.plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏"""

    # 初始化函数
    def __init__(self):
        print("游戏初始化...")
        # 1.创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3.调用私有方法，精灵和精灵族的创建
        self.__creta_sprites()
        # 4.设置定时器事件 - 创建敌机  1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        # 英雄飞机发射子弹定时器
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    # 创建精灵函数
    def __creta_sprites(self):
        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 1.创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    # 游戏开始函数
    def start_game(self):
        print("游戏开始...")

        while True:
            # 1.设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2.事件监听
            self.__event_handler()
            # 3.碰撞检测
            self.__check_collide()
            # 4.更新/绘制精灵组
            self.__update_sprites()
            # 5.更新显示
            pygame.display.update()

    #  事件监听函数
    def __event_handler(self):
        for event in pygame.event.get():
            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print("敌机出场...")
                # 创建敌机精灵
                enemy = Enemy()

                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

            # 监听模块 一次按下和一次抬起 算是一个完整操作
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动...")

        # 返回所有按键的元组，如果某个键被按下，对应的值会是1
        key = pygame.key.get_pressed()
        # 判断是否按下了方向键
        if key[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif key[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    # 碰撞检测函数
    def __check_collide(self):

        # 1.子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

        # 2.敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        # 判断列表是否有内容
        if len(enemies) > 0:
            # 英雄牺牲
            self.hero.kill()

            # 结束游戏
            PlaneGame.__game_over()

    # 更新精灵组函数
    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    # 静态方法：对象属性和类属性都没有使用
    @staticmethod
    def __game_over():
        print("游戏结束...")
        pygame.display.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    game.start_game()
