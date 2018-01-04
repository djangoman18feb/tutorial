import json
from django.shortcuts import render, HttpResponse
from apage.models import Quote, Author


# Create your views here.

def home_data_view(request):
    with open(
            r'C:\Users\deepak\Desktop\Django_projects\tutorial_max\tutorial\apage\quotes_json_data.json') as data_file:
        data = json.load(data_file)  # data is a list of dictionary

        print(len(data))
        for i in range(len(data)):
            f_dict_data = data[i]
            quote = f_dict_data['q_text']  # a list of sting
            # tags = f_dict_data['q_text_tags']
            # author = f_dict_data['q_Author_name']

            #info_list = [quote, ]
                        #for i in info_list:
            main_list = func1(main_list=quote, look_up_list=['\n', '―\n', 'Like', 'attributed-no-source'])
            print(main_list[0])
            a = Quote(quote=main_list[0], )
            a.save()
    all_quotes = Quote.objects.all()
    context = {'all_quotes': all_quotes}
    return render(request, template_name='data_home.html', context=context)

def func1(main_list, look_up_list):
    main_list = main_list
    look_up_list = look_up_list
    empty_list = []
    for i in range(len(main_list)):
        content = main_list[i]
        content = content.strip(' ')
        empty_list.append(content)

    main_list = empty_list
    # print(main_list)
    for item in range(len(look_up_list)):
        str_to_rm = look_up_list[item]
        ocurrance_no = main_list.count(str(str_to_rm))
        for i in range(ocurrance_no):
            main_list.remove(str_to_rm)
            i += 1
    return main_list