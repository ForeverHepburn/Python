import os

print('Progress (%s) start...' % os.getpid())

pid = os.fork()
if pid == 0:
	print('I am child progres (%s) and my parent is %s.' % (os.getpid(), os.getpid()))
else:
	print('I (%s) just created a child progres (%s)' % (os.getpid(), pid))
