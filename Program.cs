using System;

class Program
{
    public static double Add(int num1, int num2)
    {
        double result = num1 + num2;
        return result;
    }
    public static double Sub(int num1, int num2)
    {
        double result = num1 - num2;
        return result;
    }
    public static double Multy(int num1, int num2)
    {
        double result = num1 * num2;
        return result;
    }
    public static double Div(int num1, int num2)
    {
        double result = num1 / num2;
        return result;
    }
    public static string Calculator()
    {
        char[] operators = { '+', '-', '*', '/' };
        int num1, num2;
        char choice; // the operator the user chooses

        Console.Write("Enter a number: ");
        num1 = int.Parse(Console.ReadLine());

        Console.Write("Enter an operator: ");
        choice = char.Parse(Console.ReadLine());

        Console.Write("Enter another number: ");
        num2 = int.Parse(Console.ReadLine());

        for (int i = 0; i < operators.Length; i++)
        {
            if (operators[i] == choice)
            {
                return $"{num1} {choice} {num2} = {Math(num1, num2, choice)}";
            }
        }

        return "The operator isn't available";
    }

    public static double Math(int num1, int num2, char oper)
    {
        switch (oper)
        {
            case '+':
                return Add(num1, num2);
            case '-':
                return Sub(num1, num2);
            case '*':
                return Multy(num1, num2);
            case '/':
                return Div(num1, num2);
            default:
                return 0.0;
        }
    }

    public static void Main()
    {
        Console.WriteLine(Calculator());
    }
}
