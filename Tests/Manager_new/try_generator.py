a = [{'group': {'groupId': 'fddd4e7c-1363-49c5-9b65-faf23c6ab386'}, 'roles': [{'roleId': '8e9069c9-9015-4204-93b9-531d14985b71'}], 'applyRolesRecursively': False}]

z = [(key, val) for key, val in set(a[0]['roles'][0].items()) | set(a[0]['group'].items())]

print(z)