def create_cook_book() -> dict:
    """Description:
    This function reads recipes from a file named "recipes.txt" and creates
    a dictionary named cook_book where the keys are dish names and the values are lists of
    dictionaries, each representing an ingredient with its corresponding quantity and measure.
    The function returns the created cook_book dictionary.
    Input: No parameters.
    Output: A dictionary (cook_book) containing the recipes parsed from the "recipes.txt" file."""
    cook_book = {}
    f = open('recipes.txt', 'r')
    cook_book_raw = f.readlines()
    book_length = len(cook_book_raw)
    for i_, line in enumerate(cook_book_raw):
        line = line.strip()
        if line.isnumeric():
            #it is ingredients count
            cook_book[cook_book_raw[i_-1].strip()] = get_dish_descr(i_ - 1, int(line), cook_book_raw)
    f.close()
    return cook_book

def get_dish_descr(start_line_nr, ingr_count, book_raw) -> list:
    """
    Description:
    This function is a helper function used within the create_cook_book function.
    It retrieves the ingredients for a dish starting from the specified line number
    (start_line_nr) in the book_raw list. It then constructs a list of dictionaries,
    each representing an ingredient with its corresponding name, quantity, and measure
    for the dish.
    Input:
    start_line_nr (int): The line number where the dish's ingredients start.
    ingr_count (int): The number of ingredients for the dish.
    book_raw (list): The list of lines from the recipes file.
    Output: A list of dictionaries representing the ingredients for the dish.
    """
    ingredients = []
    for ii_ in range(ingr_count):
        ingredient = book_raw[start_line_nr + ii_ + 2].strip().split('|')
        temp_str = ''
        for i_, item in enumerate(ingredient):
            if i_ == 0:
                ingredient_name = item
            elif i_ == 1:
                quantity = item
            elif i_ == 2:
                measure = item
        ingredient_dict = {"ingredient_name": ingredient_name, "quantity": quantity, "measure": measure}
        ingredients.append(ingredient_dict)
    return ingredients

def get_shop_list_by_dishes(dishes, person_count) -> dict:
    """
    Description: This function creates a shopping list based on a list of dishes and a specified
    number of people. It retrieves the recipes from the cook book and calculates the required
    quantities of each ingredient based on the number of people. The function returns a
    dictionary (shop_list) where the keys are ingredient names, and the values are dictionaries
    containing the required quantity and measure for each ingredient.
    Input:
    dishes (list): A list of dish names.
    person_count (int): The number of people for whom the shopping list is being created.
    Output: A dictionary (shop_list) representing the required shopping list for the specified dishes and number of people.
    """
    shop_list ={}
    for c_dish in dishes:
        dish_recipe = create_cook_book().get(c_dish)
        if dish_recipe != None:
            for each_ingr in dish_recipe:
                if shop_list.get(each_ingr['ingredient_name']) == None:
                    shop_list[each_ingr['ingredient_name']] = {'measure': each_ingr['measure'], 'quantity': int(each_ingr['quantity']) * person_count}
                else:
                    previous_qnty = int(shop_list.get(each_ingr['ingredient_name']).get('quantity'))
                    shop_list[each_ingr['ingredient_name']] = {'measure': each_ingr['measure'], 'quantity': int(each_ingr['quantity']) * person_count + previous_qnty}
        else:
            print("Блюдо отсутствует в книге")
            return
    # print(shop_list)
    return shop_list

def files_routine():
    """
    Description: This function performs routine operations on multiple text files
    (1.txt, 2.txt, and 3.txt). It reads each file, appends specific information
    to a new file called "result.txt", and appends the contents of the corresponding
    file. The function also sorts the files based on the number of lines and appends
    the file's information in sorted order to "result.txt".
    Input: No parameters.
    Output: The function does not return any value, but it performs file operations as described.
    """
    files = []
    files_len = []
    for i_ in range(1, 4):
        f = open(str(i_) + '.txt', 'r')
        files.append(i_)
        files_len.append(len(f.readlines()))
        f.close()
    files_stats = list(zip(files_len, files))
    files_stats.sort()
    for i_, file_info in enumerate(files_stats):
        f = open(str(files_stats[i_][1]) + '.txt', 'r')
        f_wr = open('result.txt', 'a')
        f_wr.write(str(files_stats[i_][1]) + '.txt' + '\n' + str(i_ + 1) + '\n')
        list_from_file = f.readlines()
        for each_line in list_from_file:
            f_wr.write(each_line)
        if each_line[-1] != '\n':
            f_wr.write('\n')




print(create_cook_book())
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
files_routine()