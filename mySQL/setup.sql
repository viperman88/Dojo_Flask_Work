SELECT * FROM clients;

SELECT clients.first_name,clients.last_name,billing.amount,billing.charged_datetime
FROM clients
JOIN billing ON clients.id = billing.clients_id;

SELECT sites.domain_name,leads.first_name,leads.last_name
FROM sites
JOIN leads ON sites.id = leads.sites_id;

SELECT clients.first_name,clients.last_name,sites.domain_name,leads.last_name AS lead_last
FROM clients
JOIN sites ON clients.id = sites.clients_id
JOIN leads ON sites.id = leads.sites_id;

SELECT clients.first_name,clients.last_name, sites.domain_name
FROM clients
LEFT JOIN sites ON clients.id = sites.clients_id;

SELECT clients.first_name,clients.last_name, MAX(billing.amount) AS max_billing
FROM clients
JOIN billing ON clients.id = billing.clients_id
GROUP BY clients.id;

SELECT clients.first_name,clients.last_name, GROUP_CONCAT(sites.domain_name)
FROM clients
JOIN sites ON clients.id = sites.clients_id
GROUP BY clients.id;

SELECT COUNT(leads.id), sites.domain_name
FROM sites
JOIN leads ON sites.id = leads.sites_id
GROUP BY sites.id;
