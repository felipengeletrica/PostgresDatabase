# PostgresDatabase
This program implements multiple instances Postgres Database manipulation CRUD

#### Create database using psql (terminal)

Postgres documentation: <br/>
https://www.postgresql.org/docs/manuals/
######Now create databases

Connecting after install:<br/>
root@debian-laptop:/# su postgres<br/>
postgres@debian-laptop:/$ psql<br/>
psql (9.4.11)<br/>
type "help" for help.<br/>

postgres=# <br/>

#### Now create two database for test:<br/>
CREATE DATABASE<br/>

postgres=# CREATE DATABASE dbMainDatacenter;<br/>
CREATE DATABASE<br/>
postgres=# CREATE DATABASE dbSecondaryDatacenter;<br/>

##### Create users 

postgres=# CREATE USER dbmainuser WITH PASSWORD 'root';<br/>
postgres=# GRANT ALL PRIVILEGES ON DATABASE dbMainDatacenter to dbmainuser;<br/>


postgres=# CREATE USER dbmainuser WITH PASSWORD 'root';<br/>
postgres=# GRANT ALL PRIVILEGES ON DATABASE dbSecondaryDatacenter to dbmainuser;<br/>


List databases:<br/>
postgres=# \l


##### Set database 
postgres=# \c dbmaindatacenter
##### Create table:<br/>
CREATE TABLE tb_temperature<br/>
(<br/>
 <t/><t/><t/>id serial NOT NULL,<br/>
 <t/><t/><t/> temperature float NOT NULL,<br/>
 <t/><t/><t/> "timestamp" timestamp without time zone NOT NULL DEFAULT now()<br/>
);<br/>


##### Set database 
dbmaindatacenter-# \c dbsecondarydatacenter

CREATE TABLE tb_temperature<br/>
(<br/>
  <t/><t/><t/>id serial NOT NULL,<br/>
  <t/><t/><t/>temperature float NOT NULL,<br/>
  <t/><t/><t/>"timestamp" timestamp without time zone NOT NULL DEFAULT now()<br/>
);<br/>


#### At the moment two database and two identical tables are created !

### Now testing python code...

Install psycopg2 after 

In terminal type:<br/>

$python main.py<br/>







