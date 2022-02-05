import imp
from operator import ne
import pygame
import random
import math
from DrawInformation import DrawInformation
from SortingAlgo import SortingAlgo


pygame.init()


FONT = pygame.font.SysFont('comicsans', 20)
LARGE_FONT = pygame.font.SysFont('comicsans', 30)


def draw(draw_info, algo_name, ascending):
	draw_info.window.fill(draw_info.BACKGROUND_COLOR)

	title = LARGE_FONT.render(
     	f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.BLUE)
	draw_info.window.blit(
     	title, (draw_info.width/2 - title.get_width()/2 , 5))

	controls = FONT.render(
     	"'R' - Reset | 'SPACE' - Start Sorting | 'A' - Ascending | 'D' - Descending", 1, draw_info.BLACK)
	draw_info.window.blit(
     	controls, (draw_info.width/2 - controls.get_width()/2 , 45))

	sorting = FONT.render(
     	"'I' - Insertion Sort | 'B' - Bubble Sort", 1, draw_info.BLACK)
	draw_info.window.blit(
     	sorting, (draw_info.width/2 - sorting.get_width()/2 , 75))

	draw_list(draw_info)
	pygame.display.update()


def draw_list(draw_info, color_positions={}, clear_bg=False):
	lst = draw_info.lst

	if clear_bg:
		clear_rect = (draw_info.SIDE_PAD//2, draw_info.TOP_PAD, 
						draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)
		pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

	for i, val in enumerate(lst):
		x = draw_info.start_x + i * draw_info.block_width
		y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

		color = draw_info.GRADIENTS[i % 3]

		if i in color_positions:
			color = color_positions[i] 

		pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))

	if clear_bg:
		pygame.display.update()


def generate_starting_list(n, min_val, max_val):
	lst = random.sample(range(n), n)
	new_list = [x+1 for x in lst]
	return new_list


def main():
	run = True
	clock = pygame.time.Clock()

	bins = 10
	min_val = 10
	max_val = 100
	SCREEN_HEIGHT = 600
	SCREEN_WIDTH = 800
	FPS = 30
 
	lst = generate_starting_list(bins, min_val, max_val)
	draw_info = DrawInformation(SCREEN_WIDTH, SCREEN_HEIGHT, lst)
	sorter = SortingAlgo()

	is_sorted = False
	ascending = True
 
	sorting_algorithm = sorter.bubble_sort
	sorting_algo_name = "Bubble Sort"
	sorting_algorithm_generator = None

	while run:
		clock.tick(FPS)

		if is_sorted:
			try:
				next(sorting_algorithm_generator)

			except StopIteration:
				is_sorted = False

		else:
			draw(draw_info, sorting_algo_name, ascending)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type != pygame.KEYDOWN:
				continue

			# reset
			if event.key == pygame.K_r:
				lst = generate_starting_list(bins, min_val, max_val)
				draw_info.set_list(lst)
				is_sorted = False
    
			# start sorting 
			elif event.key == pygame.K_SPACE and is_sorted == False:
				is_sorted = True
				sorting_algorithm_generator = sorting_algorithm(draw_info, draw_list, ascending)


			# choose sort ascending or descending
			elif event.key == pygame.K_a and not is_sorted:
				ascending = True
			elif event.key == pygame.K_d and not is_sorted:
				ascending = False
    
			# choose sorting algorithm
			elif event.key == pygame.K_i and not is_sorted:
				sorting_algorithm = sorter.insertion_sort
				sorting_algo_name = "Insertion Sort"
			elif event.key == pygame.K_b and not is_sorted:
				sorting_algorithm = sorter.bubble_sort
				sorting_algo_name = "Bubble Sort"

	pygame.quit()


if __name__ == "__main__":
	main()