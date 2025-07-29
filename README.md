```markdown
# Aigeon AI Google Light Search

Aigeon AI Google Light Search is a Python-based server application designed to facilitate fast and efficient web search results using Google's Light Search API. This project leverages the capabilities of the SerpApi to provide users with a streamlined and customizable search experience.

## Features Overview

- **Customizable Search Queries**: Allows users to define detailed search queries with various parameters to tailor the search results to specific needs.
- **Location and Language Specific Searches**: Supports searches originating from specific locations and in specific languages.
- **Device-Specific Search Results**: Enables users to simulate searches from different devices such as desktop, tablet, or mobile.
- **Advanced Search Parameters**: Supports advanced search query parameters for more refined search results.
- **Cache Management**: Provides options to use cached results for faster response times or force fresh searches.
- **Asynchronous Search Capability**: Offers the ability to perform searches asynchronously, allowing retrieval of results at a later time.
- **Enterprise Features**: Includes options for enterprise users, such as ZeroTrace mode for enhanced privacy.

## Main Features and Functionality

The core functionality of the Aigeon AI Google Light Search is encapsulated in the `search_light` function, which interacts with the SerpApi to perform searches based on user-defined parameters. The application is built using the FastMCP framework for efficient server management and communication.

### Main Functions Description

#### `search_light`

This function is the primary interface for performing Google Light searches. It accepts a variety of parameters to customize the search experience:

- **q**: The query string for the search. Supports regular Google search syntax and advanced search parameters.
- **location**: Specifies the geographical location from which the search should originate.
- **uule**: Google encoded location for the search.
- **google_domain**: Defines the Google domain to use, defaulting to `google.com`.
- **gl**: Two-letter country code for the search.
- **hl**: Two-letter language code for the search.
- **lr**: Limits the search to specific languages using language codes.
- **safe**: Sets the level of filtering for adult content.
- **nfpr**: Excludes results from auto-corrected queries when set.
- **filter**: Toggles filters for 'Similar Results' and 'Omitted Results'.
- **start**: Result offset for pagination.
- **num**: Maximum number of results to return.
- **device**: Defines the device type for the search results.
- **no_cache**: Forces fresh search results, bypassing cached data.
- **aasync**: Enables asynchronous search submission.
- **zero_trace**: Enterprise-only feature to enable ZeroTrace mode for enhanced privacy.

The function constructs a payload with these parameters and sends a GET request to the SerpApi endpoint. It processes the response and returns the search results in JSON format.

---

This README provides an overview of the Aigeon AI Google Light Search project, highlighting its key features and functionality. For further details on usage and implementation, users should refer to the code and accompanying documentation.
```