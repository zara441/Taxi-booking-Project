async function initMap(){
    const { Map } = await google.maps.importLibrary("maps");
    const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");
    const location =  {
        lat: 11.92886266574933,
        lng: 75.66023330751182,         
      };
    
    

    const map = new Map(document.getElementById("map"),{
        center:location,zoom:12,mapId:"5615fb9271a6f53d"
    });
    const marker = new AdvancedMarkerElement({map,position:location});
  }


function toggleHighlight(markerView, property) {
if (markerView.content.classList.contains("highlight")) {
    markerView.content.classList.remove("highlight");
    markerView.zIndex = null;
} else {
    markerView.content.classList.add("highlight");
    markerView.zIndex = 1;
}
}

function buildContent(property) {
const content = document.createElement("div");

content.classList.add("property");
content.innerHTML = `
    <div class="icon">
        <i aria-hidden="true" class="fa fa-${property.type}" title="${property.type}"></i>
        <span class="fa-sr-only">${property.type}</span>
    </div>
    <div class="details">
        <div class="price">${property.price}</div>
        <div class="address">${property.address}</div>
        <div class="features">
        <div>
            <i aria-hidden="true" class="fa fa-car fa-lg car" title="bedroom"></i>
            <span class="fa-sr-only">car</span>
            <span>${property.size}</span>
        </div>
        </div>
    </div>
    `;
return content;
}



const stands = 
initMap();