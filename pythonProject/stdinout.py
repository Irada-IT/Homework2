import subprocess

result = subprocess.run(['ping', '-c', '3', '-n', 'yandex.ru'], encoding='utf-8', stdout=subprocess.PIPE)
print(result.stdout)