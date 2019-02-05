const proj = require('proj4');
const fs = require('fs');
const csv = require('csv-parser')
const bogenSrc = './wenkerdaten.csv';
const ch = 'PROJCS["CH1903 / LV03",GEOGCS["CH1903",DATUM["CH1903",SPHEROID["Bessel 1841",6377397.155,299.1528128,AUTHORITY["EPSG","7004"]],TOWGS84[674.4,15.1,405.3,0,0,0,0],AUTHORITY["EPSG","6149"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4149"]],PROJECTION["Hotine_Oblique_Mercator_Azimuth_Center"],PARAMETER["latitude_of_center",46.95240555555556],PARAMETER["longitude_of_center",7.439583333333333],PARAMETER["azimuth",90],PARAMETER["rectified_grid_angle",90],PARAMETER["scale_factor",1],PARAMETER["false_easting",600000],PARAMETER["false_northing",200000],UNIT["metre",1,AUTHORITY["EPSG","9001"]],AXIS["Y",EAST],AXIS["X",NORTH],AUTHORITY["EPSG","21781"]]';
const ll = proj.defs('EPSG:4326');

let results = [];

function chToLL(x, y) {
  lnglat = proj(ch, proj.defs('EPSG:4326'), [x, y])
  console.log(lnglat)
  return lnglat;
}

fs.createReadStream(bogenSrc)
  .pipe(csv())
  .on('data', (data) => {
    results.push(data)
  })
  .on('end', () => {
    results.forEach((result) => {
      if (result.X != '' && result.Y != '') {
        let conv = chToLL(parseFloat(result.X), parseFloat(result.Y));
      }
    });
  });




