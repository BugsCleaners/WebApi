using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using WebAPICore.Models;

namespace WebAPICore.Controllers
{
    [Route("api")]
    [ApiController]
    public class DefaultController : ControllerBase
    {
        readonly IConfiguration _configuration;
        public DefaultController(IConfiguration configuration)
        {
            _configuration = configuration;

        }

        [HttpGet]
        [Route("hello")]
        public IActionResult hello()
        {
            return new OkObjectResult(new DataItem { name="test" });

        }




    }
}
