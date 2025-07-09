

# Seleciona o firstName e o lastName da tabela Person (p) e da um LEFT JOIN em Address (a) onde os personId são equivalentes em ambas as tabelas
SELECT p.firstName, p.lastName, a.city, a.state FROM Person p LEFT JOIN Address a ON p.personId = a.personId;