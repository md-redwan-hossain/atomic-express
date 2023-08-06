namespace AtomicExpress;

public static class EnhancedConsole
{
    private static void WriteInConsole(string text, ConsoleColor textColor,
        ConsoleColor? backgroundColor = null, bool newLine = true)
    {
        Console.ForegroundColor = textColor;

        if (backgroundColor != null)
            Console.BackgroundColor = (ConsoleColor)backgroundColor;

        if (newLine)
            Console.WriteLine(text);
        else
            Console.Write(text);

        Console.ResetColor();
    }


    public static void WriteColoredLine(string text, ConsoleColor textColor) =>
        WriteInConsole(text, textColor);


    public static void WriteColoredLine(string text, ConsoleColor textColor,
        ConsoleColor textBackgroundColor) =>
        WriteInConsole(text, textColor, textBackgroundColor);

    public static void WriteColoredLine(string text, ConsoleColor textColor,
        ConsoleColor textBackgroundColor, bool newLine) =>
        WriteInConsole(text, textColor, textBackgroundColor, newLine);
}