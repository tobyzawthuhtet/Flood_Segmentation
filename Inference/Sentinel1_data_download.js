var aoi_1 = ee.FeatureCollection("projects/ee-tobyzawgis/assets/20210729_Detected_Flood_Water_in_Myanmar_roi_01"),
    aoi_2 = ee.FeatureCollection("projects/ee-tobyzawgis/assets/20210729_Detected_Flood_Water_in_Myanmar_roi_02"),
    geometry = 
    /* color: #d63000 */
    /* shown: false */
    /* displayProperties: [
      {
        "type": "rectangle"
      }
    ] */
    ee.Geometry.Polygon(
        [[[97.69489935204209, 17.066478675881253],
          [97.69489935204209, 16.428687757948822],
          [98.29365423485459, 16.428687757948822],
          [98.29365423485459, 17.066478675881253]]], null, false),
    geometry2 = 
    /* color: #98ff00 */
    /* shown: false */
    /* displayProperties: [
      {
        "type": "rectangle"
      }
    ] */
    ee.Geometry.Polygon(
        [[[96.60763532319704, 18.03176231890173],
          [96.60763532319704, 17.39599062324644],
          [96.97018415132204, 17.39599062324644],
          [96.97018415132204, 18.03176231890173]]], null, false),
    imageVisParam2 = {"opacity":1,"bands":["VV"],"min":-18.67121046292783,"max":-5.496740050317297,"gamma":1};


  
Map.setOptions('SATELLITE');
Map.centerObject(aoi_2,10);
Map.addLayer(aoi_1,{},"AOI1");
Map.addLayer(aoi_2,{},"AOI2");

var S1 = ee.ImageCollection("COPERNICUS/S1_GRD").filterDate('2021-07-20','2021-7-30');

var S1_a = S1.filterBounds(aoi_1).select('VV','VH').mean().clip(geometry);
var S1_b = S1.filterBounds(aoi_2).select('VV','VH').mean().clip(geometry2);
print(S1_a);

Map.addLayer(S1_a,imageVisParam2,"AOI1 Sentinel 1 Data");
Map.addLayer(S1_b,imageVisParam2,"AOI2 Sentinel 1 Data");

// Export the image, specifying the CRS, transform, and region.
Export.image.toDrive({
  image: S1_a,
  // image : S1_b
  description: 'Inference1_sentinel1_data',
  folder: 'test_data',
  crs : 'EPSG : 4326',
  scale: 10, 
  region: geometry
});
// Export the image, specifying the CRS, transform, and region.
Export.image.toDrive({
  image : S1_b,
  description: 'Inference2_sentinel1_data',
  folder: 'test_data',
  crs : 'EPSG : 4326',
  scale: 10, 
  region: geometry2
});
    
    