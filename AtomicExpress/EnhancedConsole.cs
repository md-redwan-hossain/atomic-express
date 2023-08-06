namespace AtomicExpress;

public static class EnhancedConsole
{
    public static void WriteColoredLine(string value, ConsoleColor textColor,
        ConsoleColor? backgroundColor = null, bool newLine = true)
    {
        Console.ForegroundColor = textColor;

        if (backgroundColor != null)
            Console.BackgroundColor = (ConsoleColor)backgroundColor;

        if (newLine)
            Console.WriteLine(value);
        else
            Console.Write(value);

        Console.ResetColor();
    }
}