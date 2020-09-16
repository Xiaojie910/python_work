import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	def __init__(self,ai_settings,screen):
		"""初始化飞船并设置其初始位置"""
		super(Ship,self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		
		#加载飞船图像并获取其外接矩形
		self.image = pygame.image.load('images/ship.bmp')
		##加载图像，返回一个表示飞船的surface，并将其储存到self.image中
		self.rect = self.image.get_rect()
		##获取相应surface的属性rect（矩形）
		self.screen_rect = screen.get_rect()
		##将屏幕矩形储存到self.screen_rect中
		
		#将每一艘新飞船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		##将飞船中心坐标self.rect.centerx设置为表示屏幕的矩形德属性self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		##将飞船下边缘的y坐标self.rect.bottom设置为表示屏幕的矩形的属性self.screen_rect.bottom
		
		#在飞船的属性center中储存小数值
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		
		#移动标志
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False 
	
	def update(self):
		"""根据移动标志调整飞船的位置"""
		#更新飞船的center值，而不是rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerx += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.centerx -= self.ai_settings.ship_speed_factor
		if self.moving_up and self.rect.top > self.screen_rect.top:
			self.centery -= self.ai_settings.ship_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.centery += self.ai_settings.ship_speed_factor
		
		#根据self.center更新rect对象
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery	
			
	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image,self.rect)
		##根据self.rect指定的位置将图像绘制在屏幕上
		
	def center_ship(self):
		"""让飞船在屏幕居中"""
		self.centerx = self.screen_rect.centerx
		self.centery = self.screen_rect.height - (0.5*self.rect.height)
