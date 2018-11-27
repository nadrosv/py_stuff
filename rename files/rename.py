# renames video files recorded on GOPRO or YI cameras.
# Those cameras divide long video sequences into shorter parts and name them in following manner:
# YDTL0001 (initial part), YT010001, YT020001, etc. which is confusing in some cases (sorting, browsing).
# The following script renames those files to 0000101TL, 000102TL, and so on.

import os
import datetime

path = 'testfiles\\'
files =[]


# REGEX
re_name = re.compile('\\w{4}\\d{4}\\.(txt|mov|mp4|MP4|JPG|jpg|JPEG|jepg)')
re_chap = re.compile('\\D{2}')

files = os.listdir(path)

for name in files:
	if re_name.match(name):
		if re_chap.match(name[2:4]):
			chap = '00'
		else:
			chap = name[2:4]
		new_name = name[-8:-4] + chap + name[0:2] + name[-4:]
		print(new_name)

		os.rename(path + name, path + new_name)
