import os,inspect,time
commit = "nothing"
username = "name" # your github username
useremail= "name@gmail.com" # your github email address
repo_name = "oneclick_upload" # your repo name
package_name= "ocupload" # your package name
replaced_name = repo_name.replace("_","-") #replace _ - for git hub
os.chdir(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+f'/{repo_name}')
os.system("git init")
os.system(f"git remote add {replaced_name} https://github.com/{username}/{replaced_name}")
os.system("git branch main")
os.system("git checkout -b main")
os.system(f'git config user.name "{username}" ')
os.system(f'git config user.email "{useremail}" ')
os.system(f"git add {repo_name} LICENSE README.md")
os.system(f"git commit -m \"{commit}\"")
os.system(f"git push {replaced_name} --force main")
os.system(f"rmdir /s /q .git")
os.system("python \""+os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+f"\"/{repo_name}/setup.py sdist bdist_wheel")
os.system("python -m twine upload dist/*")
print("done")
os.system(f"rmdir /s /q build dist {package_name}.egg-info")
print(f"deleted [build,dist,{package_name}.egg-info]")
