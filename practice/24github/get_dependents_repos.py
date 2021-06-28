'''
爬取某一个repo 的dependents repo列表

'''

import requests
from bs4 import BeautifulSoup

#获取 repos
def get_dependent_repos(url):
    # print("爬取网站地址： " + url)
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    repos = []
    for t in soup.findAll("div", {"class": "Box-row"}):
        try:
            user = t.find('a', {"data-hovercard-type":"user"}).text
            repository = t.find('a', {"data-hovercard-type":"repository"}).text
            print("path路径：", str(user) + "/" + str(repository))
            repos.append(str(user) + "/" + str(repository))
        except:
            continue

    # repos = [
    #     "{}/{}".format(
    #         t.find('a', {"data-hovercard-type":"user"}).text,
    #         t.find('a', {"data-hovercard-type":"repository"}).text
    #     )
    #     for t in soup.findAll("div", {"class": "Box-row"})
    # ]
    paginationContainer = soup.find("div", {"class":"paginate-container"}).find('a')
    return repos,paginationContainer


# 写repos
def write_repos(repos):
    path = "./dependents_pytorch3d.txt"
    for repo in repos:
        f = open(path, 'a', encoding='utf-8')
        f.write(repo + '\n')

#repo数
#repo = "PaddlePaddle/Paddle"
#页数  你想爬取的repo的页数
page_num = 2
#dependents 第一页的链接
url = 'https://github.com/facebookresearch/pytorch3d/network/dependents?dependents_before=MTM5NDM2MzA2NzE'
# url = 'https://github.com/huggingface/transformers/network/dependents?package_id=UGFja2FnZS01MjY1Njg3NA%3D%3D'
i = 0
repos_sum = []

#爬取  并实时写入
for i in range(page_num):
    print("爬取页数：", i+1)
    i = i + 1
    repos,paginationContainer = get_dependent_repos(url)
    write_repos(repos)
    print(i,len(repos))
    if i > 1 :
        paginationContainer = paginationContainer.next_sibling
    # print(paginationContainer.text)
    if paginationContainer:
        url = paginationContainer["href"]
    else:
        break
