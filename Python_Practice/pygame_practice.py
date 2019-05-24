"""
Pygame进行游戏开发：
通过小游戏的编程，学会用编程思想解决现实中的问题
"""
# 制作游戏窗口
# 在窗口中绘图
import pygame


def main():
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示窗口并设计窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    x, y = 50, 50
    running = True
    # 绘制一个圆（参数分别是：屏幕，颜色，圆心位置，半径，0表示填充圆）
    pygame.draw.circle(screen, (255, 0, 0), (100, 100), 30, 0)
    """
    通过指定的文件名加载图像
    ball_image = pygame.image.load('./res/ball.png')
    在窗口上渲染图像
    screen.blit(ball_image,(50,50))
    """
    """
    实现动画的效果：
    原理：将不连续的图片连续的播放，每秒达到一定的帧数->动画效果
    例如将小球动起来，不断地修改小球的位置，然后刷新整个窗口
    """
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理、
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # 设置窗口的背景色
        screen.fill((255, 255, 255))
        # 绘制一个圆（参数分别是：屏幕，颜色，圆心位置，半径，0表示填充圆）
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 30, 0)
        pygame.display.flip()
        # 每个50毫秒就改变小球的位置再刷新窗口
        pygame.time.delay(50)
        x, y = x + 5, y + 5


if __name__ == '__main__':
    main()
