import subprocess

print('$ nslookup www.ptyhon.org')

r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

