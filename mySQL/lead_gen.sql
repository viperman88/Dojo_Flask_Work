
--1. What query would you run to get the total revenue for March of 2012?
SELECT SUM(billing.amount) AS total_amount, DATE_FORMAT(billing.charged_datetime," %M ") AS billing_date
FROM billing
WHERE  billing.charged_datetime LIKE "%2012-03%"
GROUP BY MONTH(billing.billing_id);

--2. What query would you run to get total revenue collected from the client with an id of 2?
SELECT CONCAT(clients.last_name, ", ", clients.first_name) AS client_name, SUM(billing.amount) AS total_amount
FROM clients
JOIN billing ON clients.client_id = billing.client_id
WHERE clients.client_id = 2;

--3. What query would you run to get all the sites that client=10 owns?
SELECT CONCAT(clients.last_name, ", ", clients.first_name) AS client_name, GROUP_CONCAT(" ", sites.domain_name) AS domains
FROM clients
JOIN sites ON clients.client_id = sites.client_id
WHERE clients.client_id = 10;

--4. What query would you run to get total # of sites created per month per year
--for the client with an id of 1? What about for client=20?
SELECT CONCAT(clients.last_name, ", ", clients.first_name) AS client_name, clients.client_id, COUNT(sites.domain_name) AS sites_created, DATE_FORMAT(sites.created_datetime, "%M %Y") AS created
FROM clients
JOIN sites ON clients.client_id = sites.client_id
WHERE clients.client_id = 1
GROUP BY sites.created_datetime;

--5. What query would you run to get the total # of leads generated for each of
--the sites between January 1, 2011 to February 15, 2011?
SELECT sites.domain_name, COUNT(leads.leads_id) AS leads, DATE_FORMAT(leads.registered_datetime , " %M %d, %Y ") AS lead_date
FROM sites
JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN "2011-01-01" AND "2011-02-15"
GROUP BY sites.site_id;

--6. What query would you run to get a list of client names and the total # of
--leads we've generated for each of our clients between January 1, 2011 to December 31, 2011?
SELECT CONCAT(clients.last_name, ",", clients.first_name) AS  client_name, COUNT(leads.leads_id) AS total_leads, DATE_FORMAT(leads.registered_datetime , " %M %d, %Y ") AS lead_date
FROM clients
JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN "2011-01-01" AND "2011-12-31"
GROUP BY clients.client_id;

--7. What query would you run to get a list of client names and the total # of
--leads we've generated for each client each month between months 1 - 6 of Year 2011?
SELECT CONCAT(clients.last_name, ",", clients.first_name) AS client_name, COUNT(leads.leads_id) AS total_leads, DATE_FORMAT(leads.registered_datetime , " %M, %Y ") AS lead_date
FROM clients
JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN "2011-01-01" AND "2011-06-30"
GROUP BY clients.client_id;

--8. What query would you run to get a list of client names and the total # of
--leads we've generated for each of our clients' sites between January 1, 2011 to
--December 31, 2011? Order this query by client id.
SELECT CONCAT(clients.last_name, ", ", clients.first_name) AS client_names, COUNT(leads.leads_id) AS total_leads
FROM clients
JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN "2011-01-01" AND "2011-12-31"
GROUP BY clients.client_id;

--8.2 Come up with a second query that shows all the clients, the site name(s),
--and the total number of leads generated from each site for all time.
SELECT CONCAT(clients.last_name, ", ", clients.first_name) AS client_names, COUNT(leads.leads_id) AS total_leads, sites.domain_name
FROM clients
JOIN sites ON clients.client_id = sites.client_id
JOIN leads ON sites.site_id = leads.site_id
GROUP BY clients.client_id, sites.domain_name;

--9. Write a single query that retrieves total revenue collected from each client
--for each month of the year. Order it by client id.
SELECT CONCAT(clients.last_name, ", ", clients.first_name) AS client_name, SUM(billing.amount) AS total_billing,DATE_FORMAT(billing.charged_datetime, "%M, %Y") AS created
FROM clients
JOIN billing ON clients.client_id = billing.client_id
GROUP BY clients.client_id, billing.charged_datetime;

--10. Write a single query that retrieves all the sites that each client owns. Group
--the results so that each row shows a new client. It will become clearer when you
--add a new field called 'sites' that has all the sites that the client owns.
SELECT CONCAT(clients.last_name, ", ", clients.first_name) AS client_name, GROUP_CONCAT(sites.domain_name) AS sites
FROM clients
JOIN sites ON clients.client_id = sites.client_id
GROUP BY clients.client_id;
