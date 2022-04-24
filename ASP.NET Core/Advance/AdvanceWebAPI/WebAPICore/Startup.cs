using Microsoft.AspNetCore.Builder;
namespace WebAPICore
{
    public class Startup
    {

        public void ConfigureServices(IServiceCollection services)
        {
            var Configuration = new ConfigurationBuilder()
                 .SetBasePath(Directory.GetCurrentDirectory())
                 .AddJsonFile("appsettings.json")
                 .Build();
            services.AddSingleton(Configuration);

            //Microsoft.AspNetCore.Mvc.Formatters.MediaTypeCollection myContentTypes = new Microsoft.AspNetCore.Mvc.Formatters.MediaTypeCollection { System.Net.Mime.MediaTypeNames.Application.Json };

        }
    }
}
