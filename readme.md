# Reconocimiento de Entidades Nombradas

## Preparación de los datos

La página web https://tecoholic.github.io/ner-annotator/ te da una interfaz amigable para taggear tus datos de entrenamiento. Dicha página exporta un archivo llamado "annotations.json". Para agregarlo al dataset simplemente hay que poner dicho archivo en esta carpeta y correr el siguiente programa:

```bash
python add_annotations_to_dataset.py
```

El script <a href="https://github.com/santifiorino/spanish_ner/blob/main/add_annotations_to_dataset.py">add_annotations_to_dataset.py</a> se fijará si existe el archivo _dataset.csv_. En caso de que exista, agrega la información nueva al final, manteniendo la numeración existente. En caso de que no exista, crea el archivo.

## Modelo de spaCy

### Entrenamiento

Para entrenar el modelo simplemente hay que correr el siguiente programa:

```bash
python train.py dataset.csv nro_iteraciones
```

El script <a href="https://github.com/santifiorino/spanish_ner/blob/main/train.py">train.py</a> crea el modelo, lo entrena con el dataset y número de iteraciones dado, y lo guarda en un nuevo directorio de nombre _ner_n_iterations_.

### Clasificación

Una vez entrenado, si se quiere clasificar un texto simplemente se debe correr el siguiente programa:

```bash
python predict.py texto_entrada.txt
```

El script <a href="https://github.com/santifiorino/spanish_ner/blob/main/predict.py">predict.py</a> busca el modelo entrenado con mayor número de iteraciones, lo carga, e imprime todas las entidaes presentes en el texto dado.
