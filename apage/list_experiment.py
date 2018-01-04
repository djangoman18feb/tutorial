# # #This little program removes any string in a list from any list containing it..
# # #from .jsonToDict_Converter import json_To_database_Conv
# #
# # #json_To_database_Conv(r'C:\Users\deepak\Desktop\Scrape_projects\New_Project_Tdy\gdr_upto_49p.json')
# #
# main_list = ["\n      ", "\n", " Oscar Wilde ", "attributed-no-source", "be-yourself", "honesty", "inspirational", "misattributed-oscar-wilde", "135649 likes", "Like"]
# look_up_list = ['\n', '―\n', 'Oscar Wilde', 'Like', 'attributed-no-source']
# empty_list = []
# for i in range(len(main_list)):
#     content = main_list[i]
#     content = content.strip(' ')
#     empty_list.append(content)
# main_list=empty_list
# for item in range(len(look_up_list)):
#     str_to_rm = look_up_list[item]
#     ocurrance_no = main_list.count(str(str_to_rm))
#     for i in range(ocurrance_no):
#         main_list.remove(str_to_rm)
#         i+=1
#
# print(empty_list)
#
#
#
# # #
# # # #--------------
# # # #below code is working fine
# # # import json
# # # #from .models import Quote, Author
# # #
# # # def json_To_database_Conv(path):
# # #     with open(path) as data_file:
# # #         data = json.load(data_file) #data is a list of dictionary
# # #         for i in range(len(data)):
# # #             f_dict_data = data[i]
# # #             #print(f_dict_data)
# # #             quote = f_dict_data['q_text'] #a list of sting
# # #             main_list = quote
# # #             look_up_list = ['\n', '―\n']
# # #             empty_list = []
# # #             for i in range(len(main_list)):
# # #                 content = main_list[i]
# # #                 content = content.strip(' ')
# # #                 empty_list.append(content)
# # #
# # #             main_list = empty_list
# # #             #print(main_list)
# # #             for item in range(len(look_up_list)):
# # #                 str_to_rm = look_up_list[item]
# # #                 ocurrance_no = main_list.count(str(str_to_rm))
# # #                 for i in range(ocurrance_no):
# # #                     main_list.remove(str_to_rm)
# # #                     i += 1
# # #                 print(main_list)
# # #
# # #             #tags = f_dict_data['q_text_tags'] #a list of strings
# # #             #author = f_dict_data['q_Author_name'] #a list of string
# # #
# # #
# # #             #print(tags)
# # #             #print(author)
# # #             #data-->filter data(tags, quote, author_name)-->tags
# # #         #tags
# # #         #author_name
# # #
# # # json_To_database_Conv(r'C:\Users\deepak\Desktop\Scrape_projects\New_Project_Tdy\gdr_upto_49p.json')
# # #
# # tag_li = ['\n', '\n', '  J.R.R. Tolkien   ', '  J.R.R. Tolkien   ', 'The Two Towers', 'hope', 'optimism', '7667 likes', 'Like']
# # for tag in tag_li:
# #     if tag.strip()=='' or tag.strip()=='J.R.R. Tolkien':
# #         print(tag)
# #         tag_li.remove(tag)
# #
# #
# # print(tag_li)
# #
# # # string = '       \n       '
# # # print(string.strip())

import json
def home_data_view():
    with open(r'C:\Users\deepak\Desktop\Django_projects\tutorial_max\tutorial\apage\quotes_json_data.json') as data_file:
        data = json.load(data_file)  # data is a list of dictionary
        for i in range(len(data)):
            f_dict_data = data[i]
            quote = f_dict_data['q_text']  # a list of sting
            tags_li = f_dict_data['q_text_tags']
            author = f_dict_data['q_Author_name']
            info_li = [quote, tags_li]
            for content in info_li:
                main_list = content
                look_up_list = ['\n', '―\n', 'Like', 'attributed-no-source', author[0]]
                empty_list = []
                for i in range(len(main_list)):
                    content = main_list[i]
                    content = content.strip(' ')
                    empty_list.append(content)
                main_list = empty_list
                for item in range(len(look_up_list)):
                    str_to_rm = look_up_list[item]
                    ocurrance_no = main_list.count(str(str_to_rm))
                    for i in range(ocurrance_no):
                        main_list.remove(str_to_rm)
                        i += 1
                print(empty_list)
home_data_view()