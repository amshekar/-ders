import nltk, string
import os,operator
from collections import OrderedDict
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('punkt')
stemmer = nltk.stem.SnowballStemmer("english")
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]


def matcher(description):
    matchScores = dict()
    jd_text = description
    profiles_path = "C:\Users\Venkata_Narajarla\Desktop\pyders-hackathon\src\cvs"
    for pr in os.listdir(profiles_path):
        pr_text = open(profiles_path+'/'+pr, 'r').read()
        match = cosine_sim(jd_text, pr_text)
        matchScores.__setitem__(pr,match)
        # print("match between job description: " + str(jd) + " and profile: " + str(pr) + " is "+ str(match))
    print(type(matchScores))
    print(matchScores)

    d = OrderedDict((sorted(matchScores.items(), key=operator.itemgetter(1))))
    reversedMatchScores = OrderedDict()
    for k in reversed(d):
        reversedMatchScores[k] = d[k]

    print(reversedMatchScores)
    return reversedMatchScores
    # return inv_map
# matcher('desired_profiles','profiles')