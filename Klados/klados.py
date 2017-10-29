
import os
import nltk
from nltk.probability import FreqDist

import string






default_stopwords = set(nltk.corpus.stopwords.words('english'))

path = 'D:\\data\\writing20170708'

file_count = 0

# freq = FreqDist('abbb') + FreqDist('bcc')
# for word, frequencey in freq.most_common(100):
#     print(word, end=' ')
#     print(frequencey)


master_freq = FreqDist()
for root, dirs, file_names in os.walk(path):
    #path = root.split(os.sep)
    #print(os.path.basename(root))
    for file_name in file_names:
        file_path = root + os.sep + file_name
        if file_name.find('.') == -1 or file_name.endswith('.txt'):
            try:
                # file = open(file_path, 'r', encoding='utf8')
                file = open(file_path, 'r', encoding="ISO-8859-1")
                file_text = file.read()
                file_text = file_text.translate(str.maketrans('', '', string.punctuation))
                words = nltk.word_tokenize(file_text)

                #words = [word for word in words if len(word) > 2]
                words = [word for word in words if not word.isnumeric()]
                words = [word.lower() for word in words]
                words = [word for word in words if word not in default_stopwords]
                fdist = FreqDist(words)
                master_freq += fdist
            except Exception as ex:
                print('error loading '+file_path + ': ' +str(ex))
            finally:
                file.close()
                file_count += 1
                if file_count%100 == 0:
                    print(f'files processed: {file_count}')
        else:
            print(f'skipping {file_path}')


for word, frequency in master_freq.most_common(50):
    print(f'{word} {frequency}')
