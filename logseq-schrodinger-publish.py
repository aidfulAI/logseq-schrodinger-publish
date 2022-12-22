import os
import sys
from configparser import ConfigParser
from zipfile import ZipFile

def removeFilesInDir(dirPath):
	"""remove all files in directory"""
	for root, dirs, files in os.walk(dirPath, topdown=False):
		for name in files:
			os.remove(os.path.join(root, name))
		for name in dirs:
			os.rmdir(os.path.join(root, name))

def main():
	# read values from config file
	config = ConfigParser()
	config.read('config.ini')
	publicExportZip = config.get('DEFAULT', 'publicExportZip')
	githubRepoDir = config.get('DEFAULT', 'githubRepoDir')

	removeFilesInDir(os.path.join(githubRepoDir, "pages"))
	removeFilesInDir(os.path.join(githubRepoDir, "assets"))

	# transform string to path (converts on Windows the backward to a forward slash)
	publicExportZip = os.path.normpath(publicExportZip)
	githubRepoDir = os.path.normpath(githubRepoDir)
	print("Input zip:  ", publicExportZip)
	print("Output dir: ", githubRepoDir)

	# loading the zip file and extracting all objects
	if(os.path.exists(publicExportZip) == False):
		print("ERROR: File not found: ", publicExportZip)
		sys.exit(1)
	else:
		with ZipFile(publicExportZip, 'r') as zObject:
			# Extracting all the members of the zip file
			zObject.extractall(path=githubRepoDir)

	# delete the zip file
	os.remove(publicExportZip)

if __name__ == "__main__":
	main()