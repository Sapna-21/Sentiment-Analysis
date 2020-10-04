# Sentiment-Analysis
We have implemented LSTM algorithm to analyse the sentiments of live tweets on a particular trending issue. Our aim was to achieve high prediction accuracy using this NLP model.

### Datasets
Train and test datasets should be in csv formats. 

### Preprocessing the data
1. Run `preprocess.py <csv-file-path>` for train and test datasets. This will generate their preprocessed versions. 
2. Run `stats.py <preprocessed-csv-path>` where `<preprocessed-csv-path>` is the path of csv generated from `preprocess.py`. This gives general statistical information about the dataset and will generate two pickle files which are the frequency distribution of unigrams and bigrams in the training dataset.

After the above steps, you should have four files in total: `<preprocessed-train-csv>`, `<preprocessed-test-csv>`, `<freqdist>`, and `<freqdist-bi>` which are preprocessed train dataset, preprocessed test dataset, frequency distribution of unigrams and frequency distribution of bigrams respectively.

### Analysing the data
Run `lstm.py`. This will save models for each epock in `./models/`. (Please make sure this directory exists before running `lstm.py`).
