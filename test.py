import TreeStore as t_optimized
import another_version as t_std
import timeit


def check_execution_speed() -> None:
	# Some ITEMS--------------------------------------------------------------- #
	items = [
		{"id": 1, "parent": "root"},
		{"id": 2, "parent": 1, "type": "test"}, {"id": 3, "parent": 1, "type": "test"}, {"id": 4, "parent": 2, "type": "test"},
		{"id": 5, "parent": 2, "type": "test"}, {"id": 6, "parent": 2, "type": "test"}, {"id": 7, "parent": 4, "type": None},
		{"id": 8, "parent": 4, "type": None}, {"id": 9, "parent": 6, "type": "test"}, {"id": 10, "parent": 7, "type": "test"},
		{"id": 11, "parent": 8, "type": "test"}, {"id": 12, "parent": 8, "type": "test"}, {"id": 13, "parent": 10, "type": "test"},
		{"id": 14, "parent": 11, "type": "test"}, {"id": 15, "parent": 12, "type": "test"}, {"id": 16, "parent": 12, "type": "test"},
		{"id": 17, "parent": 14, "type": None}, {"id": 18, "parent": 14, "type": None}, {"id": 19, "parent": 16, "type": "test"},
		{"id": 20, "parent": 17, "type": "test"}, {"id": 21, "parent": 18, "type": "test"}, {"id": 22, "parent": 18, "type": "test"},
		{"id": 23, "parent": 20, "type": "test"}, {"id": 24, "parent": 21, "type": "test"}, {"id": 25, "parent": 20, "type": "test"},
		{"id": 26, "parent": 20, "type": "test"}, {"id": 27, "parent": 20, "type": None}, {"id": 28, "parent": 20, "type": None},
		{"id": 29, "parent": 20, "type": "test"}, {"id": 30, "parent": 20, "type": "test"}, {"id": 31, "parent": 20, "type": "test"},
		{"id": 32, "parent": 20, "type": "test"}, {"id": 33, "parent": 20, "type": "test"}, {"id": 34, "parent": 20, "type": "test"},
		{"id": 35, "parent": 20, "type": "test"}, {"id": 36, "parent": 20, "type": "test"}, {"id": 37, "parent": 20, "type": None},
		{"id": 38, "parent": 20, "type": None}, {"id": 39, "parent": 20, "type": "test"}, {"id": 40, "parent": 20, "type": "test"},
		{"id": 41, "parent": 20, "type": "test"}, {"id": 42, "parent": 20, "type": "test"}, {"id": 43, "parent": 20, "type": "test"},
		{"id": 44, "parent": 20, "type": "test"}, {"id": 45, "parent": 20, "type": "test"}, {"id": 46, "parent": 20, "type": "test"},
		{"id": 47, "parent": 20, "type": None}, {"id": 48, "parent": 20, "type": None}, {"id": 49, "parent": 20, "type": "test"},
		{"id": 50, "parent": 23, "type": "test"}, {"id": 61, "parent": 20, "type": "test"}, {"id": 62, "parent": 20, "type": "test"},
		{"id": 63, "parent": 20, "type": "test"}, {"id": 64, "parent": 20, "type": "test"}, {"id": 65, "parent": 20, "type": "test"},
		{"id": 66, "parent": 20, "type": "test"}, {"id": 67, "parent": 20, "type": None}, {"id": 68, "parent": 20, "type": None},
		{"id": 69, "parent": 20, "type": "test"}, {"id": 70, "parent": 20, "type": "test"}, {"id": 71, "parent": 20, "type": "test"},
		{"id": 72, "parent": 20, "type": "test"}, {"id": 73, "parent": 20, "type": "test"}, {"id": 74, "parent": 20, "type": "test"},
		{"id": 75, "parent": 20, "type": "test"}, {"id": 76, "parent": 20, "type": "test"}, {"id": 77, "parent": 50, "type": None},
		{"id": 78, "parent": 77, "type": None}, {"id": 79, "parent": 20, "type": "test"}, {"id": 80, "parent": 20, "type": "test"},
		{"id": 81, "parent": 20, "type": "test"}, {"id": 82, "parent": 20, "type": "test"}, {"id": 83, "parent": 20, "type": "test"},
		{"id": 84, "parent": 20, "type": "test"}, {"id": 85, "parent": 20, "type": "test"}, {"id": 86, "parent": 20, "type": "test"},
		{"id": 87, "parent": 20, "type": None}, {"id": 88, "parent": 20, "type": None}, {"id": 89, "parent": 20, "type": "test"},
		{"id": 90, "parent": 78, "type": "test"}, {"id": 91, "parent": 90, "type": "test"}, {"id": 92, "parent": 91, "type": "test"},
		{"id": 93, "parent": 92, "type": "test"}, {"id": 94, "parent": 93, "type": "test"}, {"id": 95, "parent": 94, "type": "test"},
		{"id": 96, "parent": 95, "type": "test"}, {"id": 97, "parent": 20, "type": None}, {"id": 98, "parent": 20, "type": None},
		{"id": 99, "parent": 20, "type": "test"}, {"id": 100, "parent": 20, "type": "test"}, {"id": 100, "parent": 20, "type": "test"},
		{"id": 101, "parent": 20, "type": "test"}, {"id": 102, "parent": 20, "type": "test"}, {"id": 103, "parent": 20, "type": "test"},
		{"id": 104, "parent": 20, "type": "test"}, {"id": 105, "parent": 20, "type": "test"}, {"id": 106, "parent": 20, "type": "test"},
		{"id": 107, "parent": 20, "type": None}, {"id": 108, "parent": 20, "type": None}, {"id": 109, "parent": 20, "type": "test"},
		{"id": 110, "parent": 20, "type": "test"}, {"id": 111, "parent": 20, "type": "test"}, {"id": 112, "parent": 20, "type": "test"},
		{"id": 113, "parent": 20, "type": "test"}, {"id": 114, "parent": 20, "type": "test"}, {"id": 115, "parent": 20, "type": "test"},
		{"id": 116, "parent": 20, "type": "test"}, {"id": 117, "parent": 20, "type": None}, {"id": 118, "parent": 20, "type": None},
		{"id": 119, "parent": 20, "type": "test"}, {"id": 120, "parent": 20, "type": "test"}, {"id": 121, "parent": 20, "type": "test"},
		{"id": 122, "parent": 20, "type": "test"}, {"id": 123, "parent": 20, "type": "test"}, {"id": 124, "parent": 20, "type": "test"},
		{"id": 125, "parent": 20, "type": "test"}, {"id": 126, "parent": 20, "type": "test"}, {"id": 127, "parent": 20, "type": None},
		{"id": 128, "parent": 20, "type": None}, {"id": 129, "parent": 20, "type": "test"}, {"id": 130, "parent": 20, "type": "test"},
		{"id": 131, "parent": 20, "type": "test"}, {"id": 132, "parent": 20, "type": "test"}, {"id": 133, "parent": 20, "type": "test"},
		{"id": 134, "parent": 20, "type": "test"}, {"id": 135, "parent": 20, "type": "test"}, {"id": 136, "parent": 20, "type": "test"},
		{"id": 137, "parent": 20, "type": None}, {"id": 138, "parent": 20, "type": None}, {"id": 139, "parent": 20, "type": "test"},
		{"id": 140, "parent": 20, "type": "test"}, {"id": 141, "parent": 20, "type": "test"}, {"id": 142, "parent": 20, "type": "test"},
		{"id": 143, "parent": 20, "type": "test"}, {"id": 144, "parent": 20, "type": "test"}, {"id": 145, "parent": 20, "type": "test"},
		{"id": 146, "parent": 20, "type": "test"}, {"id": 147, "parent": 20, "type": None}, {"id": 148, "parent": 20, "type": None},
		{"id": 149, "parent": 20, "type": "test"}, {"id": 150, "parent": 20, "type": "test"}, {"id": 161, "parent": 20, "type": "test"},
		{"id": 162, "parent": 20, "type": "test"}, {"id": 163, "parent": 20, "type": "test"}, {"id": 164, "parent": 20, "type": "test"},
		{"id": 165, "parent": 20, "type": "test"}, {"id": 166, "parent": 20, "type": "test"}, {"id": 167, "parent": 20, "type": None},
		{"id": 168, "parent": 20, "type": None}, {"id": 169, "parent": 20, "type": "test"}, {"id": 170, "parent": 20, "type": "test"},
		{"id": 171, "parent": 20, "type": "test"}, {"id": 172, "parent": 20, "type": "test"}, {"id": 173, "parent": 20, "type": "test"},
		{"id": 174, "parent": 20, "type": "test"}, {"id": 175, "parent": 20, "type": "test"}, {"id": 176, "parent": 20, "type": "test"},
		{"id": 177, "parent": 20, "type": None}, {"id": 178, "parent": 20, "type": None}, {"id": 179, "parent": 20, "type": "test"},
		{"id": 180, "parent": 20, "type": "test"}, {"id": 181, "parent": 20, "type": "test"}, {"id": 182, "parent": 20, "type": "test"},
		{"id": 183, "parent": 20, "type": "test"}, {"id": 184, "parent": 20, "type": "test"}, {"id": 185, "parent": 20, "type": "test"},
		{"id": 186, "parent": 20, "type": "test"}, {"id": 187, "parent": 20, "type": None}, {"id": 188, "parent": 20, "type": None},
		{"id": 189, "parent": 20, "type": "test"}, {"id": 190, "parent": 20, "type": "test"}, {"id": 191, "parent": 20, "type": "test"},
		{"id": 192, "parent": 20, "type": "test"}, {"id": 193, "parent": 20, "type": "test"}, {"id": 194, "parent": 20, "type": "test"},
		{"id": 195, "parent": 20, "type": "test"}, {"id": 196, "parent": 20, "type": "test"}, {"id": 197, "parent": 20, "type": None},
		{"id": 198, "parent": 20, "type": None}, {"id": 199, "parent": 20, "type": "test"}, {"id": 200, "parent": 20, "type": "test"},
		{"id": 200, "parent": 20, "type": "test"}, {"id": 201, "parent": 20, "type": "test"}, {"id": 202, "parent": 20, "type": "test"},
		{"id": 203, "parent": 20, "type": "test"}, {"id": 204, "parent": 20, "type": "test"}, {"id": 205, "parent": 20, "type": "test"},
		{"id": 206, "parent": 20, "type": "test"}, {"id": 207, "parent": 20, "type": None}, {"id": 208, "parent": 20, "type": None},
		{"id": 209, "parent": 20, "type": "test"}, {"id": 210, "parent": 20, "type": "test"}, {"id": 211, "parent": 20, "type": "test"},
		{"id": 212, "parent": 20, "type": "test"}, {"id": 213, "parent": 20, "type": "test"}, {"id": 214, "parent": 20, "type": "test"},
		{"id": 215, "parent": 20, "type": "test"}, {"id": 216, "parent": 20, "type": "test"}, {"id": 217, "parent": 20, "type": None},
		{"id": 218, "parent": 20, "type": None}, {"id": 219, "parent": 20, "type": "test"}, {"id": 220, "parent": 20, "type": "test"},
		{"id": 221, "parent": 20, "type": "test"}, {"id": 222, "parent": 20, "type": "test"}, {"id": 223, "parent": 20, "type": "test"},
		{"id": 224, "parent": 20, "type": "test"}, {"id": 225, "parent": 20, "type": "test"}, {"id": 226, "parent": 20, "type": "test"},
		{"id": 227, "parent": 20, "type": None}, {"id": 228, "parent": 20, "type": None}, {"id": 229, "parent": 20, "type": "test"},
		{"id": 230, "parent": 20, "type": "test"}, {"id": 231, "parent": 20, "type": "test"}, {"id": 232, "parent": 20, "type": "test"},
		{"id": 233, "parent": 20, "type": "test"}, {"id": 234, "parent": 20, "type": "test"}, {"id": 235, "parent": 20, "type": "test"},
		{"id": 236, "parent": 20, "type": "test"}, {"id": 237, "parent": 20, "type": None}, {"id": 238, "parent": 20, "type": None},
		{"id": 239, "parent": 20, "type": "test"}, {"id": 240, "parent": 20, "type": "test"}, {"id": 241, "parent": 20, "type": "test"},
		{"id": 242, "parent": 20, "type": "test"}, {"id": 243, "parent": 20, "type": "test"}, {"id": 244, "parent": 20, "type": "test"},
		{"id": 245, "parent": 20, "type": "test"}, {"id": 246, "parent": 20, "type": "test"}, {"id": 247, "parent": 20, "type": None},
		{"id": 248, "parent": 20, "type": None}, {"id": 249, "parent": 20, "type": "test"}, {"id": 250, "parent": 20, "type": "test"},
		{"id": 261, "parent": 20, "type": "test"}, {"id": 262, "parent": 20, "type": "test"}, {"id": 263, "parent": 20, "type": "test"},
		{"id": 264, "parent": 20, "type": "test"}, {"id": 265, "parent": 20, "type": "test"}, {"id": 266, "parent": 20, "type": "test"},
		{"id": 267, "parent": 20, "type": None}, {"id": 268, "parent": 20, "type": None}, {"id": 269, "parent": 20, "type": "test"},
		{"id": 270, "parent": 20, "type": "test"}, {"id": 271, "parent": 20, "type": "test"}, {"id": 272, "parent": 20, "type": "test"},
		{"id": 273, "parent": 20, "type": "test"}, {"id": 274, "parent": 20, "type": "test"}, {"id": 275, "parent": 20, "type": "test"},
		{"id": 276, "parent": 20, "type": "test"}, {"id": 277, "parent": 20, "type": None}, {"id": 278, "parent": 20, "type": None},
		{"id": 279, "parent": 20, "type": "test"}, {"id": 280, "parent": 20, "type": "test"}, {"id": 281, "parent": 20, "type": "test"},
		{"id": 282, "parent": 20, "type": "test"}, {"id": 283, "parent": 20, "type": "test"}, {"id": 284, "parent": 20, "type": "test"},
		{"id": 285, "parent": 20, "type": "test"}, {"id": 286, "parent": 20, "type": "test"}, {"id": 287, "parent": 20, "type": None},
		{"id": 288, "parent": 20, "type": None}, {"id": 289, "parent": 20, "type": "test"}, {"id": 290, "parent": 20, "type": "test"},
		{"id": 291, "parent": 20, "type": "test"}, {"id": 292, "parent": 20, "type": "test"}, {"id": 293, "parent": 20, "type": "test"},
		{"id": 294, "parent": 20, "type": "test"}, {"id": 295, "parent": 20, "type": "test"}, {"id": 296, "parent": 20, "type": "test"},
		{"id": 297, "parent": 20, "type": None}, {"id": 298, "parent": 20, "type": None}, {"id": 299, "parent": 20, "type": "test"}
	]
	
	# Init [t1] -> optimized TreeStoree Class
	t1 = t_optimized.TreeStore(items)

	# Init [t2] -> NOT optimized TreeStoree Class
	t2 = t_std.Test(items)

	# Testing GET_ALL

	t_optimized.print_custom('Get ALL method TEST: 400.000 times', 'yellow')

	result = timeit.timeit(lambda: t1._getAll(), number=200000)
	t_optimized.print_custom(result, 'test1')
	# ------------------------------------------------------------------------- #
	result = timeit.timeit(lambda: t2._getAll_TEST(), number=200000)
	t_optimized.print_custom(result, 'test2')

	# Testing GET_ITEM

	t_optimized.print_custom('Get Item method TEST: 400.000 times', 'yellow')

	result = timeit.timeit(lambda: t1._getItem(47), number=200000)
	t_optimized.print_custom(result, 'test1')
	# ------------------------------------------------------------------------- #
	result = timeit.timeit(lambda: t2._getItem_TEST(47), number=200000)
	t_optimized.print_custom(result, 'test2')

	# Testing GET_CHILDREN

	t_optimized.print_custom('Get Children TEST: 400.000 times', 'yellow')

	result = timeit.timeit(lambda: t1._getChildren(20), number=200000)
	t_optimized.print_custom(result, 'test1')
	# ------------------------------------------------------------------------- #
	result = timeit.timeit(lambda: t2._getChildren_TEST(20), number=200000)
	t_optimized.print_custom(result, 'test2')

	# Testing GET_ALL_PARENTS
	
	t_optimized.print_custom('Get ALL Parents TEST: 400.000 times', 'yellow')

	result = timeit.timeit(lambda: t1._getAllParents(96), number=200000)
	t_optimized.print_custom(result, 'test1')
	# ------------------------------------------------------------------------- #
	result = timeit.timeit(lambda: t2._getAllParents_TEST(96), number=200000)
	t_optimized.print_custom(result, 'test2')
