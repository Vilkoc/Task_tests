# Task_tests

1. Install java 8, postgreSQL (with pgAdmin), project (RabotyNET, front), NodeJS
1.5 Download apach-tomcat-9.0.10
2. put project in ...\apache-tomcat-9.0.10\webapps + extracted front
3. add path:JAVA_HOME for tomcat set "CURRENT_DIR=C:\SoftServ\soft\apache-tomcat-9.0.10"
3.5 create database in pgAdmin for project (rabotaNET)
4. postgreSQL set password "root" (for RabotyNET). Or change password in tomcat/webapps/APP/WEB-INF/classes/database.properties
5. nmp install
6.1. into tomcat/bin "startup" // start tomcat-server
6.2. into tomcat/webapps/front run "ng serve" // initialize project
7. open http://localhost:4200/
