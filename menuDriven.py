import os

print("How can I help you?")

while True:
	print("What's your request : ",end='')
	ch = input()
	
	if (("run in ch") or ("open" in ch) or ("execute" in ch)) and ("chrome" in ch):
		os.system("chrome")
	
	elif (("run in ch") or ("open" in ch) or ("execute" in ch)) and (("notepad" in ch) or ("editor" in ch)):
		os.system("notepad")

	elif (("run in ch") or ("open" in ch) or ("execute" in ch)) and ("player" in ch) and ("media" in ch):
		os.system("wmplayer")

	elif (("run in ch") or ("open" in ch) or ("execute" in ch)) and ("vlc" in ch):
		os.system("vlc")

	elif (("run in ch") or ("open" in ch) or ("execute" in ch)) and ("whatsapp" in ch):
		os.system("whatsapp")

	elif (("run in ch") or ("open" in ch) or ("execute" in ch) or ("do" in ch)) and (("calculator" in ch) or ("calculation" in ch)):
		os.system("calc")

	elif ("open" in ch) and ("camera" in ch):
		os.system("start microsoft.windows.camera:")

	elif ("open" in ch) and (("jupyter" in ch) or ("jupyter-notebook" in ch) or ("jupyter notebook" in ch) or ("python" in ch)):
		os.system("jupyter notebook")

	elif (("run in ch") or ("open" in ch) or ("execute" in ch)) and ("telegram" in ch):
		os.system("telegram")

	elif ("open" in ch) and (("word" in ch) and ("office" in ch) and ("microsoft" in ch)):
		os.system("start winword")

	elif ("open" in ch) and (("excel" in ch) and ("office" in ch) and ("microsoft" in ch)):
		os.system("start excel")

	elif ("open" in ch) and (("powerpoint" in ch) and ("office" in ch) and ("microsoft" in ch)):
		os.system("start powerpnt")


	elif ("exit" in ch) or ("quite" in ch) or ("close" in ch):
		break
	else:
		print("command not supported")