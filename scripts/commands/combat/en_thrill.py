import sys

def setup(core, actor, target, command):
	core.buffService.addBuffToCreature(target, 'en_debuff_thrill')
	return
	
def preRun(core, actor, target, command):
	return

def run(core, actor, target, commandString):
	return