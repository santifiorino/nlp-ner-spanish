```bash
python train.py dataset.csv nro_iteraciones
python predict.py texto_entrada.txt
```

El script <a href="https://github.com/santifiorino/spanish_ner/blob/main/train.py">train.py</a> crea el modelo, lo entrena con el dataset dado, y lo guarda en un nuevo directorio de nombre _ner_n_iterations_. Luego, el <a href="https://github.com/santifiorino/spanish_ner/blob/main/predict.py">predict.py</a> busca los directorios nombrados de esa forma, y carga aquel modelo con mayor número de iteraciones.
