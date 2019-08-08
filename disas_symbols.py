# Force disassembly of function symbols
#@author Or Cyngiser
#@category Analysis
#@keybinding 
#@menupath 
#@toolbar 

from ghidra.program.model.symbol import *
from ghidra.program.model.address.Address import *
sm = currentProgram.getSymbolTable()
it = sm.getPrimarySymbolIterator(currentProgram.getMemory().getExecuteSet(), True)
for x in it: 
    if x.getSymbolType() == ghidra.program.model.symbol.SymbolType.FUNCTION:
        disassemble(x.getAddress())
    
