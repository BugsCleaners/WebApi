using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace WebAPICore.Controllers
{
    [Route("api")]
    [ApiController]
    public class DefaultController : ControllerBase
    {

        [HttpGet]
        [Route("hello")]
        public IActionResult hello(string? name = "World")
        {
                return new OkObjectResult( String.Format("Hello {0}", name));
           
        }

    

    }
}
