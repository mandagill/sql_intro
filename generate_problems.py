import pickle
from sql_problem import result_to_str, generate_result_hash
import sql_problem

PROBLEMS = [
{   # Problem 1 -- a basic select
"instruction": 
"""The 'select' is the basic query. We use it to extract information from a
table. There are a number of clauses to a select statement. Right now, we'll
concern ourself with just two: the column list and the table you are querying.

The format of the basic select statement is

    SELECT <column list> FROM <table name>;

For now, we can use the wildcard '*' (without quotes) to select all columns
from a given table.

Examples: http://sqlzoo.net/wiki/SELECT_from_WORLD_Tutorial -- 1

Task: Write a query that shows all the information about all the salespeople in
the database. Use a basic SELECT query.
""",
"hint": """Select all the columns from the 'salespeople' table.""",
"solution": """SELECT * FROM salespeople;"""
},

{   # Problem 2 -- select with a where clause
"instruction":
"""Select statements can have an additional clause called the 'where' clause.
This lets us extract specific rows out of our table. Our where clause can be
specific enough to match a single row, or general enough to match a set of
rows. The format of a select statement with a 'where' clause is:

    SELECT <column list> FROM <table name> WHERE <equality expression>;

Examples: http://sqlzoo.net/wiki/SELECT_basics -- 1

Task: Write a query that shows all the information about all salespeople from
the 'Northwest' region.
""",
"hint": """Select all the columns from the 'salespeople' table where the region
matches the string 'Northwest'.""",
"solution": """SELECT * FROM salespeople WHERE region = 'Northwest';"""
},

{   # Problem 3 -- select individual columns
"instruction":
"""We've been selecting all the columns out of our table up until now, but the
amount of data can be overwhelming. We can use the column list to specify
individual columns. We do this by specifying the column list as a single column
name instead of a '*'.

Examples: http://sqlzoo.net/wiki/SELECT_from_WORLD_Tutorial -- 1

Task: Write a query that shows just the emails of the salespeople from the
'Southwest' region.
""",
"hint": """Select the email column from the 'salespeople' table where the
region matches the string 'Southwest'.""",
"solution":  """SELECT email FROM salespeople WHERE region = 'Southwest';"""
},

{   # Problem 4 -- select more than one column
"instruction":
"""We can ask for more than one column from the data set by specifying all the
columns separated by commas.

Examples: http://sqlzoo.net/wiki/SELECT_from_Nobel_Tutorial -- 1, 2
          http://sqlzoo.net/wiki/SELECT_from_WORLD_Tutorial -- 1

Task: Write a query that shows the given name, surname, and email of all
salespeople in the 'Northwest' region.
""",
"hint": """Select the givenname, surname, and email column from the
'salespeople' table where the region matches the string 'Northwest'.""",
"solution": """SELECT givenname, surname, email FROM salespeople WHERE region = 'Northwest';"""
},

{   # Problem 5 -- inequality query
"instruction":
"""In addition to finding exact matches, we can specify the where clause of our
query to match a range of columns using inequalities.

Examples: http://sqlzoo.net/wiki/SELECT_basics -- 2, 3
          http://sqlzoo.net/wiki/SELECT_from_WORLD_Tutorial -- 2

Task: Write a query that shows the common name of melons that cost more than
$5.00.
""",
"hint": """Select the common_name column from the 'melons' table where the
price column is greater than 5.0.""",
"solution": """SELECT common_name FROM melons WHERE price > 5.0;"""
},

{   # Problem 6 -- and clause
"instruction":
"""Sometimes, we want to filter down our matched rows even further. We can add
additional restrictions to our query using an 'and' clause. It looks like this:

    SELECT <column list> FROM <table> WHERE <expression 1> AND <expression 2>;

Examples: http://sqlzoo.net/wiki/SELECT_basics -- 3, 6

Task: Write a query that shows the melon type and common name for all
watermelons that cost more than $5.00.
""",
"hint": """Select the melon_type and common_name columns from the 'melons'
table where the price is greater than or equal to 5.0 and the melon_type is
'Watermelon'. """,
"solution": """SELECT melon_type, common_name FROM melons WHERE price >= 5.0 AND melon_type = 'Watermelon';"""
},

{   # Problem 7 -- like clause, simple wildcard
"instruction":
"""Using inequalities on numeric columns lets us match a range of rows.
Similarly, we can use a string wildcard to do matches on ranges of strings.
Confusingly, the string wildcard is '%', which is different from the column
wildcard, which is '*'. Additionally, you can't use an equality to match a
string wildcard, you have to use a 'like' clause instead. The format is as
follows:

    <column_name> LIKE "<match string with wildcards>"
    
Examples: http://sqlzoo.net/wiki/SELECT_basics -- 5

Task: Write a query that displays all common names of melons that start with
the letter 'C'.
""",
"hint": """Select the common_name column from the 'melons' table where the
common name is like the letter 'C' followed by a wildcard.""",
    "solution": """SELECT common_name FROM melons WHERE common_name LIKE 'C%';"""
},

{   # Problem 8 -- more complex wildcard
"instruction": 
"""String wildcards can be places anywhere in a string, allowing you to match
complex patterns. For example, the string pattern 'W%termelon%' matches the
strings 'Watermelon', 'Wintermelon', 'Watermelons', and 'Wintermelons'.
    
Examples: http://sqlzoo.net/wiki/SELECT_basics -- 5

Task: Write a query that shows the common name of any melon with 'Golden'
anywhere in the common name.
""",
"hint": """Select the common_name column from the 'melons' table where the
common name is like the word 'Golden', surrounded on either side by a
wildcard.""",
    "solution": """SELECT common_name FROM melons WHERE common_name LIKE '%Golden%';"""
},

{   # Problem 9 -- distinct keyword
"instruction":
"""Frequently, you will encounter duplicate data across multiple rows. In our
salespeople table schema, we can see that each one is attached to a specific
'region'. If we query that table for all the different regions that are used,
sql will return duplicates, one for each salesperson in our table.

To counter this, we can use the 'distinct' keyword. In our column list, we can
prepend the keyword to the column name.

Examples: http://sqlzoo.net/wiki/Using_SUM,_Count,_MAX,_DISTINCT_and_ORDER_BY -- 2
          http://sqlzoo.net/wiki/SUM_and_COUNT -- 2

Task: Write a query that shows all the distinct regions that a salesperson can belong to.
""",
"hint": """Select the distinct entries in the region column from the 'salespeople' table. """,
    "solution": """SELECT DISTINCT region FROM salespeople;"""
},

{   # Problem 10 -- 'or' clause
"instruction": 
"""Earlier, we used the 'and' keyword to narrow down our query: we made our
search more specific. We can use the 'or' keyword in exactly the opposite way,
to make our search match more rows.

Example: http://sqlzoo.net/wiki/SELECT_basics -- 6

Task: Write a query that shows the emails of all salespeople from both the
Northwest and Southwest regions.
""",
"hint": """Select the email column from the 'salespeople' table where the
region is either 'Northwest' or 'Southwest'. Use the 'or' clause to do
that.""",
    "solution": """SELECT email FROM salespeople WHERE region = 'Northwest' OR region = 'Southwest';"""
},

{   # Problem 11 -- 'in' clause
"instruction": 
"""It can be tedious to match a single column against multiple options. In our
previous exercise, we searched for the region to match both 'Northwest' and
'Southwest'. If we had more options we were trying to match, this would make
our query very long. We can use an 'in' clause to write this kind of query more
succinctly. We can replaces a series of 'or' clauses with a single 'in' clause
that takes the following format:

    <column name> IN (<option1>, <option2>, <...>)

Example: http://sqlzoo.net/wiki/SELECT_basics -- 4
    
Task: Write a query that shows the emails of all salespeople from both the
Northwest and Southwest regions, this time using an 'IN' clause.  
""",
"hint": """Select the email column from the 'salespeople' table where the
region is in the list of 'Northwest' and 'Southwest'. Use the 'in' clause.""",
"solution": """SELECT email FROM salespeople WHERE region IN ('Northwest', 'Southwest');"""
},

{   # Problem 12 -- combining column selection, in clause, and wildcards
"instruction": 
"""Using all these tools, we can bring them together to do fairly complex
queries that match many different rows. Using what you've learned, write a
query that combines column selection, an 'in' clause, and string wildcards.

Task: Write a query that shows the email, given name, and surname of all
salespeople in either the Northwest or Southwest regions whose surnames start
with the letter 'M'.
""",
"hint": """Select the email, givenname, and surname column from the
'salespeople' table where the region is in the list of 'Northwest', and
'Southwest', and where the surname matches the character 'M' followed by a
wildcard.""",
"solution": """SELECT email, givenname, surname FROM salespeople WHERE region IN ('Northwest', 'Southwest') AND surname LIKE 'M%';"""
},

{   # Problem 13 -- computed columns
    # Show the price in euros
"instruction": """An odd feature of sql is the ability to select data out of a
table that doesn't actually exist. Certain kinds of data can be computed on the
fly and be made to look as if they were part of the table. We'll use this to
query for melon price in USD and EUR, where one column will be computed from
the other.

Examples: http://sqlzoo.net/wiki/SELECT_basics -- 2

Task: Write a query that shows the melon type, common name, price, and the
price of the melon given in euros. The 'melons' table has prices in dollars,
and the dollar to euro conversion rate is 0.735693.
""",
"hint": """Select the melon_type, common_name, price, and a computed column
which is the price multiplied by the value .735693 from the table 'melons'.""",
"solution": """SELECT melon_type, common_name, price, price*.735693 FROM melons;"""
},

{   # Problem 14 -- aggregate functions, count
    #-> How many customers do we have?
"instruction": 
"""Similar to the 'computed' columns, SQL has a set of predefined 'aggregate'
functions that operate on an entire set of matched rows. Aggregate functions
condense a set of rows into a single row. An example of this kind of aggregate
operation is a 'count'. It simply counts up all the matched rows and returns a
single record in their place.

Example: http://sqlzoo.net/wiki/The_nobel_table_can_be_used_to_practice_more_SUM_and_COUNT_functions. -- 1

Task: Write a query that shows the total number of customers in our customer
table.
""",
"hint": """Select the count of all the columns from the table 'customers'. """,
"solution": """SELECT count(*) FROM customers;"""
},

{   # Problem 15 -- aggregate functions with where clauses
# -> How many orders were shipped to California?
"instruction": 
"""We can combine aggregate functions with the standard SQL clauses we've seen
so far. In this exercise, you will combine a count clause with a where clause
to limit what is counted.

Task: Write a query that counts the number of orders shipped to California.
""",
"hint": """Select the count of all the columns from the table 'orders' where
the shipto_state is 'CA'.""",
"solution": """SELECT count(*) FROM orders WHERE shipto_state = 'CA';"""
},

{   # Problem 16 -- sum function
    # -> dollar total for all orders
"instruction": 
"""Aggregate functions work on column lists. When we're counting things, it
doesn't matter which column we count, there should be the same number of each
column across all the records. For this reason, it is customary to execute the
count on all the columns in the query. With other aggregate functions, the
column we use can be meaningful, for example, if we are totaling up the values
in a single column.

Examples: http://sqlzoo.net/wiki/SUM_and_COUNT -- 1
          http://sqlzoo.net/wiki/The_nobel_table_can_be_used_to_practice_more_SUM_and_COUNT_functions. -- 3

Task: Write a query that shows the total amount of money spent across all melon
orders.
""",
"hint": """Select the sum of the order_total column from the table 'orders'.""",
"solution": """SELECT SUM(order_total) FROM orders;"""
},

{   # Problem 17 -- avg function
    #-> What is the average order amount?
"instruction": 
"""Another useful aggregate function is the average.

Task: Write a query that shows the average order cost.""",
"hint": """Select the average of the order_total from the table 'orders'.""",
"solution": """SELECT AVG(order_total) FROM orders;"""
},

{   # Problem 18 -- min function
    # - -> What is the smallest (dollar amount) order?
"instruction": 
"""Lastly, we have aggregate functions to select both the minimum or maximum values of a column.

Task: Write a query that shows the order total that was lowest in price.""",
"hint": """Select the minimum of the order_total from the table 'orders'. """,
"solution": """SELECT MIN(order_total) FROM orders;"""
},

{   # Problem 19 -- english query
"instruction": 
"""Now, for a change of pace, we're going to try to write queries that can show us information that spans multiple tables. Before we can do that though, a quick review.

Task: Write a query that fetches the id of the customer whose email is 'phyllis@demizz.edu'.
""",
"hint": """Select the id column from the 'customers' table where the email matches the string 'phyllis@demizz.edu'""",
"solution": """SELECT id FROM customers WHERE email = 'phyllis@demizz.edu';"""
},

{   # Problem 20 -- english query 2
"instruction": 
"""We've identified Phyllis in our previous exercise to be customer number 100.

Task: Write a query that shows the id, status and order_total for all orders made by customer 100.
""",
"hint": """Select the id, status, and order_total columns from the `orders` table where the customer id is 100.""",
"solution": """SELECT id, status, order_total FROM orders WHERE customer_id = 100;"""
},

{   # Problem 21 -- select-within-a-select
    #-> Get the orders for Phyliss by email address
"instruction": 
"""Our first technique for writing queries that cross tables is the subselect.
It lets us use the results of a query in the where clause of another query. In
this case, we can query the 'orders' table for orders matching the 'id' that
comes out of a different query. In this way, we can combine the previous two
queries into a single query.

Examples: http://sqlzoo.net/wiki/SELECT_within_SELECT_Tutorial -- 1

Task: Write a single query that shows the id, status, and order total for all
orders made by 'phyllis@demizz.edu'. Use a subselect to do this.
""",
"hint": """Select the id, status, and order_total columns from the 'orders'
table where the customer id matches the result from a subselect that queries
for the id column from the 'customers' table where the email matches the string
'phyllis@demizz.edu'.""",
"solution": """SELECT id, status, order_total FROM orders WHERE customer_id = (SELECT id FROM customers WHERE email = 'phyllis@demizz.edu');"""
},

{   # Problem 22 -- a simple join between two tables, using the 'as' clause.
    #-> Get all Orders with the customer name 
"instruction": 
"""Another way we can span tables is the 'join'. Joins can be complicated, but
one way to visualize them is as a venn diagram. Imagine you have a query that
selects all the customers in the customer table, and another query that selects
all the orders in the orders table. You can treat these two queries as the two
circles in a venn diagram. The intersection of these two sets, then, is all the
orders, attached to their respective customers.

Using a join, we can get the same results as the previous query by connecting
orders to the customers that made them, then filtering on the email of the
resulting join.

Examples: http://sqlzoo.net/wiki/The_JOIN_operation -- 1, 2, 3, 4

Task: Write a query that shows the id, status, and order total for all orders
made by 'phyllis@demizz.edu'. Use a join to do this.
""",
"hint": """Select the id, status, and order_total columns from the 'orders' table joined with the 'customers' table using the customer_id to line the two tables up. Use a where clause to limit the rows to only those that match 'phyliss@demizz.edu'.
""",
"solution": """SELECT orders.id, status, order_total FROM orders INNER JOIN customers ON (customer_id=customers.id) WHERE email = 'phyllis@demizz.edu';"""
},

{   # Problem 23 -- Prep for a join
    # -> What are all the items ordered for Order #2725?
"instruction":
"""We're going to practice more joins. The question we'll eventually answer is,
'can you show me all the details of the melons attached to a particular order?'
We will, but first, we need to understand how our data is organized. We have a
table called 'order_items'. This table includes information about all the items
in a given order. You can think of this table as representing a 'shopping cart'
of an order.

We'll start by querying for just half of the information we want: which melons
were present in a given order.

Task: Write a query that shows all columns
that were attached to order #2725.
""",
"hint": """Select all columns from the 'order_items' table where the order_id is equal to 2725.""",
"solution": """SELECT * FROM order_items WHERE order_id = 2725;"""
},

{   # Problem 24 -- Join with details
    # -> What are all the items ordered for Order #2725 with the melon details?
"instruction": 
"""Now, in addition to all the pricing information, we'll join the
'order_items' table to the 'melons' table to show all the information about the
melons in any given order.

Task: Write a query that shows the common_name, melon_type, quantity,
unit_price and total_price for all the melons in order #2725.
""",
"hint": """Select the common_name and melon_type from the 'melons' table, left
joined to the quantity, unit_price, and total_price from the 'order_items'
table, using the melon_id to line up the two tables. Limit the results to only
the items present in order #2725.""",
"solution": """SELECT M.common_name, M.melon_type, I.quantity, I.unit_price, I.total_price FROM order_items I JOIN melons M ON (I.melon_id = M.id) WHERE I.order_id = 2725;"""
},

{   # Problem 25 -- The null keyword
    # -> Get total amount of web orders (no sales person id) 
"instruction": 
"""In our system, an order can be attached to a salesperson in order to give
them commission. However, some orders come in from the web, which means some
orders have no salesperson. This is indicated in our table by having the
salesperson id be 'NULL', similar to python's 'None'.

Task: Write a query that shows the total amount of revenue that comes from
internet orders.""",
"hint": """Select the sum of the order_total column from the 'orders' table
where the salesperson_id is null.""",
"solution": """SELECT SUM(order_total) FROM orders WHERE salesperson_id IS NULL;"""
},

{   # Problem 26 -- A combination of pretty much everything, adding group_by
    # -> Get a list of all sales people and the total amount of orders they've sold.  Calculate a 15% commision.
"instruction": 
"""
Challenge: Produce a list of all salespeople and the total amount of orders
they've sold, while calculating a 15% commission on all of their orders.
Include their given name, surname, the total of all their sales, and their
commission. Only report one row per salesperson. Include salespeople who have
not made any sales.

You will need 'left join' (http://sqlzoo.net/wiki/LEFT_JOIN) and 'group by'
(http://sqlzoo.net/wiki/SELECT_.._GROUP_BY) clauses to finish this one.
""", 
"hint": """Select the givenname, surname, the sum of the order_total, and the
sum of the order_total multiplied by .15 from the table 'salespeople' joined on
the 'orders' table, matching the salesperson_id on the order to the id column
from the 'salespeople' table. Group the results by the id from the salespeople
table.""",
    "solution": """SELECT S.givenname, S.surname, SUM(order_total), SUM(order_total) * .15 AS commision FROM salespeople S LEFT JOIN orders O ON (O.salesperson_id = S.id) GROUP BY S.id;"""
}

]

def generate_solution_hash(problem, cursor):
    soln_query = problem['solution']
    return generate_result_hash(soln_query, cursor)

def serialize_problems(problems, cursor):
    for p in problems:
        hash_ = generate_solution_hash(p, cursor)
        p['soln_hash'] = hash_
        del p['solution']

    output_file = open("problem_set.pickle", "w")
    pickle.dump(problems, output_file)
    

def main():
    cursor = sql_problem.connect()
    output = serialize_problems(PROBLEMS, cursor)


if __name__ == "__main__":
    main()


