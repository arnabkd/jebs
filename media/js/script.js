$(document).ready(function() {
	$("#search-form button").click(function() {
		showAddress($("#search").val());		
	});
});




    

/*

geoLocation();

function geoLocation() {
 
function showAddress(address) {
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