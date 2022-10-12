import sys
import test as test
from test import t_optimized as TS

def main(arg: str) -> None:
	if arg == 'test':
		try:
			test.check_execution_speed()
		except RuntimeError as err:
			print('Runtime error:', err.args[0])
	elif arg is None:
		items = [
		{"id": 1, "parent": "root"},
		{"id": 2, "parent": 1, "type": "test"},
		{"id": 3, "parent": 1, "type": "test"},
		{"id": 4, "parent": 2, "type": "test"},
		{"id": 5, "parent": 2, "type": "test"},
		{"id": 6, "parent": 2, "type": "test"},
		{"id": 7, "parent": 4, "type": None},
		{"id": 8, "parent": 4, "type": None},
		]      	
		ts = TS.TreeStore(items)      	
		TS.print_custom("Get ALL method and ARGs():", 'yellow')
		TS.print_custom(ts._getAll(), 'white')      	
		TS.print_custom("Get Item method and ARGs(7):", 'yellow')
		TS.print_custom(ts._getItem(7), 'white')      	
		TS.print_custom("Get ALL Children method and ARGs(4):", 'yellow')
		TS.print_custom(ts._getChildren(4), 'white')      	
		TS.print_custom("Get ALL Children method and ARGs(5):", 'yellow')
		TS.print_custom(ts._getChildren(5), 'white')      	
		TS.print_custom("Get ALL Parents method and ARGs(7):", 'yellow')
		TS.print_custom(ts._getAllParents(7), 'white')      	
		del ts, items
	else:
		TS.print_custom("Wrong [ARG]", 'red')

	
if __name__ == '__main__':
	if len(sys.argv) == 2:
		try:
			main(sys.argv[1])
		except RuntimeError as err:
			print('Runtime error:', err.args[0])
	elif len(sys.argv) > 2:
		print("Too many arguments")
	else:
		main(None)
		TS.print_custom('\nYou can write ["python3 main.py test"] to see the difference in speed.', 'green')