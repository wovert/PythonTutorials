import subprocess

# dir命令，系统命令，
res = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# windows控制台字符编码是gbk
out = res.stdout.read().decode('GBK')
err = res.stderr.read().decode('GBK')

print('stdout:', out)
print('stderr:', err)