using System.Text.RegularExpressions;

namespace AtomicExpress
{
    public class FileSystemUtils
    {
        private readonly string _baseDirectory;

        public FileSystemUtils() => _baseDirectory = Directory.GetCurrentDirectory();


        public bool CheckDirectoryAvailability(string dirName) =>
            !Directory.Exists(Path.Combine(_baseDirectory, dirName));

        public bool CheckValidDirectoryName(string dirName)
        {
            dirName = dirName.Trim();
            const string pattern = "^[a-zA-Z0-9-_]+$";
            return Regex.IsMatch(dirName, pattern);
        }


        public void CreateDirectory(string dirName)
        {
            try
            {
                Directory.CreateDirectory(Path.Combine(_baseDirectory, dirName));
            }
            catch (UnauthorizedAccessException)
            {
                EnhancedConsole.WriteColoredLine(text: $"{_baseDirectory} is not writeable",
                    textColor: ConsoleColor.Red);
            }
        }
    }
}