# { %
# for quote in all_quotes %}
# < h4 > {{quote.quote}} < / h4 >
# < h4 > {{quote.pk}} < / h4 >
# < a
# href = "{% url 'apage:author_detail' quote.pk %}" > < h5 > {{quote.author.author_name}} < / h5 > < / a >
# < h5 > Tags: {{quote.tag}}, Followers: {{quote.author.followers}}, Like
# {{quote.is_liked}} < / h5 >
# < a
# href = "#" > < h5 > Comment! < / h5 > < / a >
# < form
# action = "" >
# { % if quote.is_liked %}
# < img
# src = "@"
# alt = "liked" / >
# < button
# type = "submit"
# name = "favorite"
# value = "{{ quote.id }}" > DisLike < / button >
# { % else %}
# < img
# src = "#"
# alt = "disliked" / >
# < button
# type = "submit"
# name = "favorite"
# value = "{{ quote.id }}" > Like < / button >
# { % endif %}
# < / form >
