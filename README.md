# CityMe

<a href="https://cityme.novaims.unl.pt">![Website](https://img.shields.io/website?label=CityMe&style=for-the-badge&up_message=live&url=https%3A%2F%2Fcityme.novaims.unl.pt%2F)</a>
![GitHub last commit](https://img.shields.io/github/last-commit/CityMe-project/cityme?style=for-the-badge)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/instagrapi?style=for-the-badge)
    
The **CityMe** project aims at creating a framework for mapping, exploring and analyzing official and non-official neighborhoods, regions of interest, districts and other areas that constitute people’s mental map of the city. By harvesting data from our **map-based application** and social media platforms, we can better understand how citizens spatially reason about administrative and non-administrative regions in the urban landscape, such as parishes, residential areas, informal neighborhoods, historical centers and commercial areas.

<p align="center">
<img align="left" alt="Product Page" src="https://cityme.novaims.unl.pt/static/media/svg-map.d62718760857113ad3fd07495df17757.svg" width="250">

<p>Through applying state-of-the-art spatial analysis, our framework can be applied to other cities in order to improve and enhance participatory urban planning, citizen-engagement in public policies and projects in smart cities.
    
**CityMe** is not only restricted to characterizing different types of regions in the city, but it is also committed to contributing to the efforts of making cities more human through citizen-centered, transparent and bottom-up approaches in various applications in the context of urban intelligence.</p>

</p>

\
&nbsp;
\
&nbsp;


## :mortar_board: Objectives

<ul>
    <li> Make available a web map survey and questionnaire interface
    <li> Perform spatial analysis to compare and characterize the regions from surveyed data and user-generated content from social media
    <li> Evaluate survey results based on sociodemographic attributes
    <li> Explore results based on administrative boundaries, official names, census blocks, urban morphology, landmarks and points of interest
</ul>

<!-- CONTENTS -->
<h2 id = "contents">Contents</h2>

<details open = "open">
  <summary>Contents</summary>
  <ol>
    <li><a href = "#data">Data Sources</a></li>
    <li><a href = "#pre">Prerequisites</a></li>
    <li><a href = "#db">Database</a></li>
    <li><a href = "#init">Installation</a></li>
    <li><a href = "#use">Usage</a></li>
    <li><a href = "#authors">Authors</a></li>
  </ol>
</details>

<h2 id = "data">Data Sources</h2>
Data platforms that support user-generated geo-tagged content were used for this project. The relevant sources are listed below

<ul>
  <li>Twitter</li>
  <li>Instagram</li>
  <li>Flickr</li>
  <li>Wikipedia</li>
  <li>Idealista</li>
</ul>

<h2 id = "pre">Prerequisites</h2>
<ul>
  <li>Postgres 14.1
  <li>Python 3.10
  <li>GDAL 3.4.1
</ul>

<h2 id = "db">Database Setup</h2>

Following parameters are required to be configured in each of the ingestion file
```
database = ""
user = "postgres"
password = "postgres"
host = "localhost"
port = 5432
table_name = ""
```

<h2 id = "init">Installation</h2>

Setup Python Environment
```
git clone https://github.com/CityMe-project/cityme.git
conda install -n py10 python=3.10
conda activate py10
pip3 install -r requirements.txt
```

<h2 id = "usage">Usage</h2>

All `.ipynb` files show an example of how to dump data into Postgres

<b>Twitter</b>

Fetching 10,000 tweets using bounding box. More filters for `query` can be referred from here [Twitter API](https://developer.twitter.com/apitools/api?endpoint=%2F2%2Ftweets%2Fsearch%2Fall&method=get)

The API requires configuration of API keys in `creds.yaml`. To modify filters of the command, [refer here](https://github.com/twitterdev/search-tweets-python/tree/v2)

```
python ingestion/twitter/search-tweets-python/scripts/search_tweets.py --credential-file creds.yaml --max-pages 1 --max-tweets 10000 --output-format a --results-per-call 100 --query "(bounding_box:[-9.237994149198911 38.68001599304764 -9.088636579438045 38.801883026428158] has:geo)" --start-time "2015-01-01T01:00" --end-time "2020-04-15T20:37" --tweet-fields author_id,created_at,geo,id,source,text --place-fields country,geo,name,country_code,full_name --expansions geo.place_id --filename-prefix twitter_data --no-print-stream --debug --results-per-file 5000
```

<hr />

<b>Instagram</b>

Instagram posts can be downloaded for specific `hashtags`. 
Possible post types are `top` and `recent`

Installation
```
pip install instagrapi
```

Basic Example
```
python .\hashtag_downloader.py --u username --p password --posts 1000 --keyword lisbon --type top

```

To continue scraping from a specific point, use the cursor stored in `insta_hash_cursor.txt`.
`insta_duplicate_map.txt` is used to keep a track of all the insta posts scrapped in order to avoid duplicates as it is not checked by the API even in the same session

```
python .\hashtag_downloader.py --u username --p password --posts 5000 --keyword lsibon --type recent --cursor d3a84e8b0618449a9e9c102c5cf70c01
```

[Thanks To instagrapi](https://github.com/adw0rd/instagrapi)

<hr />

<b>Flickr</b>

This official API enables downloading geo-tagged images. Please configure the keys in `flickr.ipynb`

<hr />

<b>Idealista</b>

The research-only API enables downloading geo-tagged real-estate listing. Please configure the keys in `idealista.ipynb`

<hr />

<b>Wikipedia</b>

```
pip install wikipedia
```

<h2 id = "authors"> :heart: Authors</h2>

<p>
  <b>Vicente De Azevedo Tang</b><br>
  <a href ="mailto:vtang@novaims.unl.pt">Contact</a> | <a href="https://github.com/vicetang" target="_blank">Github</a>
</p>

<p>
  <b>Jaskaran Singh Puri</b><br>
  <a href ="mailto:jpuri@novaims.unl.pt">Contact</a> | <a href="https://github.com/purijs" target="_blank">Github</a>
</p>
