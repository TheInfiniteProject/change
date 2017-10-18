# change
project is focused on parsing through various open-source databases containing facts about various topics of the world (ie. https://www.cia.gov/library/publications/resources/the-world-factbook/docs/faqs.html)

- 'PARSE_fields_print.py' will parse through each field file in 'FactBookExtract/factbook/fieldsPRINT' and create a file in 'SORTED_fields_print' called 'category_list_file'
- 'PARSE_fields_print_data.py' will parse through each field file in 'FactBookExtract/factbook/fieldsPRINT' and create a file for each category found in 'category_list_file' with the corresponding data


- 'SORTED_fields_print' contains 'category_list_file' and 'category_data_files'
- 'category_data_files' will hold all the data obtained from the parsed field files



1.download the world factbook 2016 from cia.gov > https://www.cia.gov/library/publications/resources/the-world-factbook/
2. in order to run 'PARSE_fields_print.py' or 'PARSE_fields_print_data' create 3 folders in the local directory named 'FactBookExtract', 'SORTED_fields_print', and 'factbook'('factbook' should be created inside 'FactBookExtract')
3.extract the world fact book files into 'FactBookExtract/factbook'
4. delete all files and directories in 'factbook' except for 'fields'
5. create a folder named 'fieldsPrint' inside 'FactBookExtract/factbook'
6. move all 'print_...' files from 'fields' into 'fieldsPrint'
7. run 'PARSE_fields_print.py'

- im still working on 'PARSE_fields_print_data.py' 
