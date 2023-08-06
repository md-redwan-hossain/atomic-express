namespace AtomicExpress;


public class DownloadManager
{
    private readonly HttpClient _httpClient;


    public DownloadManager()
    {
        _httpClient = new HttpClient();

    }

    public async Task<bool> Download(string url, string path, string fileName)
    {
        EnhancedConsole.WriteColoredLine(text: $"Downloading {fileName}", textColor: ConsoleColor.Green);
        var stream = await _httpClient.GetStreamAsync(url);
        var fileStream = new FileStream(Path.Combine(path, fileName), FileMode.CreateNew);
        await stream.CopyToAsync(fileStream);
        return true;
    }
}