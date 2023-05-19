import sys
import os
import spacy

def main():
    if len(sys.argv) != 2:
        print("Uso: python predict.py texto_entrada.txt")
        sys.exit(1)
    input_txt = sys.argv[1]
    dirs_list = os.listdir()
    models_iterations = [int(dir.split('_')[1]) for dir in dirs_list if dir.startswith('ner_')]
    if not models_iterations:
        print('No se encontraron modelos entrenados')
        sys.exit(1)
    max_iterations = max(models_iterations)
    print(f'\n\nUsando el modelo con {max_iterations} iteraciones\n')
    nlp = spacy.load(f'ner_{max_iterations}_iterations')
    with open(input_txt, 'r', encoding='utf-8') as f:
        for line in f:
            doc = nlp(line.strip())
            for ent in doc.ents:
                print(f'"{ent.text}" -> {ent.label_}\n')

if __name__ == "__main__":
    main()