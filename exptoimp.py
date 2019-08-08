# Imports a flat header file directly as labels
# Flat means no preprocessor macros or use of other defines
#@author Or Cyngiser
#@category Data
#@keybinding 
#@menupath 
#@toolbar 

f = askFile("Data type export file to open", "Make labels!")
for line in file(f.absolutePath):  # note, cannot use open(), since that is in GhidraScript
        if not len(line.split()) == 3:
            continue
	(_, name, loc) = line.split(' ')
	address = toAddr(long(hex(int(loc[:-1])), 16))
	print("creating symbol", name, "at address", address)
	createLabel(address, name, False)
