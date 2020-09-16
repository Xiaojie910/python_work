import sys

import pygame

from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboad import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	##初始化背景设置，让pygame能够正常的工作
	ai_settings = Settings()
	##游戏中的设置（游戏外观和飞船的属性）
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	##创建一个名字为screen的宽1200像素*高800像素的显示窗口
	pygame.display.set_caption("Alien Invasion")
	
	#创建一个按钮
	play_button = Button(ai_settings,screen,"play")
	
	#创建一个用于储存游戏统计信息的实例,并创建计分牌
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings,screen,stats)
	
	#创建一个飞船
	ship = Ship(ai_settings,screen)
	
	#创建一个用于储存子弹的编组
	bullets = Group()
	
	#创建一个储存外星人的编组
	aliens = Group()
	#创建外星人群
	gf.create_fleet(ai_settings,screen,ship,aliens)
	
	#开始游戏的主循环
	while True:
		#监视键盘和鼠标事件
		gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
			gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
		
		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
		
run_game()
##初始化游戏并开始主循环
