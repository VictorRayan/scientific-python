#
# THIS IS  A PROTOTYPE SCRIPT
#

def google_search_for(mat, word):
  print('Warning: Need to code google search!')

# Dictionary with the data gathered in the search
gathered_data={'material':[],'search_word':[],'search_result':[]}

# List of materials to be searched
list_of_materials=['CrSe2','VI2','V2C']

# List of words to be searched for
list_of_words=['magnetism','insulator','metal']

# Loop over material and search words
# 'google_search_for()' should be substituted with appropriate method from google API
for mat in list_of_materials:
  for word in list_of_words:
    gathered_data['material'].append(mat)
    gathered_data['search_word'].append(word)
    gathered_data['search_result'].append(google_search_for(mat,word))


