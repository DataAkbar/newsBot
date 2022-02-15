# url = "https://www.securitylab.ru/news/529313.php"

# article_id = url.split("/")[-1]
# article_id = article_id[:-4]
# print(article_id)

# import json

# with open("news_dict.json") as file:
#     news_dict = json.load(file)

# search_id = "5293428234"

# if search_id in news_dict:
#     print("Yangiliklar lug'atta bo'r")
# else:
#     print("yangi yangilik, lug'atga qo'shish kerak!")


"""binary_search"""

def binary_search(list, item):
    """BINARY SEARCH"""
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid + 1
    return None

my_list = [1,2,3,4,5,6,7,88,9,10,11,12,13,14,15,16]

print(binary_search(my_list, 2)) # => 1



