import re

text = '\nRusty → Firepaw → Fireheart → Firestar\n\n\n'
print(text)
words = re.findall(r'\b\w+\b', text)
words = [word for word in words if word != 'n']  # Exclude 'n' from the list
# print(len(words))
# print(words)
# ua_names = words[1:]

uk_names = words
print(ua_names)
print(uk_names)

length_difference = len(ua_names) - len(uk_names)
match length_difference:
    case -1:
        print('ua names array is shorter than uk')
    case 1:
        print('ua names array is longer than uk')
    case _:
        length_difference
# import pandas as pd
#
# # List with two elements
# my_list = ['Медя → Медолапка → Медозела', 'Кошеня → Вчениця → Воїн']
#
# # Create an empty DataFrame
# df = pd.DataFrame(columns=['kitten_ua', 'apprentice_ua', 'warrior_ua', 'kitten_uk', 'apprentice_uk', 'warrior_uk'])
#
# # Iterate over the list elements and split the values
# # for element in my_list:
# split_data = my_list[0].split(' → ')
# second_element_split = my_list[1].split(' → ')
# for i in range(len(second_element_split)):
#     split_data.append(second_element_split[i])
#
#
# row = {col: split_data[i] if i < len(split_data) else '' for i, col in enumerate(df.columns)}
# df = df._append(row, ignore_index=True)
# print(df)
