import requests

class GitFileRequestor():
    git_raw_url = "https://raw.githubusercontent.com/"
    branch = "master"

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_raw_file(self,repo_owner, repository_name, file_path:str, save_dir=""):
        complete_url = joinURL(self.git_raw_url, repo_owner, repository_name, self.branch, file_path)
        r = requests.get(complete_url)
        file_name = file_path.split("/")[-1]
        target_save = save_dir + '\\' + file_name
        print(target_save)
        open(target_save, 'wb').write(r.content)
        return r.status_code, complete_url

def joinURL(*args:str):
    full_url = ""
    for url in args:
        full_url += url + "/"
    return full_url[:-1]


file = GitFileRequestor('my_username','my_password')
# file.get_raw_file('GitSquared','edex-ui','media/linuxIcons/16x16.png', "E:\Money Flow 2017")
x = file.get_raw_file('ibrahimyaacob92','excel_vba_essential','cohort-analysis-sample.xlsx', "E:\Money Flow 2017")
# print(x)