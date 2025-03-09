This is a pack of programs that I used for editing texts on Persona 5 Strikers LINKDATA.

I didn't do any of the tools, most of them were made by Grok. (Yes, the X AI, I'm no programmer.)

Russian_Tool is necessary, but all of the executables have warnings on VirusTotal. (Nothing ever happened to me, but it's up to you download it or not.)

VirusTotal for the 4 files:

https://www.virustotal.com/gui/file/207abf5719bb65d9a256c5e55587c3d4f1f6a714de81a43cb6f57f768cbd0370
https://www.virustotal.com/gui/file/90b2a3f9b13946b9cad8a41bbb179f2dd870406a1372ad3024e5e6f63330566f
https://www.virustotal.com/gui/file/62ef3b4c2f855926a6d1c41ea6ed078012019ca8e4312e470f83fcb88df7e3e2
https://www.virustotal.com/gui/file/12cdbbad4169aa8414321dbf8b5fe92f8017bc88fe6ca596efd8ec11b0df93f8

All credits to FaceOff (the group that made the russian tools.) and [Cethleann]([url](https://github.com/yretenai/Cethleann)) (They documented the encryption used on P5S_EnDe.).

The process to edit the LINKDATA is kinda boring. (this probably could be fully automated if I knew programming...)

1 - This is only for the PC version. Use LD Ex & In.py to get the LINKDATA.IDX from the game.exe

2 - With LINKDATA.BIN and LINKDATA.IDX on the same folder, you can now use idx_export_switch.exe and wait until a notification in Russian warns you. (It probably says that the process ended.)

3 - If you're in the Switch version, you'll have a bunch of .struct/.bin, if you're in PC, you'll only have a bunch of .bins

On PC, you now have to use P5S_EnDe to decrypt the .bins. Just open it and follow the instructions.

4 - Before doing the main step here, save the files: 8158.struct, 8168.struct and 8178.struct. (They are separated for some reason, but it is the street talk, phone messages and cutscene subtitles.)

To make it easier to navigate in this shit-ton of files, you can put Delete_OtherLanguages.py on the folder where the .bins are, open the PowerShell/CMD and execute it with the command "Py Delete_OtherLanguages.py".

(This will delete every file that isn't 0 or a multiple of 8, including the tool, as they seem to be every english file other than the ones I talked about.)

(I don't know what happens if you just open it without PowerShell/CMD.) (You can do this step before decrypting the files.)

5 - After this, you'll have .Structs that can be turned to .TXTs with P5S_struct_Export.exe.

6 - The texts files of this game have a lot of trash. I did 2 Text Simplification tools. You can use Text-Simplification to select 1 or more .TXTs to make a .TSV sheet.

The new texts must be inserted on the D row.

After that, Simplification-Import can be used to import the texts back to each .TXT.

7 - Having the .struct.txt and .struct files on the same folder, use P5S_struct_Import.exe to get everything back to .structs.

8 - Use P5S_EnDe to encrypt every .struct back to .bin. (Only for the PC version.)

9 - Download (yes, other tool, sorry.) [this]([url](https://gbatemp.net/threads/dragon-quest-builders-2.528161/post-8466669)).

10 - Use the command on Inject Command.txt. (The folder where the .bins are is set to a folder called NEW, change it to whatever your folder is called.)

The program linkdata.exe and this command must be on the same folder as the LINKDATA.BIN/IDX

It's a PowerShell command. If you don't have PowerShell... I don't know, sorry.

11 - If you're editing the Switch version, nothing more is needed, it's probably good to go. On the PC version, use LD Ex & In.py to inject the IDX back to .exe.

I guess that this is all, if I forgot anything, I'll probably remember later...
