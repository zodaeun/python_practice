t = '[ARTICLE] 200820 BLACKPINK Jennie is regarded to have great effect on KT Mystic Red as it was chosen by 50% of those who prebooked for the Samsung Galaxy Note 20 (LG U+ Mystic Pink 30%, SKT Mystic Blue not disclosed) '


tReplace = t.replace('KT','*').replace('Samsung','*').replace('LG','*').replace('SKT','*')

print(tReplace)
