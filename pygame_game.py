import pygame
import os
import time
import __future__
import random	
	
class sprite_object:
	"""docstring for alien_object"""
	def __init__(self, x, y, name):
		self.type_img = name
		self.x_cord = x
		self.y_cord = y


def make_text_objs(text, font) :
	text_surface = font.render(text, True, white)
	return text_surface, text_surface.get_rect()


def replay_or_quit() :
	for event in pygame.event.get([pygame.KEYDOWN, pygame.QUIT]) :
		if event.type == pygame.QUIT :
			pygame.quit()
			quit()
		elif event.type == pygame.KEYDOWN :
			return event.key

	return None

def score_display(score):
	small_text = pygame.font.Font('freesansbold.ttf', 20)
	type_text_surface, type_text_rect = make_text_objs(str(score), small_text)
	type_text_rect.center = surface_width - 30 , 30
	surface.blit(type_text_surface, type_text_rect)

	

def msg_surface(text):
	small_text = pygame.font.Font('freesansbold.ttf', 20)
	large_text = pygame.font.Font('freesansbold.ttf', 150)

	title_Text_surf, title_text_rect = make_text_objs(text, large_text)
	title_text_rect.center = surface_width / 2, surface_height/2

	surface.blit(title_Text_surf, title_text_rect)


	type_text_surface, type_text_rect = make_text_objs('press any key to continue: ', small_text)
	type_text_rect.center = surface_width /2 , ((surface_height /2) + 100)
	surface.blit(type_text_surface, type_text_rect)

	pygame.display.update()
	time.sleep(.5)

	while replay_or_quit() == None: 
		clock.tick()

	
	game_loop()


def game_over() :
	msg_surface('Kaboom!') 


def image_print(x, y, image):
	surface.blit(image, (x,y))


#pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag                              #initialize pygame




surface_width = 800
surface_height = 500
img_size = 50

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

pygame.mixer.music.load('/Users/helmutcardenas/Desktop/python/rifle.mp3')

#load music
#pygame.mixer.music.load('arcade.mp3')

#rifle = pygame.mixer.Sound('/Users/helmutcardenas/Desktop/python/rifle.mp3')  #load sound
#fail = pygame.mixer.Sound(os.path.join('data','fail.wav'))  #load sound

# play music non-stop
pygame.mixer.music.play(-1) 

black = (0,0,0)			# black color for background
white = (255,255,255)	# white color

surface = pygame.display.set_mode((surface_width, surface_height)) # creates a display
pygame.display.set_caption("Helicopter") # gives display a name
clock = pygame.time.Clock() # sets the frames per second

# the reazon why we define the image outside of helicopter is because we dont 
# want to load the image every time instead of jkust one time here
heli_img = pygame.image.load('/Users/helmutcardenas/Desktop/python/heli.png')
alien_img = pygame.image.load('/Users/helmutcardenas/Desktop/python/alien2.png')
bull_img = pygame.image.load('/Users/helmutcardenas/Desktop/python/bull.png')
explos_img = pygame.image.load('/Users/helmutcardenas/Desktop/python/explosion.png')

MAX_NUM_ALIEN = 5

def game_loop():


	x = 150		# star values of heli
	y = 150		# star value of heli
	player_helicopter = sprite_object(x,y, "helicopter")

	y_move = 0
	x_move = 5

	score = 0


	alien_on_screen_count = 0

	alien_list = []
	bullet_list = []
	

	game_over_var = False
	pygame.time.set_timer(pygame.USEREVENT+1, 500)

	while not game_over_var :

		for event in pygame.event.get():		# itterates tru event handler list
			if event.type == pygame.QUIT:
				game_over_var = True

			if event.type == pygame.KEYDOWN:
				print (event)
				if event.key == pygame.K_UP:
					y_move = -5

			if event.type == pygame.KEYDOWN:
				print (event)
				if event.key == pygame.K_DOWN:
					y_move = 5

			if event.type == pygame.KEYDOWN:
				print (event)
				if event.key == pygame.K_LEFT:
					x_move = -5

			if event.type == pygame.KEYDOWN:
				print (event)
				if event.key == pygame.K_RIGHT:
					x_move = 5

			if event.type == pygame.USEREVENT+1:
				alien_list.append(sprite_object(surface_width - 80, 
					random.randint(100, surface_height - 70) - 100, "alien"))

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE :
					bullet_list.append(sprite_object(player_helicopter.x_cord + 10, player_helicopter.y_cord,
						"bullet"))
					#rifle.play()




			
		if player_helicopter.y_cord > surface_height - 48 or player_helicopter.y_cord < 0:
			game_over()

		player_helicopter.y_cord += y_move
		player_helicopter.x_cord += x_move

		for alien in alien_list :
			alien.x_cord += -6
			if alien.x_cord == 0:
				alien_list.remove(alien)
				score += 10
			if (alien.x_cord <= player_helicopter.x_cord + img_size and alien.x_cord >= player_helicopter.x_cord - img_size)  and (alien.y_cord <= player_helicopter.y_cord+img_size and alien.y_cord >= player_helicopter.y_cord- img_size) :
				game_over()

			for bull in bullet_list :
				if (alien.x_cord <= bull.x_cord + img_size and alien.x_cord >= bull.x_cord - img_size) and (alien.y_cord <= bull.y_cord + img_size and alien.y_cord >= bull.y_cord - img_size ):
					image_print(alien.x_cord, alien.y_cord, explos_img)
					alien_list.remove(alien)
					pygame.display.update()
					bullet_list.remove(bull)

					score += 100
					break


		for bullet in bullet_list :
			bullet.x_cord += 10
			if bullet.x_cord == surface_width + 100 :
				bullet_list.remove(bullet)





		# this needs to happen before we draw the helicopters or aliens 
		surface.fill(black)

		image_print(player_helicopter.x_cord,player_helicopter.y_cord, heli_img)
		
		#print (len(alien_list))
		for alien in alien_list :
			image_print(alien.x_cord, alien.y_cord, alien_img)

		for bullet in bullet_list :
			image_print(bullet.x_cord, bullet.y_cord, bull_img)


		score_display(score)
		pygame.display.update() # update with no parameter just re draws the whole screen 
		clock.tick(60)	# sets the frames per secoonds 


		#print (score)


	pygame.quit()
	quit()


if __name__ == '__main__':
	game_loop()




