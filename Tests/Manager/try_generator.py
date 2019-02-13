a = [{'group': {'groupId': '850fb30b-c205-4fd1-8d38-01033a68b5af'}, 'roles': [{'roleId': '454a2e9f-2c87-478f-a49c-dcb58bfd0ee3'}], 'applyRolesRecursively': False}]

z = {(key, val) for key, val in set(a[0]['roles'][0].items()) | set(a[0]['group'].items())}
z2 = set(a[0]['roles'][0].items() | a[0]['group'].items())

b = [{'group': {'name': 'hmSFY52J18', 'groupId': '850fb30b-c205-4fd1-8d38-01033a68b5af'}, 'roles': [{'name': 'lYSNUoOlg', 'system': False, 'roleId': '454a2e9f-2c87-478f-a49c-dcb58bfd0ee3'}]}]




x = {(key, val) for key, val in set(b[0]['group'].items()) | set(b[0]['roles'][0].items())}

print("x", x)

print("z", z)
print("z2", z2)
print(z.issubset(x))
