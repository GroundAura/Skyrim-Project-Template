import os
import json
import configparser


# print(os.getcwd())

# # if (os.path.isfile("README.md") == True):
# # 	print(True)
# # else:
# # 	print(False)



# old_name_folder = "{FolderName}"
# #if (os.path.exists("./dist/" + old_name_folder + "/Base/scripts")):


# testpath = "dist/" + old_name_folder + "/Base/scripts"

# # os.chdir("./dist")

# print(os.getcwd())

# # os.chdir("./{FolderName}")

# if (os.path.exists(old_name_folder)):
# 	os.chdir('./dist/' + old_name_folder + '/Base/scripts')

# print(os.getcwd())






# def read_config_json(file_path):
# 	with open(file_path, 'r') as file:
# 		config_data = json.load(file)
# 	return config_data
# config_path = '.vscode/scripts/variables.json'

# def read_config(file_path):
#     config = configparser.ConfigParser()
#     config.read(file_path)
#     return config['Variables']
# config_path = './.vscode/scripts/variables.ini'


# # Example usage

# config_values = read_config(config_path)


# # Access the variables
# variable1 = config_values["new_author_display"]
# variable2 = config_values["new_author_github"]
# variable3 = config_values["new_id_github"]

# # Now you can use these variables in your script
# print(f"Variable 1: {variable1}")
# print(f"Variable 2: {variable2}")
# print(f"Variable 3: {variable3}")






# with open('./.vscode/scripts/variables.json', 'r') as file:
#   data = str(json.load(file))
# print(json.dumps(data))
#{'new_author_display': '______', 'new_author_github': '______', 'new_id_github': '______', 'new_id_nexus': '______', 'new_license_holder': '______', 'new_license_year': '______', 'new_name_folder': '______', 'new_name_mo2_release': '______', 'new_name_mo2_test': '______', 'new_name_plugin': '______', 'new_name_plugin_short': '______', 'new_name_zip': '______', 'new_path_7Zip': '______', 'new_path_md2nexus': '______', 'new_path_MO2Downloads': '______', 'new_path_MO2Mods': '______', 'new_path_PapyrusCK': '______', 'new_path_PapyrusMCMHelper': '______', 'new_path_PapyrusSKSE': '______', 'new_title': '______', 'new_title_xml': '______', 'new_title_short': '______', 'new_title_short_xml': '______'}

# data_str = str(data)
# print(data_str)
#{'new_author_display': '______', 'new_author_github': '______', 'new_id_github': '______', 'new_id_nexus': '______', 'new_license_holder': '______', 'new_license_year': '______', 'new_name_folder': '______', 'new_name_mo2_release': '______', 'new_name_mo2_test': '______', 'new_name_plugin': '______', 'new_name_plugin_short': '______', 'new_name_zip': '______', 'new_path_7Zip': '______', 'new_path_md2nexus': '______', 'new_path_MO2Downloads': '______', 'new_path_MO2Mods': '______', 'new_path_PapyrusCK': '______', 'new_path_PapyrusMCMHelper': '______', 'new_path_PapyrusSKSE': '______', 'new_title': '______', 'new_title_xml': '______', 'new_title_short': '______', 'new_title_short_xml': '______'}

#data_split = data.split(',')
#print(data_split)
#["{'new_author_display': '______'", " 'new_author_github': '______'", " 'new_id_github': '______'", " 'new_id_nexus': '______'", " 'new_license_holder': '______'", " 'new_license_year': '______'", " 'new_name_folder': '______'", " 'new_name_mo2_release': '______'", " 'new_name_mo2_test': '______'", " 'new_name_plugin': '______'", " 'new_name_plugin_short': '______'", " 'new_name_zip': '______'", " 'new_path_7Zip': '______'", " 'new_path_md2nexus': '______'", " 'new_path_MO2Downloads': '______'", " 'new_path_MO2Mods': '______'", " 'new_path_PapyrusCK': '______'", " 'new_path_PapyrusMCMHelper': '______'", " 'new_path_PapyrusSKSE': '______'", " 'new_title': '______'", " 'new_title_xml': '______'", " 'new_title_short': '______'", " 'new_title_short_xml': '______'}"]







print("Setting Variables: Starting...")

def read_config(file_path, section_header):
    config = configparser.ConfigParser(comment_prefixes=(";", "#", "//"), inline_comment_prefixes=(";", "#", "//"))
    config.read(file_path)
    return config[section_header]

config_path = './.vscode/scripts/variables.ini'
config_values_ids = read_config(config_path, 'IDs')
config_values_license = read_config(config_path, 'License')
config_values_name = read_config(config_path, 'Name')
config_values_paths = read_config(config_path, 'Paths')

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
old_name_plugin_short = "{PluginNameShort}"
old_name_zip = "{ZipName}"
old_path_7Zip = "{Path7Zip}"
old_path_md2nexus = "{Pathmd2nexus}"
old_path_MO2Downloads = "{PathMO2Downloads}"
old_path_MO2Mods = "{PathMO2Mods}"
old_path_PapyrusCK = "{PathCKSource}"
old_path_PapyrusMCMHelper = "{PathMCMHelperSource}"
old_path_PapyrusSKSE = "{PathSKSESource}"
old_title = "{TitleName}"
old_title_short = "{TitleNameShort}"
old_title_xml = "{TitleNameXML}"
old_title_xml_short = "{TitleNameXMLShort}"

# New Text:
new_author_display = config_values_name["AuthorName"]
new_author_github = config_values_ids["GitHubAccount"]
new_id_github = config_values_ids["RepositoryName"]
new_id_nexus = config_values_ids["NexusID"]
new_license_holder = config_values_license["LicensorName"]
new_license_year = config_values_license["LicenseYear"]
new_name_folder = config_values_name["FolderName"]
new_name_mo2_release = config_values_name["MO2ModName"]
new_name_mo2_test = config_values_name["MO2ModNameTest"]
new_name_plugin = config_values_name["PluginName"]
new_name_plugin_short = config_values_name["PluginNameShort"]
new_name_zip = config_values_name["ZipName"]
new_path_7Zip = config_values_paths["Path7Zip"]
new_path_md2nexus = config_values_paths["Pathmd2nexus"]
new_path_MO2Downloads = config_values_paths["PathMO2Downloads"]
new_path_MO2Mods = config_values_paths["PathMO2Mods"]
new_path_PapyrusCK = config_values_paths["PathCKSource"]
new_path_PapyrusMCMHelper = config_values_paths["PathMCMHelperSource"]
new_path_PapyrusSKSE = config_values_paths["PathSKSESource"]
new_title = config_values_name["TitleName"]
new_title_xml = config_values_name["TitleNameXML"]
new_title_short = config_values_name["TitleNameShort"]
new_title_short_xml = config_values_name["TitleNameXMLShort"]

print("Setting Variables: Complete!")



print(new_author_display)
print(new_author_github)
print(new_id_github)
print(new_id_nexus)
print(new_license_holder)
print(new_license_year)
print(new_name_folder)
print(new_name_mo2_release)
print(new_name_mo2_test)
print(new_name_plugin)
print(new_name_plugin_short)
print(new_name_zip)
print(new_path_7Zip)
print(new_path_md2nexus)
print(new_path_MO2Downloads)
print(new_path_MO2Mods)
print(new_path_PapyrusCK)
print(new_path_PapyrusMCMHelper)
print(new_path_PapyrusSKSE)
print(new_title)
print(new_title_xml)
print(new_title_short)
print(new_title_short_xml)







