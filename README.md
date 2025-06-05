# WaW Stock Map Script Placer

A tool for creating custom Stock Map - Mods.
It essentially just drops a base set of files into a specific folder structure.
Said base files are extracted from the stock .ff files located in waw_root/zone/english.
You can download my base_files.zip file or extract the ff's yourself.

If extracting them yourself:
- Create these subdirs (sp, mp, zm) in the _internal/base_files folder, then place your extracted ff's into the game-mode subdirs
    i.e _internal/base_files/sp/ber1, ber2, etc.
- Drop mapname_patch into mapname & replace all, then mapname_load into mapname & replace all.
- The tool only looks out for _internal/base_files/*mode*/*mapname*, not _patch nor _load so ensure you merge them all in correct order.

# Installation

- Download waw-stock-map-script-placer v1.2.1.zip
- Extract waw-stock-map-script-placer v1.2.1.zip

- Download base_files.zip
- Extract base_files.zip

- Drop base_files folder into _internal folder
    The base_files dir will automatically be created when you try to build a mod and it detects the base_files dir is missing.
    So.. if you see a dialog pointing this out, then you've skipped a step but not worry, just drop the subdirs from the extracted base_files.zip into the _internal/base_files folder.

# Usage

- Go into _internal folder, then into json folder, open local.json and replace the directory with your own waw root directory.
- Run waw-stock-map-script-placer v1.2.1.exe
- Enter your desired Mod Name

Decide whether you want (all of these options are optional):
- A waw exe shortcut sent to your desktop with predefined args so you can load right into map via running said shortcut.
- The mod built/compiled, it does the same thing as the stock launcher.
- Insert an in-game print message to confirm build. this will just add a few lines of code to mapname.gsc so when you run the map it will print a message which will indicate that the build was successful. if you check build mod, as well as this option, but dont see the in-game print message, then the build failed.
- Automatically have the map run after mod has been created.

Select one of the maps in the mode-specific sections.

# License

GNU Lesser General Public License Version 3

# Screenshot

![alt text](misc/screenshot1.png)

# Video

https://youtu.be/-cfac1ugllk

# Creator

Phil81334

# Socials

[ModOps](https://modopshq.com) || [Discord](https://discord.gg/SEkBECkt2Q) || [YouTube](https://www.youtube.com/@modopshq)