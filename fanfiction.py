import csv

titles = []
title_tags = {}
title_contents = []
tags = []
likes = []
comments = []
texts = []
words_per_sentence = []
genres = []


end_sentence = ['。', '！', '？', '”', '……']

# a list of characters and their nicknames generated from the name list/personal experience. But this has some problems:
# the name tradition makes it hard to automatically separate first names and last names.
# some fans has other nicknames they prefer to use to call those characters
# different translation for some of the characters
# the characters used in the names may refer to other things in a normal context
# the hero names have different version as well
characters = ['绿谷出久', '爆豪胜己', '丽日御茶子', '饭田天哉', '轰焦冻', '蛙吹梅雨', '丰田实',
              '切岛锐儿郎', '八百万百', '常暗踏阴', '上鸣电气', '青山优雅', '耳郎响香', '芦户三奈',
              '障子目藏', '尾白猿夫', '濑吕范太', '叶隐透', '砂藤力道', '口田甲司', '物间宁人',
              '拳藤一佳', '通行百万', '天喰环', '波动螺卷', '心操人使', '欧尔麦特', '相泽消太', 
              '安德瓦', '格兰特里诺', '潮爆牛王', '死柄木弔', '黑雾', '荼毘', '渡我被身子',
              '治崎廻','绿谷', '出久', '小久', '臭久', '爆豪', '胜己', '小胜', '榴莲头', 
              '丽日', '御茶子','饭田', '轰', '焦冻','阴阳脸', '蛙吹', '梅雨', '切岛', '八百万', 
              '常暗', '踏阴', '上鸣', '电电', '耳郎', '尾白', '物间', '宁人', '天喰', '心操', 
              '人使', '相泽', '三三', '消太', '死柄木', '弔', '渡我',
              '木偶', '绿谷少年', '爆杀', '爆心', '轻灵', '天哉', '葡萄', '月咏', 'Eraser', 
              '八木俊典', '八木', '俊典', '轰炎司', '轰冷', '死柄木吊',
              '少女','小鬼', 'xx', '臭女人', '蠢女人'] 
              
# Secetal instances of cross-cultural translation/ingetration
culturals = ['君', '酱', '三三', '同学']

# open the corpus and get the data for analysis 
with open ('meta_data.csv') as file:
    reader = csv.reader(file, delimiter = ',')
    for row in reader:
        titles.append(row[0])
        tags.append(row[2])
        likes.append(row[3])
        comments.append(row[4])
        texts.append(row[-2])
        genres.append(row[-1])

# count the number of likes, comments
def count(data, remove_item):
    data.remove(remove_item)
    data_numbers = [int(str(item)) for item in data]
    return(data_numbers)

# count the number of each tag in tags and genre in genres
def process(data, remove_item):
    data.remove(remove_item)
    item_count = {}
    for item in data:
        single_item = item.strip().split('/')
        for item in single_item:
            if item in item_count:
                item_count[item] += 1
            else:
                item_count[item] = 1
    return(item_count)

# count the number of characters & cross_cultural elements
def count_instance(data):
    item_count = {}
    for item in data:
        for text in texts:
            if item in text:
                if item in item_count:
                    item_count[item] += 1
                else:
                    item_count[item] = 1
    print(item_count)

# number of likes
like_numbers = count(likes, 'likes')
print('The max number of likes is %s, the min is %s.' 
    % (max(like_numbers), min(like_numbers)))

# number of comments
comment_numbers = count(comments, 'number of comments')
print('The max number of comments is %s, the min is %s.' 
    % (max(comment_numbers), min(comment_numbers)))

# tags
tags_count = process(tags, 'extra tags')
print(tags_count, len(tags_count))

# titles
titles.remove('title')
for title in titles:
    title = title.split('】')
    if title[0] in title_tags:
        title_tags[title[0]] += 1
    else:
        title_tags[title[0]] = 1
    title_contents.append(title[-1])
print(title_tags)

# genres
genres_count = process(genres, 'genre')
print(genres_count)


# texts
texts.remove('texts')

# how many characters and their frequency
character_count = count_instance(characters)


# text - total length 
text_length = [len(text) for text in texts]
print('The max length of the text is %s, the min is %s.' 
    % (max(text_length), min(text_length)))

# text - words per sentence
for text in texts:
    sentence_count = 0
    for place, letter in enumerate(text):
        try:
            if letter in end_sentence and text[place + 1] not in end_sentence:
                sentence_count += 1 
        except IndexError:
            sentence_count += 1  
    words_per_sentence.append(round(len(text)/sentence_count,2))

print('The max length of a sentence is %s, the min is %s.' 
    % (max(words_per_sentence), min(words_per_sentence)))

# cross-cultrual aspect
cultruals_count = count_instance(culturals)