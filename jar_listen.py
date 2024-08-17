

print("默认监听端口5005")
port = 5005
jar_name = input("input  your jar name")
cmd = "java -Xdebug -Xrunjdwp:transport=dt_socket,address=5005,server=y,suspend=y -jar "