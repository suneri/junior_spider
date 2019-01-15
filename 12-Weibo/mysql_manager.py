import mysql.connector
from mysql.connector import errorcode
from mysql.connector import pooling
import time 

import re

class MysqlManager:
    
    dbconfig = {
        "database": "weibo",
        "user":     "root",
        "password": "password",
        "host":     "localhost"
    }

    TABLES = {}
    TABLES['post'] = (
        "CREATE TABLE `post` ("
        "  `id` bigint NOT NULL,"
        "  `user_id` bigint NOT NULL,"
        "  `text` varchar(160) NOT NULL,"
        "  `screen_name` varchar(32) NOT NULL,"
        "  `reposts_count` int NOT NULL,"
        "  `comments_count` int NOT NULL,"
        "  `attitudes_count` int NOT NULL,"
        "  `profile_image_url` varchar(320) NOT NULL DEFAULT '',"
        "  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,"
        "  `queue_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,"
        "  PRIMARY KEY (`id`)"
        ") ENGINE=InnoDB")

    TABLES['pic'] = (
        "CREATE TABLE `pic` ("
        "  `post_id` bigint NOT NULL,"
        "  `url` varchar(1024) NOT NULL,"
        "  UNIQUE (`url`)"
        ") ENGINE=InnoDB")

    TABLES['comment'] = (
        "CREATE TABLE `comment` ("
        "  `post_id` bigint NOT NULL,"
        "  `id` bigint NOT NULL,"
        "  `user_id` bigint NOT NULL,"
        "  `text` varchar(160) NOT NULL,"
        "  `screen_name` varchar(32) NOT NULL,"
        "  `profile_image_url` varchar(320) NOT NULL DEFAULT '',"
        "  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,"
        "  PRIMARY KEY (`id`)"
        ") ENGINE=InnoDB")

    def __init__(self, max_num_thread):
        try:
            cnx = mysql.connector.connect(host=self.dbconfig['host'], user=self.dbconfig['user'], password=self.dbconfig['password'])
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print('Create Error ' + err.msg)
            exit(1)

        cursor = cnx.cursor()

        try:
            cnx.database = self.dbconfig['database']
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.create_database(cursor)
                cnx.database = self.dbconfig['database']
                self.create_tables(cursor)
            else:
                print(err)
                exit(1)
        finally:
            cursor.close()
            cnx.close()

        self.cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "mypool",
                                                          pool_size = max_num_thread,
                                                          **self.dbconfig)


    def create_database(self, cursor):
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(self.dbconfig['database']))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)

    def create_tables(self, cursor):
        for name, ddl in self.TABLES.items():
            try:
                cursor.execute(ddl)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print('create tables error ALREADY EXISTS')
                else:
                    print('create tables error ' + err.msg)
            else:
                print('Tables created')

    # Give a create table sql, return its columns
    def get_table_column_keys(self, sql):
        return re.findall(r'\s\s\`(.*?)\`\s', sql)

    def get_insert_sql(self, table_name, data):
        columns = self.get_table_column_keys(self.TABLES[table_name])

        sql0 = 'INSERT INTO {}('.format(table_name)
        sql1 = 'VALUES ('

        for col in columns:
            if col in data:
                sql0 += col + ','
                sql1 += "'{}',".format(data[col])
        
        sql0 = sql0[:-1]
        sql1 = sql1[:-1]

        return sql0 + ')' + sql1 + ')'

    def insert_data(self, table_name, data):
        con = self.cnxpool.get_connection()
        cursor = con.cursor()
        try:
            sql = self.get_insert_sql(table_name, data)
            print(sql)
            cursor.execute((sql))
            con.commit()
        except mysql.connector.Error as err:
            print('insert_data() ' + err.msg)
            # print("Aready exist!")
            return
        finally:
            cursor.close()
            con.close()

if __name__ == "__main__":
    mysql_mgr = MysqlManager(8)