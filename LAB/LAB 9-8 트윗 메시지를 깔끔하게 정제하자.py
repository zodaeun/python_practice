import re

tweet = input("트윗을 입력하시오: ")

tweet = re.sub('RT', '', tweet)
tweet = re.sub('@\S+', '', tweet)
tweet = re.sub('#\S+', '', tweet)
tweet = re.sub('@\S+', '', tweet)

print(tweet)
