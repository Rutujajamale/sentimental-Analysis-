import string

# importing counter from collection module to count the number of emotions
from collections import Counter

#import matplotlib to draw the graph
import matplotlib.pyplot as plt

#opening t.txt inopen mode
text=open('t.txt',encoding='utf_8').read()
# conerting into lower case
lower_case=text.lower()
#removing punctuations
clean_text=lower_case.translate(str.maketrans('','',string.punctuation))
# breaking sentence into words
token_text=clean_text.split()
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
final_list=[]
for word in token_text:
    if word not in stop_words:
        final_list.append(word)

#create empty list to store emotion only which are present in given text 

emotion_list=[]
with open('emotions.txt', 'r') as file:
    for line in file:
        #clear line means remove line , and ' and space in starting 
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        # variable_1,variable_2 = value fro variable 1,value fro variable 2
        #split() it is use to break the sentence into words
        word, emotion = clear_line.split(':')
        # print("Words: "+word+"  "+"Emotions: "+emotion)

        if word in final_list:
            emotion_list.append(word)

# print(emotion_list)
#count the emotion which are given in the paragraph

x=Counter(emotion_list)
# print(x)

#drawing graph
fig, ax1 = plt.subplots()
#it will draw the axis 
ax1.bar(x.keys(), x.values())
# it will automate the axis update
fig.autofmt_xdate()
#save the graph
plt.savefig('graph.png')
#display the graph
plt.show()
