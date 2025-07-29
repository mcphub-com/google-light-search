import os
import requests
from typing import Union, Annotated, Literal
from pydantic import Field
from mcp.server import FastMCP
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP('serp-light-search')

serp_url = "https://serpapi.com/search"
serp_api_key = os.getenv("SERP_API_KEY")


@mcp.tool()
def search_light(
    q: Annotated[str, Field(
        description="Parameter defines the query you want to search. You can use anything that you would use in a regular Google search. e.g. inurl:, site:, intitle:. We also support advanced search query parameters such as as_dt and as_eq. See the full list of supported advanced search query parameters.")],
    location: Annotated[Union[str, None], Field(description="Parameter defines from where you want the search to originate. If several locations match the location requested, we'll pick the most popular one. Head to the /locations.json API if you need more precise control. The location and uule parameters can't be used together. It is recommended to specify location at the city level in order to simulate a real user’s search. If location is omitted, the search may take on the location of the proxy.")] = None,
    safe: Annotated[Union[Literal["active", "off"], None], Field(
        description="Parameter defines the level of filtering for adult content. It can be set to active or off, by default Google will blur explicit content.")] = None,
    nfpr: Annotated[Union[Literal[0, 1], None], Field(
        description="Parameter defines the exclusion of results from an auto-corrected query when the original query is spelled wrong. It can be set to 1 to exclude these results, or 0 to include them (default). Note that this parameter may not prevent Google from returning results for an auto-corrected query if no other results are available.")] = None,
    filter: Annotated[Union[Literal[0, 1], None], Field(
        description="Parameter defines if the filters for 'Similar Results' and 'Omitted Results' are on or off. It can be set to 1 (default) to enable these filters, or 0 to disable these filters.")] = None,
    start: Annotated[Union[int, None], Field(
        description="Parameter defines the result offset. It skips the given number of results. It's used for pagination. (e.g., 0 (default) is the first page of results, 10 is the 2nd page of results, 20 is the 3rd page of results, etc.).")] = None,
    num: Annotated[Union[int, None], Field(
        description="Parameter defines the maximum number of results to return. (e.g., 10 (default) returns 10 results, 40 returns 40 results, and 100 returns 100 results). The use of num may introduce latency, and/or prevent the inclusion of specialized result types. It is better to omit this parameter unless it is strictly necessary to increase the number of results per page.")] = None,
    device: Annotated[Union[Literal["desktop", "tablet", "mobile"], None], Field(
        description="Parameter defines the device to use to get the results. It can be set to desktop (default) to use a regular browser, tablet to use a tablet browser (currently using iPads), or mobile to use a mobile browser (currently using iPhones).")] = None,
    no_cache: Annotated[Union[bool, None], Field(
        description="Parameter will force SerpApi to fetch the Google Light results even if a cached version is already present. A cache is served only if the query and all parameters are exactly the same. Cache expires after 1h. Cached searches are free, and are not counted towards your searches per month. It can be set to false (default) to allow results from the cache, or true to disallow results from the cache. no_cache and async parameters should not be used together.")] = None,
    aasync: Annotated[Union[bool, None], Field(
        description="Parameter defines the way you want to submit your search to SerpApi. It can be set to false (default) to open an HTTP connection and keep it open until you got your search results, or true to just submit your search to SerpApi and retrieve them later. In this case, you'll need to use our Searches Archive API to retrieve your results. async and no_cache parameters should not be used together. async should not be used on accounts with Ludicrous Speed enabled.")] = None,
    zero_trace: Annotated[Union[bool, None], Field(
        description="Enterprise only. Parameter enables ZeroTrace mode. It can be set to false (default) or true. Enable this mode to skip storing search parameters, search files, and search metadata on our servers. This may make debugging more difficult.")] = None
):
    """Search Google Light for fast, web search results"""

    if location:
        q = q + ", location: %s"%location

    payload = {
        'engine': "google_light",
        'q': q,
        'api_key': serp_api_key,
        'safe': safe,
        'nfpr': nfpr,
        'filter': filter,
        'start': start,
        'num': num,
        'device': device,
        'no_cache': no_cache,
        'async': aasync,
        'zero_trace': zero_trace
    }
    # Remove None values
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(serp_url, params=payload)
    response.raise_for_status()
    return response.json()


if __name__ == '__main__':
    mcp.run(transport="stdio")