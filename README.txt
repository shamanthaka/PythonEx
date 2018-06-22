edit .git/config file under your repo directory
find url=entry under section [remote "origin"]
change it from url=https://github.com/shamanthaka/lunch_call.git to

url = https://shamanthaka@github.com/shamanthaka/PythonEx.git
Save config file and quit. now you could use git push origin master to sync your repo on GitHub