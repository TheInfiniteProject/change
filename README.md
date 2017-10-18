# change
project is focused on parsing through various open-source databases containing facts about various topics of the world (ie. CIA.org The World Fact Book))

1. MAIN_change.py will act as the main module, this will be where the graph and gui are created
2. PARSE_fields_print.py will parse through each field file in 'FactBookExtract/factbook/fieldsPRINT' and create a file in 'SORTED_fields_print' called 'category_list_file'
3. PARSE_fields_print_data.py will parse through each field file in 'FactBookExtract/factbook/fieldsPRINT' and create a file for each category found in 'category_list_file' with the corresponding data

- 'SORTED_fields_print' contains 'category_list_file' and 'category_data_files'
- 'category_data_files' will hold all the data obtained from the parsed field files
