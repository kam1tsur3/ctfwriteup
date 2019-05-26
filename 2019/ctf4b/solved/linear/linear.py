import angr
proj = angr.Project("./linear_operation")

target_addr = 0x40cf78

state = proj.factory.entry_state()
simgr = proj.factory.simgr(state)
simgr.explore(find=target_addr)
state = simgr.found[0]

print(state.posix.dumps(0))

#this is template

