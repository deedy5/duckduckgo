![Python >= 3.8](https://img.shields.io/badge/python->=3.8-red.svg) [![](https://badgen.net/github/release/deedy5/duckduckgo_search)](https://github.com/deedy5/duckduckgo_search/releases) [![](https://badge.fury.io/py/duckduckgo-search.svg)](https://pypi.org/project/duckduckgo-search) [![Downloads](https://static.pepy.tech/badge/duckduckgo-search)](https://pepy.tech/project/duckduckgo-search) [![Downloads](https://static.pepy.tech/badge/duckduckgo-search/week)](https://pepy.tech/project/duckduckgo-search)
# Duckduckgo_search<a name="TOP"></a>

Search for words, documents, images, videos, news, maps and text translation using the DuckDuckGo.com search engine. Downloading files and images to a local hard drive.

## Table of Contents
* [Install](#install)
* [CLI version](#cli-version)
* [Duckduckgo search operators](#duckduckgo-search-operators)
* [Regions](#regions)
* [DDGS and AsyncDDGS classes](#ddgs-and-asyncddgs-classes)
* [Proxy](#proxy)
* [Exceptions](#exceptions)
* [1. text() - text search](#1-text---text-search-by-duckduckgocom)
* [2. answers() - instant answers](#2-answers---instant-answers-by-duckduckgocom)
* [3. images() - image search](#3-images---image-search-by-duckduckgocom)
* [4. videos() - video search](#4-videos---video-search-by-duckduckgocom)
* [5. news() - news search](#5-news---news-search-by-duckduckgocom)
* [6. maps() - map search](#6-maps---map-search-by-duckduckgocom)
* [7. translate() - translation](#7-translate---translation-by-duckduckgocom)
* [8. suggestions() - suggestions](#8-suggestions---suggestions-by-duckduckgocom)

## Install
```python
pip install -U duckduckgo_search
```
There is also a beta release that uses the `httpx` library:
```python
pip install -U duckduckgo_search==5.3.1b1
```
> [!NOTE]
> you can install lxml to use the `text` function with `backend='html'` or `backend='lite'` (size ≈ 12Mb)</br>
> `pip install -U duckduckgo_search[lxml]`

## CLI version

```python3
ddgs --help
```
or
```python3
python -m duckduckgo_search --help
```

CLI examples:
```python3
# text search
ddgs text -k "axon regeneration"
# find and download pdf files via proxy (example: Tor browser)
ddgs text -k "neuroscience filetype:pdf" -r wt-wt -m 50 -d -p socks5://localhost:9150
# find and download images
ddgs images -k "gaz 14 chaika" -r ru-ru -type photo -m 500 -d
# get latest news and save to csv
ddgs news -k "hubble telescope" -m 50 -o csv
```
[Go To TOP](#TOP)

## Duckduckgo search operators

| Keywords example |	Result|
| ---     | ---   |
| cats dogs |	Results about cats or dogs |
| "cats and dogs" |	Results for exact term "cats and dogs". If no results are found, related results are shown. |
| cats -dogs |	Fewer dogs in results |
| cats +dogs |	More dogs in results |
| cats filetype:pdf |	PDFs about cats. Supported file types: pdf, doc(x), xls(x), ppt(x), html |
| dogs site:example.com  |	Pages about dogs from example.com |
| cats -site:example.com |	Pages about cats, excluding example.com |
| intitle:dogs |	Page title includes the word "dogs" |
| inurl:cats  |	Page url includes the word "cats" |

[Go To TOP](#TOP)

## Regions
<details>
  <summary>expand</summary>

    xa-ar for Arabia
    xa-en for Arabia (en)
    ar-es for Argentina
    au-en for Australia
    at-de for Austria
    be-fr for Belgium (fr)
    be-nl for Belgium (nl)
    br-pt for Brazil
    bg-bg for Bulgaria
    ca-en for Canada
    ca-fr for Canada (fr)
    ct-ca for Catalan
    cl-es for Chile
    cn-zh for China
    co-es for Colombia
    hr-hr for Croatia
    cz-cs for Czech Republic
    dk-da for Denmark
    ee-et for Estonia
    fi-fi for Finland
    fr-fr for France
    de-de for Germany
    gr-el for Greece
    hk-tzh for Hong Kong
    hu-hu for Hungary
    in-en for India
    id-id for Indonesia
    id-en for Indonesia (en)
    ie-en for Ireland
    il-he for Israel
    it-it for Italy
    jp-jp for Japan
    kr-kr for Korea
    lv-lv for Latvia
    lt-lt for Lithuania
    xl-es for Latin America
    my-ms for Malaysia
    my-en for Malaysia (en)
    mx-es for Mexico
    nl-nl for Netherlands
    nz-en for New Zealand
    no-no for Norway
    pe-es for Peru
    ph-en for Philippines
    ph-tl for Philippines (tl)
    pl-pl for Poland
    pt-pt for Portugal
    ro-ro for Romania
    ru-ru for Russia
    sg-en for Singapore
    sk-sk for Slovak Republic
    sl-sl for Slovenia
    za-en for South Africa
    es-es for Spain
    se-sv for Sweden
    ch-de for Switzerland (de)
    ch-fr for Switzerland (fr)
    ch-it for Switzerland (it)
    tw-tzh for Taiwan
    th-th for Thailand
    tr-tr for Turkey
    ua-uk for Ukraine
    uk-en for United Kingdom
    us-en for United States
    ue-es for United States (es)
    ve-es for Venezuela
    vn-vi for Vietnam
    wt-wt for No region
___
</details>

[Go To TOP](#TOP)


## DDGS and AsyncDDGS classes

The DDGS and AsyncDDGS classes are used to retrieve search results from DuckDuckGo.com.
To use the AsyncDDGS class, you can perform asynchronous operations using Python's asyncio library.
To initialize an instance of the DDGS or AsyncDDGS classes, you can provide the following optional arguments:
```python3
class DDGS:
    """DuckDuckgo_search class to get search results from duckduckgo.com

    Args:
        headers (dict, optional): Dictionary of headers for the HTTP client. Defaults to None.
        proxy (str, optional): proxy for the HTTP client, supports http/https/socks5 protocols.
            example: "http://user:pass@example.com:3128". Defaults to None.
        timeout (int, optional): Timeout value for the HTTP client. Defaults to 10.
    """
```

Here is an example of initializing the DDGS class. 
```python3
from duckduckgo_search import DDGS

results = DDGS().text("python programming", max_results=5)
print(results)
```
Here is an example of initializing the AsyncDDGS class:
```python3
import asyncio

from duckduckgo_search import AsyncDDGS

async def aget_results(word):
    results = await AsyncDDGS(proxy=None).atext(word, max_results=100)
    return results

async def main():
    words = ["sun", "earth", "moon"]
    tasks = [aget_results(w) for w in words]
    results = await asyncio.gather(*tasks)
    print(results)

if __name__ == "__main__":
    asyncio.run(main())
```

[Go To TOP](#TOP)

## Proxy

Package supports http/https/socks proxies. Example: `http://user:pass@example.com:3128`.
Use a rotating proxy. Otherwise, use a new proxy with each DDGS or AsyncDDGS initialization.

*1. The easiest way. Launch the Tor Browser*
```python3
ddgs = DDGS(proxy="socks5://localhost:9150", timeout=20)
results = ddgs.text("something you need", max_results=50)
```
*2. Use any proxy server* (*example with [iproyal rotating residential proxies](https://iproyal.com?r=residential_proxies)*)
```python3
ddgs = DDGS(proxy="socks5://user:password@geo.iproyal.com:32325", timeout=20)
results = ddgs.text("something you need", max_results=50)
```

[Go To TOP](#TOP)

## Exceptions

Exceptions:
- `DuckDuckGoSearchException`: Base exception for duckduckgo_search errors.
- `RatelimitException`: Inherits from DuckDuckGoSearchException, raised for exceeding API request rate limits.
- `TimeoutException`: Inherits from DuckDuckGoSearchException, raised for API request timeouts.

  
[Go To TOP](#TOP)

## 1. text() - text search by duckduckgo.com

```python
def text(
    keywords: str,
    region: str = "wt-wt",
    safesearch: str = "moderate",
    timelimit: Optional[str] = None,
    backend: str = "api",
    max_results: Optional[int] = None,
) -> List[Dict[str, str]]:
    """DuckDuckGo text search generator. Query params: https://duckduckgo.com/params.

    Args:
        keywords: keywords for query.
        region: wt-wt, us-en, uk-en, ru-ru, etc. Defaults to "wt-wt".
        safesearch: on, moderate, off. Defaults to "moderate".
        timelimit: d, w, m, y. Defaults to None.
        backend: api, html, lite. Defaults to api.
            api - collect data from https://duckduckgo.com,
            html - collect data from https://html.duckduckgo.com,
            lite - collect data from https://lite.duckduckgo.com.
        max_results: max number of results. If None, returns results only from the first response. Defaults to None.

    Returns:
        List of dictionaries with search results.
    """
```
***Example***
```python
results = DDGS().text('live free or die', region='wt-wt', safesearch='off', timelimit='y', max_results=10)
# Searching for pdf files
results = DDGS().text('russia filetype:pdf', region='wt-wt', safesearch='off', timelimit='y', max_results=10)

# async
results = await AsyncDDGS().atext('sun', region='wt-wt', safesearch='off', timelimit='y', max_results=10)
```

[Go To TOP](#TOP)

## 2. answers() - instant answers by duckduckgo.com

```python
def answers(keywords: str) -> List[Dict[str, str]]:
    """DuckDuckGo instant answers. Query params: https://duckduckgo.com/params.
    
    Args:
        keywords: keywords for query,
    
    Returns:
        List of dictionaries with instant answers results.
    """
```
***Example***
```python
results = DDGS().answers("sun")

# async
results = await AsyncDDGS().aanswers("sun")
```

[Go To TOP](#TOP)

## 3. images() - image search by duckduckgo.com

```python
def images(
    keywords: str,
    region: str = "wt-wt",
    safesearch: str = "moderate",
    timelimit: Optional[str] = None,
    size: Optional[str] = None,
    color: Optional[str] = None,
    type_image: Optional[str] = None,
    layout: Optional[str] = None,
    license_image: Optional[str] = None,
    max_results: Optional[int] = None,
) -> List[Dict[str, str]]:
    """DuckDuckGo images search. Query params: https://duckduckgo.com/params.
    
    Args:
        keywords: keywords for query.
        region: wt-wt, us-en, uk-en, ru-ru, etc. Defaults to "wt-wt".
        safesearch: on, moderate, off. Defaults to "moderate".
        timelimit: Day, Week, Month, Year. Defaults to None.
        size: Small, Medium, Large, Wallpaper. Defaults to None.
        color: color, Monochrome, Red, Orange, Yellow, Green, Blue,
            Purple, Pink, Brown, Black, Gray, Teal, White. Defaults to None.
        type_image: photo, clipart, gif, transparent, line.
            Defaults to None.
        layout: Square, Tall, Wide. Defaults to None.
        license_image: any (All Creative Commons), Public (PublicDomain),
            Share (Free to Share and Use), ShareCommercially (Free to Share and Use Commercially),
            Modify (Free to Modify, Share, and Use), ModifyCommercially (Free to Modify, Share, and
            Use Commercially). Defaults to None.
        max_results: max number of results. If None, returns results only from the first response. Defaults to None.
    
    Returns:
        List of dictionaries with images search results.
    """
```
***Example***
```python
results = DDGS().images(
    keywords="butterfly",
    region="wt-wt",
    safesearch="off",
    size=None,
    color="Monochrome",
    type_image=None,
    layout=None,
    license_image=None,
    max_results=100,
)

# async
results = await AsyncDDGS().aimages('sun', region='wt-wt', safesearch='off', max_results=20)
```

[Go To TOP](#TOP)

## 4. videos() - video search by duckduckgo.com

```python
def videos(
    keywords: str,
    region: str = "wt-wt",
    safesearch: str = "moderate",
    timelimit: Optional[str] = None,
    resolution: Optional[str] = None,
    duration: Optional[str] = None,
    license_videos: Optional[str] = None,
    max_results: Optional[int] = None,
) -> List[Dict[str, str]]:
    """DuckDuckGo videos search. Query params: https://duckduckgo.com/params.
    
    Args:
        keywords: keywords for query.
        region: wt-wt, us-en, uk-en, ru-ru, etc. Defaults to "wt-wt".
        safesearch: on, moderate, off. Defaults to "moderate".
        timelimit: d, w, m. Defaults to None.
        resolution: high, standart. Defaults to None.
        duration: short, medium, long. Defaults to None.
        license_videos: creativeCommon, youtube. Defaults to None.
        max_results: max number of results. If None, returns results only from the first response. Defaults to None.
    
    Returns:
        List of dictionaries with videos search results.
    """
```
***Example***
```python
results = DDGS().videos(
    keywords="cars",
    region="wt-wt",
    safesearch="off",
    timelimit="w",
    resolution="high",
    duration="medium",
    max_results=100,
)

# async
results = await AsyncDDGS().avideos('sun', region='wt-wt', safesearch='off', timelimit='y', max_results=10)
```

[Go To TOP](#TOP)

## 5. news() - news search by duckduckgo.com

```python
def news(
    keywords: str,
    region: str = "wt-wt",
    safesearch: str = "moderate",
    timelimit: Optional[str] = None,
    max_results: Optional[int] = None,
) -> List[Dict[str, str]]:
    """DuckDuckGo news search. Query params: https://duckduckgo.com/params.
    
    Args:
        keywords: keywords for query.
        region: wt-wt, us-en, uk-en, ru-ru, etc. Defaults to "wt-wt".
        safesearch: on, moderate, off. Defaults to "moderate".
        timelimit: d, w, m. Defaults to None.
        max_results: max number of results. If None, returns results only from the first response. Defaults to None.
    
    Returns:
        List of dictionaries with news search results.
    """
```
***Example***
```python
results = DDGS().news(keywords="sun", region="wt-wt", safesearch="off", timelimit="m", max_results=20)

# async
results = await AsyncDDGS().anews('sun', region='wt-wt', safesearch='off', timelimit='d', max_results=10)
```

[Go To TOP](#TOP)

## 6. maps() - map search by duckduckgo.com

```python
def maps(
    keywords,
    place: Optional[str] = None,
    street: Optional[str] = None,
    city: Optional[str] = None,
    county: Optional[str] = None,
    state: Optional[str] = None,
    country: Optional[str] = None,
    postalcode: Optional[str] = None,
    latitude: Optional[str] = None,
    longitude: Optional[str] = None,
    radius: int = 0,
    max_results: Optional[int] = None,
) -> List[Dict[str, str]]:
    """DuckDuckGo maps search. Query params: https://duckduckgo.com/params.
    
    Args:
        keywords: keywords for query
        place: if set, the other parameters are not used. Defaults to None.
        street: house number/street. Defaults to None.
        city: city of search. Defaults to None.
        county: county of search. Defaults to None.
        state: state of search. Defaults to None.
        country: country of search. Defaults to None.
        postalcode: postalcode of search. Defaults to None.
        latitude: geographic coordinate (north-south position). Defaults to None.
        longitude: geographic coordinate (east-west position); if latitude and
            longitude are set, the other parameters are not used. Defaults to None.
        radius: expand the search square by the distance in kilometers. Defaults to 0.
        max_results: max number of results. If None, returns results only from the first response. Defaults to None.
    
    Returns:
        List of dictionaries with maps search results.
    """
```
***Example***
```python
results = DDGS().maps("school", place="Uganda", max_results=50)

# async
results = await AsyncDDGS().amaps('shop', place="Baltimor", max_results=10)
```

[Go To TOP](#TOP)

## 7. translate() - translation by duckduckgo.com

```python
def translate(
    self,
    keywords: str,
    from_: Optional[str] = None,
    to: str = "en",
) -> List[Dict[str, str]]:
    """DuckDuckGo translate.
    
    Args:
        keywords: string or list of strings to translate.
        from_: translate from (defaults automatically). Defaults to None.
        to: what language to translate. Defaults to "en".
    
    Returns:
        List od dictionaries with translated keywords.
    """
```
***Example***
```python
keywords = 'school'
# also valid
keywords = ['school', 'cat']
results = DDGS().translate(keywords, to="de")

# async
results = await AsyncDDGS().atranslate('sun', to="de")
```

[Go To TOP](#TOP)

## 8. suggestions() - suggestions by duckduckgo.com

```python
def suggestions(
    keywords,
    region: str = "wt-wt",
) -> List[Dict[str, str]]:
    """DuckDuckGo suggestions. Query params: https://duckduckgo.com/params.
    
    Args:
        keywords: keywords for query.
        region: wt-wt, us-en, uk-en, ru-ru, etc. Defaults to "wt-wt".
    
    Returns:
        List of dictionaries with suggestions results.
    """
```
***Example***
```python3
results = DDGS().suggestions("fly")

# async
results = await AsyncDDGS().asuggestions('sun')
```

[Go To TOP](#TOP)
