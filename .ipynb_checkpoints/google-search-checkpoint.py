from googleapiclient.discovery import build
import pprint

my_api_key = "AIzaSyDqGh4xYa6T0o0J85NNl1veRxT9Efs6Opo"
my_cse_id = "ff1f623185feabbbb"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

results = google_search('what is python?', my_api_key, my_cse_id, num=2)

for result in results:
    '''pprint.pprint(result)'''

    title = result['title']
    link = result['formattedUrl']
    dis = result['snippet']
    print (title)
    print (link)
    print (dis)
