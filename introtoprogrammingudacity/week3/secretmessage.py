import os

def rename_files():
	# Get filename from a folder
	file_list = os.listdir("/Users/Keagan/Dropbox/Udacity/IPND/Stage_3/alphabet")
	print (file_list)
	saved_path = os.getcwd()
	print("Current working directory is " + saved_path)
	os.chdir("/Users/Keagan/Dropbox/Udacity/IPND/Stage_3/alphabet")

	# for each file, rename without numbers
	for file_name in file_list:
		print ("Old name - "+file_name)
		print ("New name - "+file_name.translate(None, "0123456789"))
		os.rename(file_name, file_name.translate(None, "0123456789"))
	os.chdir("/Users/Keagan/Dropbox/Udacity/IPND/Stage_3/alphabet")

rename_files()
