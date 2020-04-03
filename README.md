# About 

The idea is to develop an API for streaming elevation data at arbitrary
locations in Canada... and soon, THE WORLD!


Right now, it's a tool to crawl over a specified area and provide a scanline of
the elevation in that area for further munging.

Consumes elevation data in the form of GeoTIFF files (like those available from geogratis, e.g. CDEM).

# Resources

* Canadian Digital Elevation Model
  * [Documnetation (PDF)](http://ftp.geogratis.gc.ca/pub/nrcan_rncan/elevation/cdem_mnec/doc/CDEM_en.pdf)
  * [CDEM Product Specs](http://ftp.geogratis.gc.ca/pub/nrcan_rncan/elevation/cdem_mnec/doc/archive/CDEM_product_specs_1_0.pdf)
  * [GeoTIFF Dataset](http://ftp.geogratis.gc.ca/pub/nrcan_rncan/elevation/cdem_mnec/)
* [GDAL](https://gdal.org/gdal_tutorial.html), a Python library for GeoTIFF processing 
* [Geotrellis](https://geotrellis.readthedocs.io/en/latest/index.html), a Scala library for fast GeoTIFF processing
* [UTM CRS overview](https://www.maptools.com/tutorials/utm/quick_guide)
