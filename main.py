import TreeStore as TS

def main() -> None:
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
	ts._getAll()
	ts._getItem(7)
	ts._getChildren(4)
	ts._getChildren(5)
	ts._getAllParents(7)
	
if __name__ == '__main__':
    main()