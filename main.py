import json
import os
import click
from creation_index import build_non_pos_index, preprocess_text

def create_index_with_options(documents, options, index_filename, stats_filename):
    index, stats = build_non_pos_index(documents, options)

    # Write the index to a file
    with open(index_filename, 'w') as file:
        json.dump(index, file, indent=2)

    return stats

@click.command()
@click.option('--input_file', default='crawled_urls.json', help='Input JSON file containing the list of documents.')
def main(input_file):
    # Load the JSON data
    with open(input_file, 'r', encoding='utf-8') as file:
        documents = json.load(file)

    # Set the processing options
    options_with_stemmer = ['lowercase', 'remove_stopwords', 'stemming']
    options_without_stemmer = ['lowercase', 'remove_stopwords']

    # Create index with stemmer
    stemmer_index_filename = 'mon_stemmer.title.non_pos_index.json'
    stats_filename = 'metadata.json'
    stats = create_index_with_options(documents, options_with_stemmer, stemmer_index_filename, stats_filename)

    # Create index without stemmer
    no_stemmer_index_filename = 'title.non_pos_index.json'
    create_index_with_options(documents, options_without_stemmer, no_stemmer_index_filename, stats_filename)
    
    
    # Write the stats to a file
    with open("metadata", 'w') as file:
        json.dump(stats, file, indent=2)

if __name__ == '__main__':
    main()

