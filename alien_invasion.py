# 导入sys模块和pygame模块
# pygame模块包含开发游戏所需的功能，当玩家退出时，使用sys模块中的工具来退出游戏
import sys

import pygame
from settings import Settings
from ship import Ship

# 创建类【AlienInvasion】
class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        # 调用pygame.init()函数来初始化背景
        pygame.init()
        # 创建pygame.time模块中的Clock类的一个实例，然后在run_game()的while循环末尾让这个时钟进行计时
        self.clock = pygame.time.Clock()
        # 调用pygame.display.set_mode()创建一个显示窗口
        # 实参(1200, 800)是一个元组，指定游戏窗口的尺寸（宽，高）
        # 将这个显示窗口赋值给属性self.screen，让这个类的所有方法都能够使用它
        # 赋给属性self.screen的对象是一个surface。在pygame中，surface是屏幕的一部分，用以显示游戏元素
        # 在这个游戏中，每个元素（如外星人或飞船）都是一个surface
        # display.set_mode()返回的surface表示整个游戏窗口，激活游戏的动画循环后
         # 每经过一次循环都将自动重绘这个surface，将用户输入触发的所有变化都反应出来
        self.settings = Settings() #创建Settings实例
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        #self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        # 设置背景色
        #self.bg_color = (230, 230, 230)
        self.ship = Ship(self)

    # 此游戏由run_game()方法控制。
    def run_game(self):
        """开始游戏的主循环"""
        # 这个循环包含一个事件循环以及管理屏幕更新的代码
        # 事件是用户玩游戏时执行的操作，如按键或移动鼠标。
        while True:
            #重构后：
            self._check_events() #调用_check_events方法
            self.ship.update()
            self._update_screen() #调用_update_screen方法
            # tick方法接受一个参数：游戏的帧率
            self.clock.tick(60)

    def _check_events(self):
        """响应按键和鼠标事件"""
        # 侦听键盘和鼠标事件
        # 事件循环，以侦听事件并根据发生的事件类型执行适当的任务。
        # 使用pygame.event.get()函数来访问pygame检测到的事件
        # 这个函数返回一个列表，包含它在上一次调用后发生的所有事件
        # 所有键盘和鼠标事件都将导致这个for循环运行
        for event in pygame.event.get():
            # 使用if语句来检测并响应特定的事件
            # 当玩家单击游戏窗口的关闭按钮，将检测到pygame.QUIT事件
            if event.type == pygame.QUIT:
                # 进而调用sys.exit()来退出游戏
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """响应按下"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        # 按q结束游戏
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """响应释放"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        # 每次循环都重绘屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # 让最近绘制的屏幕可见【更新屏幕】
        # 每次执行while循环时都会绘制一个空屏幕，并擦去旧屏幕，使得只有一个新的空屏幕可见
        pygame.display.flip()

if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()