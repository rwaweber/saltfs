import toml
import json
import requests

# homu_repos = toml.load('/home/servo/homu/cfg.toml')['repo']
# keys = homu_repos.keys()
# # in the event that libraries are configured on repos other than the servo group
# configured_repos = [homu_repos[i]['owner']+'/'+i for i in keys ]

# dirty way to page through 2 maximum repos
# gh_repos_p1 = [repo['html_url'] for repo in requests.get(
#     'https://api.github.com/orgs/servo/repos?page=1&per_page=100').json()]

# gh_repos_p2 = [repo['html_url'] for repo in requests.get(
#     'https://api.github.com/orgs/servo/repos?page=2&per_page=100').json()]
# print("GH:",gh_repos)
# configured_repos = toml.load('/home/servo/homu/cfg.toml')['repo']
# keys = configured_repos.keys()
# # in the event that libraries outside servo org
# homu_repos = ["https://github.com/"+configured_repos[i]['owner']+'/'+i for i in keys ]

# print("HOMU:",homu_repos)

# homu_repo_diff = list(set(homu_repos) - set(gh_repos))

# print("Difference:",homu_repo_diff)

def repo_retrieve(org,page):
    return [repo for repo in requests.get('https://api.github.com/orgs/'+org+'/repos?page='+str(page)).json()]

def repo_pager(org):
    endpoint = 'https://api.github.com/orgs/'+org+'/repos'
    num_pages = int(requests.get(endpoint).links["last"]["url"].split("page=", 1)[1])+1
    return [ repo_retrieve(org,page) for page in (1,num_pages)]
        
print("p1:",repo_retrieve('servo',1)['message'])
print("p2:",repo_retrieve('servo',2))
print("p3:",repo_retrieve('servo',3))
print("p4:",repo_retrieve('servo',4))
print("p5:",repo_retrieve('servo',5))
