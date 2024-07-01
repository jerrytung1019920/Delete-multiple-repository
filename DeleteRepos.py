import requests

#輸入你的用戶名與鑰匙
username = 'YOUR_GITHUB_USERNAME'
token = 'YOUR_PERSONAL_ACCESS_TOKEN'

# 要刪除的Respository名稱
repos_to_delete = [
    'repo1',
    'repo2',
    'repo3'
]

#你Github網址
url = f'https://api.github.com/repos/{username}/'

headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'

}

# 批量删除
for repo in repos_to_delete:
    response = requests.delete(url + repo, headers=headers)
    if response.status_code == 204:
        print(f'Successfully deleted {repo}')
    else:
        print(f'Failed to delete {repo}: {response.status_code} - {response.text}')
