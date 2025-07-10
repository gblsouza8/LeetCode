/* 
Seleciona os nomes de todos os empregados como "e" e da um Join como "m" onde os managerID de "e" 
equivalem ao ID de "m" para separar ambos e compara o salário de e com m, 
retornando os Employees que ganham mais que os Managers
*/
SELECT e.Name AS Employee FROM Employee e
JOIN Employee m ON e.managerId = m.id WHERE e.Salary > m.Salary;