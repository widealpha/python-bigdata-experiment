# Hadoop

## 安装

在windows上的安装由于我的java安装目录有空格失败,转而用ubuntu虚拟机安装

1.安装必要的包(ssh和pdsh)

```bash
sudo apt-get install ssh
sudo apt-get install pdsh
```

2.接着下载并解压hadoop

```bash
wget https://mirrors.tuna.tsinghua.edu.cn/apache/hadoop/common/hadoop-3.3.1/hadoop-3.3.1.tar.gz
sudo tar -zxvf hadoop-3.3.1.tar.gz -C /usr/local
```

3.编辑hadoop解压目录下的 `etc/hadoop/hadoop-env.sh` 插入java安装位置(推荐1.8)

```
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
```

4. 测试安装结果

```bash
hadoop version
```

![image-20210702173503305](https://gitee.com/widealpha/pic/raw/master/image-20210702173503305.png)

## 运行实例

### Standalone Operation

执行以下命令，查看结果（在写实验报告的时候已经配置了分布）

```bash
mkdir input
cp etc/hadoop/*.xml input
bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.1.jar grep input output 'dfs[a-z.]+'
cat output/*
```

### Pseudo-Distributed Operation

1. 编辑下面两个文件

   etc/hadoop/core-site.xml:

   ```xml
   <configuration>
       <property>
           <name>fs.defaultFS</name>
           <value>hdfs://localhost:9000</value>
       </property>
   </configuration>
   ```

   etc/hadoop/hdfs-site.xml:

   ```xml
   <configuration>
       <property>
           <name>dfs.replication</name>
           <value>1</value>
       </property>
   </configuration>
   ```

2. 接着配置ssh环境

   ```bash
   ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
   cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
   chmod 0600 ~/.ssh/authorized_keys
   # 接着
   ssh localhost
   ```

3. 按照下面的命令运行节点

   ```bash
   bin/hdfs namenode -format
   sbin/start-dfs.sh
   ```

4. 访问`127.0.0.1:9870`

   这儿由于我是linux服务器虚拟机，所以采用了内网ip `192.168.116.128:9870`

   ![image-20210702174744903](https://gitee.com/widealpha/pic/raw/master/image-20210702174744903.png)

5. 执行mapreduce工作

   ```bash
   bin/hdfs dfs -mkdir /user
   bin/hdfs dfs -mkdir /user/hadoop
   
   bin/hdfs dfs -mkdir input
   bin/hdfs dfs -put etc/hadoop/*.xml input
   bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.1.jar grep input output 'dfs[a-z.]+'
   
   bin/hdfs dfs -get output output
   cat output/*
   ```

   ![执行结果](https://gitee.com/widealpha/pic/raw/master/image-20210702175224436.png)

6. 最后处理完工作，关闭节点

   ```bash
   sbin/stop-dfs.sh
   ```

   ![image-20210702175341596](https://gitee.com/widealpha/pic/raw/master/image-20210702175341596.png)

### YARN on a Single Node

1. 编辑如下文件

   `etc/hadoop/mapred-site.xml`:

   ```xml
   <configuration>
       <property>
           <name>mapreduce.framework.name</name>
           <value>yarn</value>
       </property>
       <property>
           <name>mapreduce.application.classpath</name>
           <value>$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*</value>
       </property>
   </configuration>
   ```

   `etc/hadoop/yarn-site.xml`:

   ```xml
   <configuration>
       <property>
           <name>yarn.nodemanager.aux-services</name>
           <value>mapreduce_shuffle</value>
       </property>
       <property>
           <name>yarn.nodemanager.env-whitelist</name>
           <value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_HOME,PATH,LANG,TZ,HADOOP_MAPRED_HOME</value>
       </property>
   </configuration>
   ```

2. 启动yarn

   ```bash
    sbin/start-yarn.sh	
   ```

   ![image-20210702175916829](https://gitee.com/widealpha/pic/raw/master/image-20210702175916829.png)

3. 访问 `127.0.0.1:8088`

   访问成功yarn配置完成

   ![image-20210702180006553](https://gitee.com/widealpha/pic/raw/master/image-20210702180006553.png)