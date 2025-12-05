##INNER JOIN 
##1 - List all orders with customer names and email.
select o.order_id, o.order_date , o.total_amount,
c.customer_name , c.email 
from orders o inner join customers c 
on o.customer_id = c.customer_id;

##2. Show product name, category, price for every ordered product.
select p.product_name , p.category , p.price 
from orders o inner join products p 
on o.product_id = p.product_id;

##3. List all orders with customer name and product name.
select o.order_id, o.order_date , c.customer_name , p.product_name
from orders o inner join customers c 
on o.customer_id = c.customer_id
inner join products p 
on o.product_id = p.product_id;

##4. Show customer name and total_amount for all valid customer orders.
select c.customer_name, o.total_amount 
from orders o inner join customers c
on o.customer_id = c.customer_id;

##5. List all Electronics products that have been ordered.
select p.product_name from orders o inner join products p 
where p.category = 'Electronics';





