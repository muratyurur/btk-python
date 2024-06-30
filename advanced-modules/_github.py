import requests

r = requests


class Github:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = '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'

    def getUser(self, username):
        response = r.get(self.api_url + '/users/' + username)
        return response.json()

    def getRepositories(self, username):
        response = r.get(self.api_url + '/users/' + username + '/repos')
        return response.json()

    def createRepository(self, name):
        headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }

        response = r.post(self.api_url + '/user/repos?access_token=' + self.token, headers=headers, json={
            "name": name,
            "description": "This is my first repository created in Python using Github RestAPI",
            "homepage": "https://github.com/muratyurur/btk-python",
            "private": False,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        })

        return response.json()


github = Github()

while True:
    print(' Menü '.center(50, '*'))
    choice = input('1- Find User\n2- Get Repositories\n3- Create Repositories\n4- Exit\nSeçiminiz: ')

    if choice == '4':
        break
    elif choice == '1':
        username = input('username: ')
        result = github.getUser(username)
        print(f"name: {result['name']} | public repos: {result['public_repos']} | followers: {result['followers']}")
    elif choice == '2':
        username = input('username: ')
        result = github.getRepositories(username)
        print(f" {username}'s public repositories ".center(50, '*'))
        for i in result:
            print(f"name: {i['name']} | url: {i['html_url']} | description: {i['description']}")
    elif choice == '3':
        name = input('Repository Name: ')
        result = github.createRepository(name)
        print(result)
    else:
        print('Hatalı bir seçim yaptınız.')
