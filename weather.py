from mcp.server.fastmcp import FastMCP

mcp= FastMCP("Weather")

@mcp.tool()
async def get_weather(city:str)->str:
    """
    Get the weather for a given city """
    return f"The weather in {city} is sunny"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
 #streamable-http is a transport that allows the server to be accessed via a streamable HTTP server.(more like a web server API)