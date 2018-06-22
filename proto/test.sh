#!/bin/bash

mysql_root_passwd='Cmsy_67775853'
mysql_newuser='chuangmi'
mysql_newuser_passwd='Cmsy_67775853'

echo "start install mysql"
rpm -Uvh mysql57-community-release-el7-11.noarch.rpm
yum clean all
sleep 2
yum install mysql-community-server -y
/usr/bin/systemctl start mysqld
chkconfig --level 2345 mysqld on
for i in `grep 'temporary password' /var/log/mysqld.log| awk -F": " '{print $2}'`;
    do
        mysql -uroot -p$i -e "set global validate_password_policy=0;" -b --connect-expired-password
        mysql -uroot -p$i -e "set global validate_password_length=6;" -b --connect-expired-password
        mysql -uroot -p$i -e "ALTER USER 'root'@'localhost' IDENTIFIED BY '$mysql_root_passwd';" -b --connect-expired-password
        /usr/bin/mysqladmin -u root -p$i  password ${mysql_root_passwd} -b
        mysql -uroot -p"$mysql_root_passwd" -e "grant all privileges on *.* to '$mysql_newuser'@'%'identified by '$mysql_newuser_passwd' with grant option;" -b --connect-expired-password
        mysql -uroot -p"$mysql_root_passwd" -e "flush privileges;" -b --connect-expired-password
        mysql -uroot -p"$mysql_root_passwd" -e "show databases;"
done
echo "mysql is installed"
/usr/bin/systemctl restart mysqld

echo "start install nginx"
yum install openssl-devel -y
tar -zxf nginx-1.13.9.tar.gz
cd nginx-1.13.9
./configure --prefix=/usr/local/nginx --with-http_stub_status_module --with-http_ssl_module --with-stream
sudo useradd nginx
echo nginx | sudo passwd nginx --stdin  &>/dev/null
make
make install
cd ../
echo "nginx is installed"

echo "start install java"
mkdir /usr/java
tar -xzvf jdk-8u161-linux-x64.tar.gz -C /usr/java
echo "JAVA_HOME=/usr/java/jdk1.8.0_161" >> /etc/profile
echo "CLASSPATH=\$JAVA_HOME/lib/" >> /etc/profile
echo "PATH=\$PATH:\$JAVA_HOME/bin" >> /etc/profile
echo "export PATH JAVA_HOME CLASSPATH" >> /etc/profile
source /etc/profile
echo "java is installed"

exit