function getUserLocation(){
    if (navigator.geolocation){
        alert("Getting geolocation");
    }
    alert(navigator.geolocation.getCurrentPosition(_showPosition));
}

function _showPosition(position){
    var latlng =  [position.coords.latitude, position.coords.longitude];
    // Do something with latlng array :) 
    alert(latlng)
}