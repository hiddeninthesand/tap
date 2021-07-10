def help_menu(application_name, application_version):
	print(f"{application_name} ({application_version}) - MPR in your pocket")
	print()
	print(f"Usage: {application_name} [command] [packages/options]")
	print()
	print("Commands:")
	print("  install           Install packages")
	# print("  update/upgrade    Update packages")
	print("  search            Search for packages")
	# print("  clone             Clone packages")
	print()
	print("Options:")
	print("  -h, --help        Bring up this help menu")
