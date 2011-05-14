$(document).ready(function() {
	$("#search-form button").live("click", function() {
		console.log("val", $("#search").val());
		showAddress($("#search").val());
	});
});
 
function showAddress(address) {
	var geocoder = new GClientGeocoder();
	if (geocoder) {
		geocoder.getLatLng(
			address,
			function(point) {
				if (!point) {
					alert("We're sorry but '" + address + "' cannot be found on Google Maps. Please try again.");
				} else {
			map.panTo(point); 
			}
		});
	}
}


    
    
    
    /*
    
    geoLocation();
    
    function geoLocation() {
	    // Try W3C Geolocation (Preferred)
		  if(navigator.geolocation) {
		    browserSupportFlag = true;
		    navigator.geolocation.getCurrentPosition(function(position) {
		      initialLocation = new google.maps.LatLng(position.coords.latitude,position.coords.longitude);
		      map.setCenter(initialLocation);
		    }, function() {
		      handleNoGeolocation(browserSupportFlag);
		    });
		  // Try Google Gears Geolocation
		  } else if (google.gears) {
		    browserSupportFlag = true;
		    var geo = google.gears.factory.create('beta.geolocation');
		    geo.getCurrentPosition(function(position) {
		      initialLocation = new google.maps.LatLng(position.latitude,position.longitude);
		      map.setCenter(initialLocation);
		    }, function() {
		      handleNoGeoLocation(browserSupportFlag);
		    });
		  // Browser doesn't support Geolocation
		  } else {
		    browserSupportFlag = false;
		    handleNoGeolocation(browserSupportFlag);
		  }
	  }
	  
	  function handleNoGeolocation(errorFlag) {
	    if (errorFlag == true) {
	      alert("Geolocation service failed.");
	      initialLocation = newyork;
	    } else {
	      alert("Your browser doesn't support geolocation. We've placed you in Siberia.");
	      initialLocation = siberia;
	    }
	    map.setCenter(initialLocation);
	  }
  	*/