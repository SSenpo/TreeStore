from os import sep
from unittest import result



class TreeStore:
	# Constructor call
	def __init__(self, items: list):
		print_custom('[TreeStore] Class object init', 'green')
		if items is None:
			print_custom('Invalid values', 'red')
		
		self.items = items
		self.it_dict = {}
		self._setDict()

	# Create and complete the dictionary based on the data received
	def	_setDict(self) -> None:
		for i in self.items:
			key = i.get('id')
			parent = i.get('parent')
			if parent is None or key is None:
				raise ValueError('\033[33mItems list miss [id] or [parent]\033[0m')
			self.it_dict.setdefault(key, i)
			childrens_list =[]
			for x in self.items:
				if x.get('parent') == key:
					childrens_list.append(x)
			self.it_dict.setdefault('Parent_{}'.format(key), parent)
			self.it_dict.setdefault('Children_{}'.format(key), childrens_list)

	# Return all values
	def _getAll(self) -> list:
		return self.items

	# Return value by ID
	def _getItem(self, it_number: int) -> list:
		result_item = []
		result_item.append(self.it_dict.get(it_number))
		return result_item
	
	# Return all Childrens
	def _getChildren(self, parent_num: int) -> list:
		result_children = self.it_dict.get(f'Children_{parent_num}')
		return result_children

	# Return all Parents
	def _getAllParents(self, child_num: int) -> list:
		result_parents = []
		while True:
			parent = self.it_dict.get('Parent_{}'.format(child_num))
			if parent == 'root' or parent == None:
				break
			else:
				result_parents.append(self.it_dict.get(parent))
				child_num = parent
		return result_parents
	
	# Destructor call
	def __del__(self):
		print_custom('[TreeStore] Class object destroyed', 'red')
		

# Print Custom function
def print_custom(text, color):
	check_color = ['yellow', 'white', 'green', 'red', 'test1', 'test2']
	if color not in check_color:
		raise ValueError('Invalid [color] value')
	elif color == 'yellow':
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
	# **---------------------------------**
	elif color == 'test1':
		print(f'\033[32m\033[1mOptimized_TreeStore: {text:.10f}\033[0m')
	elif color == 'test2':
		print(f'\033[34m\033[1mNot_Optimized_TreeStore: {text:.10f}\033[0m')