import sys
import os
import spacy

def main():
    if len(sys.argv) != 2:
        print("Usage: python predict.py input_txt_path")
        sys.exit(1)
    input_txt = sys.argv[1]
    dirs_list = os.listdir()
    models_iterations = [int(dir.split('_')[1]) for dir in dirs_list if dir.startswith('ner_')]
    if not models_iterations:
        print('No models found')
        sys.exit(1)
    max_iterations = max(models_iterations)
    print(f'Using model with {max_iterations} iterations')
    nlp = spacy.load(f'ner_{max_iterations}_iterations')
    with open(input_txt, 'r', encoding='utf-8') as f:
        for line in f:
            doc = nlp(line.strip())
            for ent in doc.ents:
                print(f'"{ent.text}" -> {ent.label_}\n')

if __name__ == "__main__":
    main()