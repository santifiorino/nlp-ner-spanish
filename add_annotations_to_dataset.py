# load annotations.json and convert to csv file
# output dataset2.csv

import json
import os
import pandas as pd

def main():
    if os.path.exists('dataset.csv'):
        df = pd.read_csv('dataset.csv')
        chat_num = df['Chat #'].max() + 1
        sentence_num = df['Sentence #'].max() + 1
    else:
        df = pd.DataFrame(columns=['Chat #', 'Sentence #', 'Word', 'Tag'])
        chat_num = 0
        sentence_num = 0

    with open('annotations.json', encoding='utf-8') as f:
        data = json.load(f)

    for tuple in data["annotations"]:
        sentence = tuple[0][:-1]
        words = sentence.split()
        words_lens = [len(word) for word in words]
        words_spans = []
        start = 0
        for word_len in words_lens:
            words_spans.append((start, start+word_len))
            start += word_len + 1
        entities = tuple[1]["entities"]
        all_entities = ["O"] * len(words)
        for entity in entities:
            entity_start = entity[0]
            entity_end = entity[1]
            entity_type = entity[2]
            for i in range(len(words_spans)):
                if abs(entity_start - words_spans[i][0]) <= 1 and abs(entity_end - words_spans[i][1]) <= 1:
                    all_entities[i] = entity_type
                    break
        for i in range(len(words)):
            words[i] = words[i].strip('.,;:¿?! ')
        for i in range(len(words)):
            df = df.append({'Chat #': chat_num, 'Sentence #': sentence_num, 'Word': words[i], 'Tag': all_entities[i]}, ignore_index=True)
        sentence_num += 1

    df.to_csv('dataset.csv', index=False)
                
if __name__ == '__main__':
    main()

