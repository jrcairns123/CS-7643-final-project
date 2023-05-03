# CS-7643-final-project

Project problem area is Automatic Speech Recognition (ASR; i.e. speech-to-text). 

Nvidia Neural Modules (NeMo) package was primarily used for modeling.

Example data files which the NeMo models/package could accept (given data is downloaded in specified locations on machine) may be seen in /data. Some example charts (e.g. learning curves) from training with the pre-trained conformer-transducer model may be seen in /data/conformer_transducer_small.

Code files used may be found in /code. Specifically, /code/utils.py contains a simple helper function to extract audio files from a .tar compressed file. This was not necessary when retrieving data using HuggingFace datasets package. The python notebook /code/main.ipynb contains the bulk of the code which was used for training and evaluation. This file is self-contained and may be run in Google Colab to replicate our work (possibly with a few modifications for model configs).

Example NeMo model configs may be seen in /code/configs. These are useful in getting up to speed with the expected NeMo model configurations.