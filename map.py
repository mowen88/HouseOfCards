import pygame
from state import State

class RoomSprite(pygame.sprite.Sprite):
	def __init__(self, pos, surf):
		self.image = pygame.image.load(surf).convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)
		self.vel = pygame.math.Vector2()

class Inventory():
	def __init__(self, game):
		self.game = game


		self.item_images = []

		if self.game.data['bag'] == True:
			self.game.data['max_items'] = 8
			self.inventory_box_surf = pygame.image.load(f'img/ui/inventory_box.png').convert_alpha()
		else:
			self.game.data['max_items'] = 5
			self.inventory_box_surf = pygame.image.load(f'img/ui/inventory_box_small.png').convert_alpha()
		self.inventory_box_surf = pygame.transform.scale(self.inventory_box_surf, (self.inventory_box_surf.get_width() * self.game.SCALE, self.inventory_box_surf.get_height() * self.game.SCALE))
		self.inventory_box_rect = self.inventory_box_surf.get_rect(center = (self.game.WIDTH * 0.5, self.game.HEIGHT * 0.75))


		for image in self.game.data['items']:
			text_img = self.game.font.render(str(image), True, self.game.BLACK)
			item_img = pygame.image.load(f'img/ui/items/{image}.png').convert_alpha()
			item_img = pygame.transform.scale(item_img, (item_img.get_width() * self.game.SCALE, item_img.get_height() * self.game.SCALE))
			self.item_images.append(item_img)

		self.offset_x = 120
		self.offset_y = self.inventory_box_rect.y + 80

		print(len(self.item_images))

	def inventory_display(self):
		self.game.screen.blit(self.inventory_box_surf, self.inventory_box_rect)

		for slot in range(self.game.data['max_items']):
			if slot < len(self.item_images):
				img = self.item_images[slot]	
			else:
				img = pygame.Surface((80, 80))
				img.fill(self.game.BLUE)
			slot *= self.offset_x
			self.game.screen.blit(img, (self.inventory_box_rect.x - 60 + slot + self.offset_x, self.offset_y))

	
	def render(self):
		self.inventory_display()



class Map(State):
	def __init__(self, game, room):
		State.__init__(self, game)
		self.game = game
		self.room = room
		self.display_surf = pygame.display.get_surface()
		pos = (self.game.WIDTH // 12, self.game.HEIGHT // 12) # split the screen into 12x12 grid to place room sprites easily
		
		self.inventory = Inventory(self.game)

		self.rooms = {
		'test': RoomSprite((pos[0] * 8, pos[1] * 4), 'rooms/test/map_piece.png'),
		'jail': RoomSprite((pos[0] * 8, pos[1] * 4), 'rooms/jail/map_piece.png'),
		'courtroom': RoomSprite((pos[0] * 4, pos[1] * 4), 'rooms/courtroom/map_piece.png'),
		'hallway': RoomSprite((pos[0] * 1, pos[1] * 4), 'rooms/hallway/map_piece.png'),
		'pantry': RoomSprite((pos[0] * 2, pos[1] * 2), 'rooms/pantry/map_piece.png'),
		}
		

		marker_offset_x = (self.rooms[self.game.current_room].rect.width * (self.room.player.hitbox.centerx/self.room.visible_sprites.room_size[0])) * self.game.SCALE
		marker_offset_y = (self.rooms[self.game.current_room].rect.height * (self.room.player.hitbox.centery/self.room.visible_sprites.room_size[1])) * self.game.SCALE


		marker_pos_x = self.rooms[self.game.current_room].rect.x + marker_offset_x
		marker_pos_y = self.rooms[self.game.current_room].rect.y + marker_offset_y
		self.marker_pos = (marker_pos_x, marker_pos_y)

		print(marker_offset_x)

		# player marker
		self.marker_surf = pygame.image.load('img/ui/marker.png').convert_alpha()
		self.marker_rect = self.marker_surf.get_rect(center = self.marker_pos)
		# self.icon_rect = self.marker_surf.get_rect(center = (self.game.WIDTH //2 - 120, self.game.HEIGHT - 192))
	
	def show_rooms(self):
		for sprite in self.rooms.values():
			sprite.image = pygame.transform.scale(sprite.image, (sprite.rect.width * self.game.SCALE, sprite.rect.height * self.game.SCALE))
			self.display_surf.blit(sprite.image, sprite.rect)


	def update(self, actions):
		if self.game.actions['m']:
			self.exit_state()
		self.game.reset_keys()

	def render(self, display):
		self.display_surf.fill(self.game.WHITE)
		# self.prev_state.prev_state.render(display)
		#self.prev_state.render(display)

		self.show_rooms()
		#self.inventory.inventory_display()
		self.display_surf.blit(self.marker_surf, self.marker_rect)


		

	




		





	