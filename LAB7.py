N1
hashes = ("abc123", "ffd222", "9af010", "ffd222", "x0x0x0")
print(hashes.count("ffd222"))
N2
users = ("guest", "moderator", "admin", "root")
print(users.index("admin"))
N3
key_params = ("AES", 256, "CBC")
algorithm, key_size, mode=key_params
print("Algorithm:",algorithm)
print("Key size:",key_size)
N4
log = ("login", "download", "upload", "logout")
print(log[-1])
N5
ip=input("Введите IP:")
ips = ("192.168.0.1", "10.0.0.2", "172.16.0.3")
if ip in ips:
    print("Найдено")
else:
    print("Нет в списке")
N6
name=input("Введите имя:")
role=input("Введите роль:")
status=input("Введите статус:")
t=(name,role,status)
print(t)
N7
access = ("read", "write", "execute")
new_value = input("Введите новое значение для второго элемента: ")
new_access = (access[0], new_value, access[2])
print(new_access)
N8
attempts = ("success", "fail", "fail", "success", "fail", "fail")
print("success:",attempts.count("success"))
print("fail:",attempts.count("fail"))
N9
admins = ("root", "admin")
users = ("alex", "bob")
new=admins+users
print(new)
N10
logs = ("login", "upload", "download", "logout")
start=logs[0]
middle=logs[1:-1]
end =logs[-1]
print("Start:",start)
print("Middle:",middle)
print("End:",end)