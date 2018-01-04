import json
from apage.models import Quote, Author

def json_To_database_Conv(path):
    with open(path) as data_file:
        data = json.load(data_file) #data is a list of dictionary
        #print(len(data))
        for i in range(len(data)):
            f_dict_data = data[i]
            #print(f_dict_data)
            quote = f_dict_data['q_text'] #a list of sting
            tags = f_dict_data['q_text_tags']
            author = f_dict_data['q_Author_name']
            info_list = [quote,]
            for i in info_list:
                main_list = i
                look_up_list = ['\n', '―\n']
                empty_list = []
                for i in range(len(main_list)):
                    content = main_list[i]
                    content = content.strip(' ')
                    empty_list.append(content)

                main_list = empty_list
                #print(main_list)
                for item in range(len(look_up_list)):
                    str_to_rm = look_up_list[item]
                    ocurrance_no = main_list.count(str(str_to_rm))
                    for i in range(ocurrance_no):
                        main_list.remove(str_to_rm)
                        i += 1
                    a = Quote(quote=main_list, )
                    a.save()



                    #tags = f_dict_data['q_text_tags'] #a list of strings
            #author = f_dict_data['q_Author_name'] #a list of string


            #print(tags)
            #print(author)
            #data-->filter data(tags, quote, author_name)-->tags
        #tags
        #author_name

json_To_database_Conv(r'C:\Users\deepak\Desktop\Django_projects\tutorial_max\tutorial\apage\quotes_json_data.json')