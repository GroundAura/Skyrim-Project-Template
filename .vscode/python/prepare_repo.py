import os
#import shutil
#from pathlib import Path
from pathlib2 import Path
#from fileinput import FileInput



# VARIABLES

# Old Text:
old_author_display = "{AuthorName}"
old_author_github = "{GitHubAccount}"
old_id_github = "{RepositoryName}"
old_id_nexus = "{NexusID}"
old_license_holder = "{LicensorName}"
old_license_year = "{LicenseYear}"
old_name_folder = "{FolderName}"
old_name_mo2_release = "{MO2ModName}"
old_name_mo2_test = "{MO2ModNameTest}"
old_name_plugin = "{PluginName}"
old_name_zip = "{ZipName}"
old_path_7Zip = "{Path7Zip}"
old_path_md2nexus = "{Pathmd2nexus}"
old_path_MO2Downloads = "{PathMO2Downloads}"
old_path_MO2Mods = "{PathMO2Mods}"
old_title = "{TitleName}"
old_title_short = "{TitleNameShort}"
old_title_xml = "{TitleNameXML}"
old_title_xml_short = "{TitleNameXMLShort}"

# New Text:
new_author_display = "______"
new_author_github = "______"
new_id_github = "______"
new_id_nexus = "______"
new_license_holder = "______"
new_license_year = "______"
new_name_folder = "______"
new_name_mo2_release = "______"
new_name_mo2_test = "______"
new_name_plugin = "______"
new_name_zip = "______"
new_path_7Zip = "______"
new_path_md2nexus = "______"
new_path_MO2Downloads = "______"
new_path_MO2Mods = "______"
new_title = "______"
new_title_xml = "______"
new_title_short = "______"
new_title_short_xml = "______"

# Example 1:
#new_author_display = "GroundAura"
#new_author_github = "GroundAura"
#new_id_github = "Auras-Inventory-Tweaks"
#new_id_nexus = "68557"
#new_license_holder = "GroundAura"
#new_license_year = "2023"
#new_name_folder = "Aura's Inventory Tweaks"
#new_name_mo2_release = "Aura's Inventory Tweaks []"
#new_name_mo2_test = "Aura's Inventory Tweaks (pre-release) []"
#new_name_plugin = "AIT"
#new_name_zip = "Auras Inventory Tweaks"
#new_path_7Zip = "C:\Program Files\7-Zip"
#new_path_md2nexus = "C:\Tools\md2nexus"
#new_path_MO2Downloads = "D:\Games\Bethesda\Elder Scrolls\Skyrim\MO2\downloads"
#new_path_MO2Mods = "C:\Games\Elder Scrolls\V - Skyrim\SMEFT\mods"
#new_title = "Aura's Inventory Tweaks"
#new_title_xml = "Aura's Inventory Tweaks"
#new_title_short = "AIT"
#new_title_short_xml = "AIT"

# Example 2:
#new_author_display = "GroundAura"
#new_author_github = "GroundAura"
#new_id_github = "Phenomenally-Enriched-Ingredients"
#new_id_nexus = "90526"
#new_license_holder = "GroundAura"
#new_license_year = "2023"
#new_name_folder = "Phenomenally Enriched & Nuanced Ingredients for SkyUI"
#new_name_mo2_release = "BOOBIES - PENIS (pre-release) []"
#new_name_mo2_test = "BOOBIES - PENIS (pre-release) []"
#new_name_plugin = "PENIS_IconsAddon"
#new_name_zip = "Phenomenally Enriched & Nuanced Ingredients for SkyUI"
#new_path_7Zip = "C:\Program Files\7-Zip"
#new_path_md2nexus = "C:\Tools\md2nexus"
#new_path_MO2Downloads = "D:\Games\Bethesda\Elder Scrolls\Skyrim\MO2\downloads"
#new_path_MO2Mods = "C:\Games\Elder Scrolls\V - Skyrim\SMEFT\mods"
#new_title = "Phenomenally Enriched & Nuanced Ingredients for SkyUI"
#new_title_xml = "Phenomenally Enriched and Nuanced Ingredients for SkyUI"
#new_title_short = "P.E.N.I.S. for B.O.O.B.I.E.S"
#new_title_short_xml = "P.E.N.I.S. for B.O.O.B.I.E.S"



# RENAME FOLDERS

print(os.getcwd())

# os.chdir("./dist")
# (rename folder)
# old_name_folder = new_name_folder

# os.chdir("./dist/" + old_name_folder + "/Base/MCM/Config")
# (rename folder)
# old_name_plugin = new_name_plugin



# RENAME FILES

os.chdir("./build/MO2")
print(os.getcwd())

os.rename(old_name_zip + ".zip.meta", new_name_zip + ".zip.meta")

os.chdir("../..")
print(os.getcwd())


os.chdir("./dist/" + old_name_folder + "/Base/interface/translations")
print(os.getcwd())

os.rename(old_name_plugin + "_ENGLISH.txt", new_name_plugin + "_ENGLISH.txt")

os.chdir("../../../../..")
print(os.getcwd())


os.chdir("./dist/" + old_name_folder + "/Base")
print(os.getcwd())

os.rename(old_name_plugin + ".esp", new_name_plugin + ".esp")
os.rename(old_name_plugin + ".esl", new_name_plugin + ".esl")
os.rename(old_name_plugin + ".esm", new_name_plugin + ".esm")

os.chdir("../../..")
print(os.getcwd())

os.chdir("./dist/" + old_name_folder + "/Source/scripts")
print(os.getcwd())

os.rename(old_name_plugin + "MCM.psc", new_name_plugin + "MCM.psc")

os.chdir("../../../..")
print(os.getcwd())



# REPLACE TEXT

os.chdir("./.vscode/commandline")
print(os.getcwd())

with open(r'copy-img.bat', 'r') as file:
	data = file.read()
	data = data.replace(old_name_folder, new_name_folder)
with open(r'copy-img.bat', 'w') as file:
	file.write(data)

with open(r'copy-pex.bat', 'r') as file:
	data = file.read()
	data = data.replace(old_name_folder, new_name_folder)
with open(r'copy-pex.bat', 'w') as file:
	file.write(data)

with open(r'md2nexus.bat', 'r') as file:
	data = file.read()
	data = data.replace(old_path_md2nexus, new_path_md2nexus)
with open(r'md2nexus.bat', 'w') as file:
	file.write(data)

with open(r'mo2-downloads.bat', 'r') as file:
	data = file.read()
	data = data.replace(old_name_zip, new_name_zip)
	data = data.replace(old_path_MO2Downloads, new_path_MO2Downloads)
with open(r'mo2-downloads.bat', 'w') as file:
	file.write(data)

with open(r'mo2-mod.bat', 'r') as file:
	data = file.read()
	data = data.replace(old_name_folder, new_name_folder)
	data = data.replace(old_name_mo2_test, new_name_mo2_test)
	data = data.replace(old_path_MO2Mods, new_path_MO2Mods)
with open(r'mo2-mod.bat', 'w') as file:
	file.write(data)

with open(r'zip.bat', 'r') as file:
	data = file.read()
	data = data.replace(old_name_folder, new_name_folder)
	data = data.replace(old_name_zip, new_name_zip)
	data = data.replace(old_path_7Zip, new_path_7Zip)
with open(r'zip.bat', 'w') as file:
	file.write(data)

os.chdir("../..")
print(os.getcwd())


os.chdir("./.vscode/papyrus")
print(os.getcwd())

os.chdir("../..")
print(os.getcwd())


os.chdir("./build/MO2")
print(os.getcwd())

with open(r'new_name_zip' + '.zip.meta', 'r') as file:
	data = file.read()
	data = data.replace(old_name_mo2_test, new_name_mo2_test)
	data = data.replace(old_title, new_title)
with open(r'new_name_zip + ".zip.meta"', 'w') as file:
	file.write(data)

os.chdir("../..")
print(os.getcwd())


