# 连接数据库

   ```shell
   sqlcmd -S 121.196.101.7 -Upython -p123456
   use master
   go
   select * from QunList where id = 1
   go
   ```
   用户名是python
   密码是123456
   数据库名称为QunList
   **数据库以Id,和QunNum作为索引,请不要用除此以外的任何字段作为where的判别条件**