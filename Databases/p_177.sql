/* Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null. */
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE offset_val INT;
  SET offset_val = N - 1;

  RETURN (
      SELECT DISTINCT salary
      FROM Employee
      ORDER BY salary DESC
      LIMIT offset_val, 1
  );
END