1

-----

Write a query that shows all the information about all the salespeople in
the database. Use a basic SELECT query.

-----

SELECT * from salespeople


==========
2

-----

Write a query that shows all the information about all salespeople from
the 'Northwest' region.

-----

SELECT * FROM salespeople WHERE region='Northwest';


==========
3

-----

Write a query that shows just the emails of the salespeople from the
'Southwest' region.

-----

SELECT email from salespeople where region = 'Southwest';


==========
4

-----

Write a query that shows the given name, surname, and email of all
salespeople in the 'Northwest' region.

-----

SELECT givenname, surname, email FROM salespeople WHERE region='Northwest';


==========
5

-----

Write a query that shows the common name of melons that cost more than
$5.00.

-----

select common_name from melons where price > 5.0


==========
6

-----

Write a query that shows the melon type and common name for all
watermelons that cost more than $5.00.


-----

SELECT melon_type, common_name FROM melons WHERE (melon_type='Watermelon' AND price>5);


==========
7

-----

Write a query that displays all common names of melons that start with
the letter 'C'.


-----

select common_name from melons where common_name like "C%";


==========
8

-----

Write a query that shows the common name of any melon with 'Golden'
anywhere in the common name.


-----

SELECT common_name FROM melons WHERE common_name like '%Golden%';


==========
9

-----

Write a query that shows all the distinct regions that a salesperson can belong to.


-----

select distinct region from salespeople


==========
10

-----

Write a query that shows the emails of all salespeople from both the
Northwest and Southwest regions.


-----

SELECT email FROM salespeople WHERE (region='Northwest') OR (region='Southwest');


==========
11

-----

Write a query that shows the emails of all salespeople from both the
Northwest and Southwest regions, this time using an 'IN' clause.  


-----

select email from salespeople where region in ('Northwest', 'Southwest');


==========
12

-----

Write a query that shows the email, given name, and surname of all
salespeople in either the Northwest or Southwest regions whose surnames start
with the letter 'M'.

-----

SELECT email, givenname, surname FROM salespeople WHERE (surname like 'M%') AND region IN ('Northwest', 'Southwest');


==========
13

-----

Write a query that shows the melon type, common name, price, and the
price of the melon given in euros. The 'melons' table has prices in dollars,
and the dollar to euro conversion rate is 0.735693.


-----

select melon_type, common_name, price as Price_dollars, (price * 0.735693) as Price_euros from melons


==========
14

-----

Write a query that shows the total number of customers in our customer
table.

-----

SELECT COUNT(*) FROM customers;


==========
15

-----

Write a query that counts the number of orders shipped to California.

-----

select count(*) from orders where shipto_state = 'CA';


==========
16

-----

Write a query that shows the total amount of money spent across all melon
orders.

-----

SELECT SUM(order_total) FROM orders;


==========
17

-----

Write a query that shows the average order cost.

-----

select AVG(order_total) from orders


==========
18

-----

Write a query that shows the order total that was lowest in price.

-----

SELECT order_total FROM orders ORDER BY order_total LIMIT 1;


==========
19

-----

Write a query that fetches the id of the customer whose email is 
'phyllis@demizz.edu'.

-----

select id from customers where email = 'phyllis@demizz.edu';


==========
20

-----

Write a query that shows the id, status and order_total for all orders 
made by customer 100.

-----

SELECT id, status, order_total FROM orders WHERE customer_id=100;


==========
21

-----

Write a single query that shows the id, status, and order total for all
orders made by 'phyllis@demizz.edu'. Use a subselect to do this.


-----

select id, status, order_total from orders where customer_id = (select id from customers where email = 'phyllis@demizz.edu');


==========
22

-----

Write a query that shows the id, status, and order total for all orders
made by 'phyllis@demizz.edu'. Use a join to do this.

-----

select orders.id, orders.status, orders.order_total from orders join customers on (orders.customer_id=customers.id) where customers.email='phyllis@demizz.edu';


==========
23

-----

Write a query that shows all columns that were attached to order #2725.

-----

select * from order_items where order_id = 2725


==========
24

-----

Write a query that shows the common_name, melon_type, quantity,
unit_price and total_price for all the melons in order #2725.

-----

SELECT m.common_name, m.melon_type, oi.quantity, oi.unit_price, oi.total_price FROM melons AS m JOIN order_items AS oi ON (m.id=oi.melon_id) WHERE oi.order_id=2725;


==========
25

-----

Write a query that shows the total amount of revenue that comes from
internet orders.

-----

Select sum(order_total) from orders where salesperson_id is NULL;


==========
26

-----

Challenge: Produce a list of all salespeople and the total amount of orders
they've sold, while calculating a 15% commission on all of their orders.
Include their given name, surname, the total of all their sales, and their
commission. Only report one row per salesperson. Include salespeople who have
not made any sales.

You will need 'left join' (http://sqlzoo.net/wiki/LEFT_JOIN) and 'group by'
(http://sqlzoo.net/wiki/SELECT_.._GROUP_BY) clauses to finish this one.

-----

SELECT sp.givenname, sp.surname, sum(o.order_total) as total_of_sales, (sum(o.order_total)*0.15) as commission FROM salespeople as sp LEFT JOIN orders as o ON (sp.id=o.salesperson_id) WHERE o.salesperson_id is not NULL GROUP BY o.salesperson_id;