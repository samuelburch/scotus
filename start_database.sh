docker rm -f scotusdb:0.0
docker build -t scotusdb:0.0 ./mariadb
docker run -d -v scotus:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=password --name scotusdb scotusdb:0.0 --sql-mode=""