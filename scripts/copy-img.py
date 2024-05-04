#copy "docs\images\brand\Main.png" "dist\{FolderName}\fomod\images"
#import os
#from os import getcwd
#from os.path import join

#ROOT_PATH: str = getcwd()
#print(r"C:\Games\Skyrim\Projects\My Projects\Skyrim-Project-Template\scripts\aurapy")

import sys
#sys.path.append(join(ROOT_PATH, "scripts\\aurapy"))
#sys.path.append(aurapy)
#sys.path.append(r"C:\Games\Skyrim\Projects\My Projects\Skyrim-Project-Template\scripts\aurapy")
#sys.path.append(r"C:\Games\Skyrim\Projects\My Projects\Skyrim-Project-Template\scripts")
#sys.path.append(r"C:\Games\Skyrim\Projects\My Projects\Skyrim-Project-Template")
sys.path.append('./scripts/aurapy')

for i in sys.path:
    print(f"path: {i}")

#import aura_config

#from aura_config import read_config
#from aura_files import copy_file, get_root_path




def main():
	print("test")
	#CONFIG_PATH: str = join(ROOT_PATH, "Project_Settings.ini")
	#config: dict[str, dict[str]] = read_config(CONFIG_PATH)
	#print(f"\nConfig ({CONFIG_PATH}):\n{config}")
	#FolderName: str = config["PROJECT"]["sprojectnamefolder"]

	#print(f"FolderName: {FolderName}")
	#copy_file(join(ROOT_PATH, "docs\\images\\brand\\Main.png)"), (join(ROOT_PATH, "dist", FolderName, "fomod\\images\\Main.png")))


if __name__ == "__main__":
	main()

