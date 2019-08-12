# Converts a jtl jump into a tjex r3 instruction to just a tjex r3, making variable-dependent calls much cleaner.
#@author Or Cyngiser
#@category Instructions
#@keybinding 
#@menupath 
#@toolbar 

tjex_r3_instr = [24,7,-64,70]

def instr_gen():
	instr = getFirstInstruction()
	yield instr
	while getInstructionAfter(instr):
		instr = getInstructionAfter(instr)
		yield instr
	raise StopIteration()
    
q = ghidra.app.script.GhidraScript
for instruction in instr_gen():
	try:
		if instruction.getMnemonicString() == u'tjl' and list(q.getBytes(ghidra.program.flatapi.FlatProgramAPI(currentProgram),currentAddress.getNewAddress(int(str(instruction).split(' ')[-1],16)), 4)) == tjex_r3_instr:
			print 'Instruction fixup at : {}'.format(instruction.getAddress())
			q.removeInstructionAt(ghidra.program.flatapi.FlatProgramAPI(currentProgram), instruction.getAddress())
			q.setBytes(ghidra.program.flatapi.FlatProgramAPI(currentProgram),instruction.getAddress(),tjex_r3_instr)
			q.disassemble(ghidra.program.flatapi.FlatProgramAPI(currentProgram), instruction.getAddress())
	except ghidra.program.model.mem.MemoryAccessException, e:
		continue


