
/* sql queries for 'airports' sqlite database
   created by 'csv2sqlite.py'
    */

/* show the record that has the highest latitude in Japan */
SELECT * FROM 
       airports 
       	      WHERE lat = (
			SELECT MAX(lat) FROM airports
			       WHERE country = 'Japan'
			  );

/* show the records that have the highest latitude in each country 
   index on country raises the query speed
*/
/* correlated subquery is instructed in:
http://gihyo.jp/dev/serial/01/sql_academy2/000902 
*/

CREATE INDEX IF NOT EXISTS cntidx ON 
       airports(country); 
 
SELECT * FROM 
       	airports A1
		 WHERE lat = 
		 (SELECT MAX(lat) FROM
		 	 airports A2
			 WHERE A1.country = A2.country);


/* pattern match -- case insensitive */
/*  
http://stackoverflow.com/questions/15480319/case-sensitive-and-insensitive-like-in-sqlite
*/

SELECT * FROM airports
       	      WHERE country LIKE '%ja%';

/* How do I list the tables in a SQLite database file (after ATTACH command) */
/*
http://stackoverflow.com/questions/82875/how-do-i-list-the-tables-in-a-sqlite-database-file
*/
SELECT * FROM dbname.sqlite_master WHERE type='table';

/* attach another sqlite3 database */

ATTACH 'englishwordrank.sqlite3' AS wr;

/* joint a table with a table from another database */

SELECT  mylist.id, mylist.n, mylist.word, 
	wordrank.rank, wordrank.count 
		       FROM mylist, wr.wordrank 
		       	    WHERE mylist.word = wordrank.word;

