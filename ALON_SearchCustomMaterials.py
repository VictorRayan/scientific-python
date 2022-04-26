import pandas as pd
from json import dumps
from googleapiclient.discovery import build



my_api_key = "AIzaSyBT_xGuMVLKPAIoslqM4QZ9pWrIiMNzkTY"
my_cse_id = "162d6586b735146f8"


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']


#results = google_search('what is Hadamard gate?', my_api_key, my_cse_id, num=2)

'''zzz
for result in results:
    

    title = result['title']
    link = result['formattedUrl']
    dis = result['snippet']
    print (title)
    print (link)
    print (dis)
'''


# Show all columns in pandas dataframe when printing to stdout
pd.set_option("display.max_columns", None)

datafile='../01_db_exploration/data/magnetic-dimensionality-v100.csv'
df0 = pd.read_csv(datafile, ';')
#print(df0.keys())

# Drop all the columns except these ones
df = df0[['icsd_code','dimension', 'chemical_structural_formula', 'num_atoms', 'space_group_symmetry', 'number_index', 'structure_type', 'valence', 'metal_neigh_coordination', 'partial_occupancy']].copy()

# Print only materials with a given number of atoms, two-dimensional and no partial occupancy of atomic sites
print(df[ (df.num_atoms<=3) & (df.dimension==2) & (df.partial_occupancy=='no') ])


# Dictionary with the data gathered in the search
gathered_data={'material':[],'search_word':[],'search_result':[]}

# List of materials to be searched
lista_de_materiais=['Fe Cl2','Cr Se2']

# List of words to be searched for
lista_de_termos=['magnetic','metal','insulator']


# Loop over material and search words
# 'google_search_for()' should be substituted with appropriate method from google API
for mat in lista_de_materiais:
  for word in lista_de_termos:
    gathered_data['material'].append(mat)
    gathered_data['search_word'].append(word)
    try:

        gathered_data['search_result'].append(google_search(mat+" "+word, my_api_key, my_cse_id, num=1))
    except:
        gathered_data['search_result'].append('No results')
        
        
# Writes gathered_data dictionary into json file
with open('data/gresults.json', 'w') as jsonf:
     jsonf.write(dumps(gathered_data))  



