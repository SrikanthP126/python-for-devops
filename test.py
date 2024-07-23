import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
#response = requests.get("https://www.linkedin.com/jobs/search")

complete_detail = response.json()

for i in range(len(complete_detail)):
    print (complete_detail[i]["user"]["login"])