import os
os.system("python3 hindu_api.py")
print("<<<  Data On LocalHost by API >>>")
os.system("python3 image_create.py")
print("<<<  Created Image Files and Ready to Uploade via Tweepy Developer API >>>")
os.system("python3 twitter_con.py")
print("<<< All the Images has Been Successfully Uploaded. >>>")
