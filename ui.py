import pygame

class UI:
	def __init__(self, game):

		self.game = game
	
		self.health_icon_img = pygame.image.load('img/ui/health_icon.png').convert_alpha()
		self.health_bar_img = pygame.image.load('img/ui/health_bar.png').convert_alpha()
		self.coin_icon_img = pygame.image.load('img/ui/coin_icon.png').convert_alpha()
		self.health_icon_img = pygame.transform.scale(self.health_icon_img, (self.health_icon_img.get_width() * self.game.SCALE, self.health_icon_img.get_height() * self.game.SCALE))
		self.health_bar_img = pygame.transform.scale(self.health_bar_img, (self.health_bar_img.get_width() * self.game.SCALE, self.health_bar_img.get_height() * self.game.SCALE))
		self.coin_icon_img = pygame.transform.scale(self.coin_icon_img, (self.coin_icon_img.get_width() * self.game.SCALE, self.coin_icon_img.get_height() * self.game.SCALE))



		self.pos = (self.game.WIDTH * 0.02, self.game.HEIGHT * 0.02)
		self.offset = 50
		print(self.offset)

	def coin_display(self):
		self.coin_text_img = self.game.font.render(str(self.game.data['coins']), True, self.game.WHITE)
		self.game.screen.blit(self.coin_icon_img, (self.game.WIDTH - self.coin_icon_img.get_width(), self.game.HEIGHT - (self.coin_icon_img.get_height() * 2)))
		self.game.screen.blit(self.coin_text_img, (self.game.WIDTH - self.coin_icon_img.get_width() * 0.55, self.game.HEIGHT - (self.coin_icon_img.get_height() * 1.7)))

	def health_display(self):

		for box in range(self.game.max_health):
			box *= self.offset
			self.game.screen.blit(self.health_bar_img, ((box + self.offset, self.pos[1])))
		for box in range(self.game.current_health):
			box *= self.offset
			self.game.screen.blit(self.health_icon_img, ((box + self.offset, self.pos[1])))

		
	def render(self):
		self.health_display()
		self.coin_display()

class Inventory():
	def __init__(self, game, room):
		
		self.game = game
		self.room = room
		self.item_images = []
		self.timer = 0

		if self.game.data['bag'] == True:
			self.game.data['max_items'] = 8
			self.inventory_box_surf = pygame.image.load(f'img/ui/inventory_box.png').convert_alpha()
		else:
			self.game.data['max_items'] = 5
			self.inventory_box_surf = pygame.image.load(f'img/ui/inventory_box_small.png').convert_alpha()
		self.inventory_box_surf = pygame.transform.scale(self.inventory_box_surf, (self.inventory_box_surf.get_width() * self.game.SCALE, self.inventory_box_surf.get_height() * self.game.SCALE))
		self.inventory_box_rect = self.inventory_box_surf.get_rect(center = (self.game.WIDTH * 0.5, 50))


		for image in self.game.data['items']:
			text_img = self.game.font.render(str(image), True, self.game.BLACK)
			item_img = pygame.image.load(f'img/ui/items/{image}.png').convert_alpha()
			item_img = pygame.transform.scale(item_img, (item_img.get_width() * self.game.SCALE, item_img.get_height() * self.game.SCALE))
			self.item_images.append(item_img)

		self.offset_x = 120
		self.offset_y = self.inventory_box_rect.y + 80

		print(len(self.item_images))

	def inventory_display(self):
		self.game.screen.blit(self.inventory_box_surf, (self.inventory_box_rect.x, self.inventory_box_rect.y + self.timer))
		for slot in range(self.game.data['max_items']):
			if slot < len(self.item_images):
				img = self.item_images[slot]	
			else:
				img = pygame.Surface((80, 80))
				img.fill(self.game.BLUE)
			slot *= self.offset_x
			self.game.screen.blit(img, (self.inventory_box_rect.x - 60 + slot + self.offset_x, self.offset_y + self.timer))

	def render(self):
		if self.room.inventory_showing:
			self.timer += 20
		else:
			self.timer -= 20
		if self.timer >= 100:
			self.timer = 100
		elif self.timer <= -150:
			self.timer = -150

		self.inventory_display()

