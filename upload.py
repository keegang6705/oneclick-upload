import os,inspect,time
commit = "nothing"
username = "name" # your github username
useremail= "name@gmail.com" # your github email address
package_name = "python_package" # your package name
replaced_name = package_name.replace("_","-") #replace _ - for git hub
os.chdir(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+f'/{package_name}')
os.system("git init")
os.system(f'git config --global "{username}" ')
os.system(f'git config --global "{useremail}" ')
os.system(f"git remote add {replaced_name} https://github.com/{username}/{replaced_name}")
os.system("git branch main")
os.system("git checkout -b main")
os.system(f"git add {package_name} LICENSE README.md")
os.system(f"git commit -m \"{commit}\"")
os.system(f"git push {replaced_name} --force main")
os.system(f"rmdir /s /q .git")
os.system("python \""+os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+f"\"/{package_name}/setup.py sdist bdist_wheel")
os.system("twine upload dist/*")
print("done")
os.system(f"rmdir /s /q build dist {package_name}.egg-info")
print(f"deleted [build,dist,{package_name}.egg-info]")
