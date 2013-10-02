
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

/* show the records that have the highest latitude in each country */
/* correlated subquery is instructed in:
http://gihyo.jp/dev/serial/01/sql_academy2/000902 
*/
 
SELECT * FROM 
       	airports A1
		 WHERE lat = 
		 (SELECT MAX(lat) FROM
		 	 airports A2
			 WHERE A1.country = A2.country);


