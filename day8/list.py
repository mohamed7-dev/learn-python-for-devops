servers = ["app_server_1","app_server_2","app_server_3"]

print(servers)

servers.append("app_server_5")
servers.remove("app_server_5")

# similar to at(-1) in js 
print(servers[-1])
print(servers[0])
print(len(servers))
# in python + concatenates lists, too 
print(servers + ["app_server_5"])
# this is similar to slice() in js
print(servers[1:3])

# Checks if an item is in the list
is_present = 'app_server-6' in servers  
print(is_present)