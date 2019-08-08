# Rebases thumb function name symbols by subtracting 1
#@author  Or Cyngiser
#@category Analysis
#@keybinding 
#@menupath 
#@toolbar 

from ghidra.program.model.symbol import *
from ghidra.program.model.address.Address import *
sm = currentProgram.getSymbolTable()
sym_list = []
it = sm.getPrimarySymbolIterator(currentProgram.getMemory().getExecuteSet(), True)
for sym in it:
	sym_list.append(sym)

for symbol in sym_list:
	addr_int =   int(str(symbol.getAddress()), 16)
	if addr_int % 2 == 1 and symbol.getSymbolType() == ghidra.program.model.symbol.SymbolType.FUNCTION:
		new_addr = symbol.getAddress().getNewAddress(addr_int - 1)
		for symbol_to_delete in sm.getSymbols(new_addr):
			print("removing symbol : %s" % symbol_to_delete)
			sm.removeSymbolSpecial(symbol_to_delete)
		sm.moveSymbolsAt(symbol.getAddress(), new_addr)
		print("moved symbol: %s" % symbol)
