import fbchat
import re
fbchat._util.USER_AGENTS    = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"]
# fbchat._state.FB_DTSG_REGEX = re.compile(r'"name":"fb_dtsg","value":"(.*?)"')
from getpass import getpass 
username = str(input("Username: ")) 
client = fbchat.Client(username, getpass()) 
no_of_friends = int(input("Number of friends: ")) 

for i in range(no_of_friends): 
    name = str(input("Name: ")) 
    friends = client.searchForUsers(name) # return a list of names 
    friend = friends[0] 
    msg = str(input("Message: ")) 
    sent = client.send(fbchat.models.Message( msg), thread_id = int(friend.uid)) 
    if sent: 
        print("Message sent successfully!") 