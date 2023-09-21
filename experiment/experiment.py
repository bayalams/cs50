result_list = [1, 2, 3, 4, 5]
user_input = input("result: ")
user_input_list = []
user_input_list.append(user_input)
score_list = []


while len(user_input_list) != 5:
    for user_input in user_input_list:
            for result in result_list:
                if user_input == result:
                    score_list.append(user_input)