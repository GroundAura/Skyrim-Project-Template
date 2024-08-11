from os.path import join
from auralib.config import read_config
from auralib.files import get_root_path, copy_file


def main():
	print(f"STATUS: Starting Task: Copy Image...")
	try:
		ROOT_PATH: str = get_root_path()
		CONFIG_PATH: str = join(ROOT_PATH, "Project_Settings.ini")
		config: dict[str, dict[str]] = read_config(CONFIG_PATH, preserve_key_case=True)
		copy_file(join(ROOT_PATH, "docs\\images\\brand\\Main.png"), (join(ROOT_PATH, "dist", config["PROJECT"]["sProjectNameFolder"], "fomod\\images\\Main.png")))
		print(f"INFO: Copied image successfully.")
		print(f"STATUS: Completed Task: Copy Image.")
	except Exception as e:
		print(f"STATUS: Failed Task: Copy Image.\nERROR: {e}")


if __name__ == "__main__":
	main()

