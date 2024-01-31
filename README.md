# Minimal Index Project

## Contributor
Tanguy Legrand


## Description
This Python program enables the creation of non-positional web indexes based on the content of documents. It consists of two main files:

### creation_index.py
This file contains functions for text preprocessing and building a non-positional index from a collection of documents.
### main.py
The main script that loads a list of documents, processes them using the functions from creation_index.py, and creates non-positional indexes with or without stemming.

## Features

Builds a non-positional web index from a list of URLs in JSON in JSON title.non_pos_index.json  
Shows statistics on documents in json metadata  
Creates a non-positional web index by applying a stemmer in the JSON my_stemmer.title.non_pos_index.json  


## Prerequisites
Python 3.x  
NLTK (Natural Language Toolkit) library  


## Configuration
Ensure you have the required dependencies installed by running the following commands:

pip install nltk click  
python -m nltk.downloader punkt stopwords  


## Usage
Run the program by executing the following command in your terminal:  

python main.py --input_file crawled_urls.json


## Options
--input_file: Specifies the input JSON file containing the list of documents. Default is crawled_urls.json.


## Organization of the Project

### creation_index.py

Contains functions for text preprocessing (preprocess_text) and building a non-positional index (build_non_pos_index).

### main.py

The main script that uses functions from creation_index.py to create non-positional indexes with or without stemming.



## Files

### creation_index.py

preprocess_text: Tokenizes, lowercases, removes stopwords, and applies stemming to input text.
build_non_pos_index: Builds a non-positional index from a collection of documents.

### main.py

create_index_with_options: Calls build_non_pos_index with specified options and saves the index and metadata to files.
main: Loads documents from the input file, creates non-positional indexes with and without stemming, and saves statistics.

### crawled_urls.json

Example input file containing a list of documents with fields such as URL, title, content, and h1.

### metadata.json

Output file containing statistics about the created indexes.

### mon_stemmer.title.non_pos_index.json

Output file containing the non-positional index with stemming applied.

### title.non_pos_index.json

Output file containing the non-positional index without stemming.
