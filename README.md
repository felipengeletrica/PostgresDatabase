# PostgresDatabase
This program implements multiple instances Postgres Database manipulation CRUD

#### Create database using PgAdmin III ou terminal

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

List databases:<br/>
postgres=# \l



postgres=#\connect dbMainDatacenter

##### Create tables:<br/>
CREATE TABLE dbMainDatacenter.tb_temperature<br/>
(<br/>
 <t/><t/><t/>id serial NOT NULL,<br/>
 <t/><t/><t/> temperature float NOT NULL,<br/>
 <t/><t/><t/> "timestamp" timestamp without time zone NOT NULL DEFAULT now()<br/>
);<br/>


postgres=#\connect dbSecondaryDatacenter

CREATE TABLE dbSecondaryDatacenter.tb_temperature<br/>
(<br/>
  <t/><t/><t/>id serial NOT NULL,<br/>
  <t/><t/><t/>temperature float NOT NULL,<br/>
  <t/><t/><t/>"timestamp" timestamp without time zone NOT NULL DEFAULT now()<br/>
);<br/>


