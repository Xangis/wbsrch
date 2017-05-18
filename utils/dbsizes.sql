SELECT pg_size_pretty(pg_database_size('indexes')) as indexes_size;
SELECT pg_size_pretty(pg_database_size('zetaweb')) as zetaweb_size;
SELECT pg_size_pretty(pg_database_size('urls')) as urls_size;
