# About 

The idea is to develop an API for streaming elevation data at arbitrary
locations in Canada... and soon, THE WORLD!


Right now, it's a tool to crawl over a specified area and provide a scanline of
the elevation in that area for further munging.

A separate API call is required for every single elevation point. This is very
slow, and the government webmaster probably doesn't appreciate me slamming his
endpoint without moderation.


# Resources

* Canadian Digital Elevation Model
  * [Documnetation (PDF)](http://ftp.geogratis.gc.ca/pub/nrcan_rncan/elevation/cdem_mnec/doc/CDEM_en.pdf)
  * [CDEM Product Specs](http://ftp.geogratis.gc.ca/pub/nrcan_rncan/elevation/cdem_mnec/doc/archive/CDEM_product_specs_1_0.pdf)
  * [GeoTIFF Dataset](http://ftp.geogratis.gc.ca/pub/nrcan_rncan/elevation/cdem_mnec/)
