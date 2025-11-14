import os

class Calculator:
    
    @staticmethod
    def multiply(a: int, b: int) -> int:
        """
        Multiply two integers.

        Args:
            a (int): The first integer.
            b (int): The second integer.
    
        Returns:
            int: The product of two integers.
        """
        return a * b
    
    @staticmethod
    def calculate_total(*x: float) -> float:
        """
        Calculate sum of given list of numbers.

        Args:
            x(list): List of floating numbers.

        Returns:
            float: The sum of numbers in the list x
        """
        return sum(x)
    
    @staticmethod
    def calculate_daily_budget(total: float, days: int) -> float:
        """
        calculate the daily budget based on total expense and number of days.

        Args:
            total (float): Total Expense Cost
            days (int): Total numbers of days

        Returns:
            float: Expense for a single day
        """
        return total/days if days > 0 else 0
