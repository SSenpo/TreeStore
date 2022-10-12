from os import sep
from unittest import result


class Test:
	# Constructor call
	def __init__(self, items: list):
		# print_custom('[TEST] Class object init', 'green')
		if items is None:
			print_custom('Invalid values', 'red')
		
		self.items = items

	# Return all values
	def _getAll_TEST(self) -> list:
		# print_custom("Get ALL method[TEST]:", 'green')
		# print_custom(self.items, 'white')
		return self.items

	# Return value by ID
	def _getItem_TEST(self, it_number: int) -> list:
		result_item = []
		for i in self.items:
			if i.get('id') == it_number:
				result_item.append(i)
				break
		# print_custom("Get Items method[TEST]:", 'green')
		# print_custom(result_item, 'white')
		return result_item
	
	# Return all Childrens
	def _getChildren_TEST(self, parent_num: int) -> list:
		result_children = []

		for i in self.items:
			if i.get('parent') == parent_num:
				result_children.append(i)

		# print_custom("Get Children method[TEST]:", 'green')
		# print_custom(result_children, 'white')
		return result_children

	# Return all Parents
	def _getAllParents_TEST(self, child_num: int) -> list:
		result_parents = []
		next_chield = 0
		for i in self.items:
			if i.get('id') == child_num:
				next_chield = i.get('parent')
				break
		while True:
			parent_test = next_chield
			if parent_test is None or parent_test == 'root':
				break
			for i in self.items:
				if i.get('id') == parent_test:
					next_chield = i.get('parent')
					result_parents.append(i)
					break

		# print_custom("Get ALL Parents method[TEST]:", 'green')
		# print_custom(result_parents, 'white')
		return result_parents
	
	# Destructor call
	def __del__(self):
		pass
		# print_custom('[TEST] Class object destroyed', 'red')
		

# Print Custom function
def print_custom(text, color):
	check_color = ['yellow', 'white', 'green', 'red']
	if color not in check_color:
		raise ValueError('Invalid [color] value')
	if color == 'yellow':
		print("\n\033[33m\033[1m{}" .format(text))
		print('------------------------------'\
			'------------------------------\033[0m')
	elif color == 'green':
		print("\033[32m\033[1m {}" .format(text))
		print('--------------------------------------------------'\
			'----------\033[0m')
	elif color == 'white':
		if len(text) == 0:
			print("\033[37m\033[1m{}\033[0m" .format(text).center(70))
		else:
			for x in text:
				print("\033[37m\033[1m{}\033[0m" .format(x).center(70))
	elif color == 'red':
		print('\n\033[31m\033[1m----------------------------------------'\
			'--------------------')
		print("{}\033[0m" .format(text))