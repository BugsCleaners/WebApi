namespace WebAPICore.Extension
{
    public class General
    {
        public static string GetAppSettings(string key)
        {

            string result = string.Empty;

            try
            {
                var AppSetting = new ConfigurationBuilder()
                     .SetBasePath(Directory.GetCurrentDirectory())
                     .AddJsonFile("appsettings.json")
                     .Build();

                result = AppSetting[key.ToString()].ToString();

            }
            catch (Exception ex)
            {
                string message = ex.Message;
                result = string.Empty;
            }
            return result;


        }

    }
}
