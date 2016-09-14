"""Paul Fordham | ptf06c """
#!/user/bin/env python
from __future__ import print_function # print()
import requests
import re
import json

class Comment:
    def __init__(self, num):
        self.hash = None
        self.title = None
        self.points = 0
        self.time = None
        self.comment_num = num

    def __str__(self):
        return str(self.comment_num) + ". " + self.hash + "\n" + "Points: " + str(self.points) + "\n" + "Title: " + self.title + "\n" + "Date: " + self.time + "\n"

print("Enter username: ", end='')
user = raw_input()

hasContent = None
userExists = True

url = "http://www.imgur.com/user/" + user
user_page = requests.get(url)

hasContent = re.findall(".*", user_page.text)
if hasContent[0] == '':
    userExists = False

if user_page and userExists:
    page_num = 0
    hasContent = None
    moreComments = True

    comment1 = Comment(1)
    comment2 = Comment(2)
    comment3 = Comment(3)
    comment4 = Comment(4)
    comment5 = Comment(5)

    while(moreComments):
        curl = "http://imgur.com/user/" + user + "/index/newest/page/" + str(page_num) + "/hit.json?scrolling"
        comments_page = requests.get(curl)
        hasContent = re.findall(".*", comments_page.text)
        if hasContent[0] == '':
            break
        
        user_comment_json = json.loads(comments_page.text)
        comment = user_comment_json["data"]["captions"]["data"]

        for data in comment:
            if data["points"] >= comment1.points:
                comment5.hash = comment4.hash
                comment5.title = comment4.title
                comment5.points = comment4.points
                comment5.time = comment4.time

                comment4.hash = comment3.hash
                comment4.title = comment3.title
                comment4.points = comment3.points
                comment4.time = comment3.time
                
                comment3.hash = comment2.hash
                comment3.title = comment2.title
                comment3.points = comment2.points
                comment3.time = comment2.time
               
                comment2.hash = comment1.hash
                comment2.title = comment1.title
                comment2.points = comment1.points
                comment2.time = comment1.time
 
                comment1.hash = data["hash"]
                comment1.title = data["title"]
                comment1.points = data["points"]
                comment1.time = data["datetime"]
            elif data["points"] > comment2.points:
                comment5.hash = comment4.hash
                comment5.title = comment4.title
                comment5.points = comment4.points
                comment5.time = comment4.time
                
                comment4.hash = comment3.hash
                comment4.title = comment3.title
                comment4.points = comment3.points
                comment4.time = comment3.time
                
                comment3.hash = comment2.hash
                comment3.title = comment2.title
                comment3.points = comment2.points
                comment3.time = comment2.time

                comment2.hash = data["hash"]
                comment2.title = data["title"]
                comment2.points = data["points"]
                comment2.time = data["datetime"]
            elif data["points"] > comment3.points:
                comment5.hash = comment4.hash
                comment5.title = comment4.title
                comment5.points = comment4.points
                comment5.time = comment4.time
                
                comment4.hash = comment3.hash
                comment4.title = comment3.title
                comment4.points = comment3.points
                comment4.time = comment3.time

                comment3.hash = data["hash"]
                comment3.title = data["title"]
                comment3.points = data["points"]
                comment3.time = data["datetime"]
            elif data["points"] > comment4.points:
		comment5.hash = comment4.hash
                comment5.title = comment4.title
                comment5.points = comment4.points
                comment5.time = comment4.time
                
                comment4.hash = data["hash"]
                comment4.title = data["title"]
                comment4.points = data["points"]
                comment4.time = data["datetime"]
            elif data["points"] > comment5.points:
                comment5.hash = data["hash"]
                comment5.title = data["title"]
                comment5.points = data["points"]
                comment5.time = data["datetime"]
        page_num += 1

    # no more comments print top 5
    if not comment1.points == 0:
        temp = Comment(0)
        if comment1.points == comment2.points:
            if comment2.hash > comment1.hash:
                temp.hash = comment1.hash
                temp.title = comment1.title
                temp.points = comment1.points
                temp.time = comment1.time
     
                comment1.hash = comment2.hash
                comment1.title = comment2.title
                comment1.points = comment2.points
                comment1.time = comment2.time
             
                comment2.hash = comment1.hash
                comment2.title = comment1.title
                comment2.points = comment1.points
                comment2.time = comment1.time
        if comment2.points == comment3.points:
            if comment3.hash > comment2.hash:
                temp.hash = comment2.hash
                temp.title = comment2.title
                temp.points = comment2.points
                temp.time = comment2.time
     
                comment2.hash = comment3.hash
                comment2.title = comment3.title
                comment2.points = comment3.points
                comment2.time = comment3.time
             
                comment3.hash = temp.hash
                comment3.title = temp.title
                comment3.points = temp.points
                comment3.time = temp.time
        if comment3.points == comment4.points:
            if comment4.hash > comment3.hash:
                temp.hash = comment3.hash
                temp.title = comment3.title
                temp.points = comment3.points
                temp.time = comment3.time
     
                comment3.hash = comment4.hash
                comment3.title = comment4.title
                comment3.points = comment4.points
                comment3.time = comment4.time
             
                comment4.hash = temp.hash
                comment4.title = temp.title
                comment4.points = temp.points
                comment4.time = temp.time
        if comment4.points == comment5.points:
            if comment5.hash > comment4.hash:
                temp.hash = comment4.hash
                temp.title = comment4.title
                temp.points = comment4.points
                temp.time = comment4.time
     
                comment4.hash = comment5.hash
                comment4.title = comment5.title
                comment4.points = comment5.points
                comment4.time = comment5.time
             
                comment5.hash = temp.hash
                comment5.title = temp.title
                comment5.points = temp.points
                comment5.time = temp.time
        print(comment1)
        print(comment2)
        print(comment3)
        print(comment4)
        print(comment5)
    else:
        print("User has no comments!")
else:
    print("User not found!")
