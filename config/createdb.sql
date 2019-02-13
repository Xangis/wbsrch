create database zetaweb;
create database urls;
create database indexes;
create database news;
create user zetaweb with password 'd9irk0kfnv,er9kd2';
alter user zetaweb createdb;
grant all on database zetaweb to zetaweb;
grant all on database urls to zetaweb;
grant all on database indexes to zetaweb;
grant all on database news to zetaweb;
alter database zetaweb owner to zetaweb;
alter database urls owner to zetaweb;
alter database indexes owner to zetaweb;
alter database news owner to zetaweb;

