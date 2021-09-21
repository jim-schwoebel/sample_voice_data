import os, uuid

curdir=os.getcwd()

def rename_files():
	listdir=os.listdir()
	for i in range(len(listdir)):
		if listdir[i].endswith('.wav'):
			os.rename(listdir[i], str(uuid.uuid4())+'.wav')

os.chdir(curdir)
os.chdir('males')
rename_files()

os.chdir(curdir)
os.chdir('females')
rename_files()