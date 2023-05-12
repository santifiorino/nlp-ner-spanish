import sys
import spacy
import random
import numpy as np
import pandas as pd
from spacy.training import Example

def format_dataframe_to_spacy(df):
    res = []
    for i, data in df.groupby('Sentence #'):
        sentence_words_list = data['Word'].values.tolist()
        sentence_words_lens = [len(word) for word in sentence_words_list]
        sentence = ' '.join(sentence_words_list)
        tag_list = data['Tag'].values.tolist()
        start_end_tag = []
        for j, tag in enumerate(tag_list):
            if tag != 'O':
                start = sum(sentence_words_lens[:j]) + j
                end = start + sentence_words_lens[j]
                start_end_tag.append((start, end, tag))
        res.append((sentence, start_end_tag))
    return res

def create_spacy_model(labels):
    nlp = spacy.blank('es')
    ner = nlp.add_pipe('ner')
    for label in labels:
        ner.add_label(label)
    return nlp

def train_model(nlp, train_data, iterations):
    optimizer = nlp.begin_training()
    for itn in range(iterations):
        random.shuffle(train_data)
        for raw_text, entity_offsets in train_data:
            doc = nlp.make_doc(raw_text)
            example = Example.from_dict(doc, {"entities": entity_offsets})
            nlp.update([example], sgd=optimizer)
    
def main():
    if len(sys.argv) != 3:
        print("Usage: python train.py dataset_file.csv iterations")
        sys.exit(1)
    dataset_file = sys.argv[1]
    iterations = int(sys.argv[2])
    # Load dataset
    df = pd.read_csv(dataset_file)
    labels = np.delete(df['Tag'].unique(), np.where(df['Tag'].unique() == 'O'))
    train_data = format_dataframe_to_spacy(df)
    # Create, train and save model
    nlp = create_spacy_model(labels)
    train_model(nlp, train_data, iterations)
    nlp.to_disk(f'ner_{iterations}_iterations')

if __name__ == "__main__":
    main()