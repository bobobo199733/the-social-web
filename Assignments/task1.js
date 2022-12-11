function initMap() {
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 12,
    center: { lat: 52.33, lng: 4.86 },
  });
  const kmlLayer = new google.maps.KmlLayer({
    url: "https://raw.githubusercontent.com/bobobo199733/the-social-web/main/vrije_location.kml",
    suppressInfoWindows: true,
    map: map,
  });

  kmlLayer.addListener("click", (kmlEvent) => {
    const text = kmlEvent.featureData.description;

    showInContentWindow(text);
  });

  function showInContentWindow(text) {
    const sidebar = document.getElementById("sidebar");

    sidebar.innerHTML = text;
  }
}
window.initMap = initMap;
