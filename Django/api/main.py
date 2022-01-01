import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("kod stanu :", r.status_code)

response_dict = r.json()
print("Całkowita liczba repozytorióœ : ",response_dict['total_count'])

repo_dicts =  response_dict['items']
print("liczba zwróconych repozytoriów: ", len(repo_dicts))

repo_dict = repo_dicts[0]
print("\nKlucze:",len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

print( response_dict.keys() )