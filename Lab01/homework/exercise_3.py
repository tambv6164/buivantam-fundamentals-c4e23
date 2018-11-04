from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
db = client.get_database()

posts = db["posts"]

new_post = {
    "title": "Đây là tiêu đề",
    "author": "Bùi Văn Tâm",
    "content": "Phần này là một đoạn văn bản thôi cũng không có gì cả đâu vì mình chỉ viết để\
    làm mẫu cho phần content của post này nên mình không viết gì quá dài dòng cả nếu bạn đọc đến đây\
    có lẽ bạn đã hiểu mình đang viết gì dồi đúng không vậy thì xin cảm ơn bạn nhiều vì đã theo dõi"
}

posts.insert_one(new_post)

client.close()