function getUserLocation(){
    if (!navigator.geolocation){
        alert("Your browser does not support Geolocation. Please update your browser.");
    }
    else{
        navigator.geolocation.getCurrentPosition(_showPosition)
    };
}

function _showPosition(position){
    var lat = position.coords.latitude
    var lng = position.coords.longitude
    var alt = position.coords.altitude

    console.log(position)

    // Redirect to another page with these parameters.
    generatedUrl = "secondpage/?latitude=" + String(lat) + "&longitude=" + String(lng) + "&altitude=" + String(alt)
    window.location = (generatedUrl)
}