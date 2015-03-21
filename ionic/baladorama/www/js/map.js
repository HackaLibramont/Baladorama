angular
	.module('osmMap', [])
	.factory('$osm', function() {
		var osm = {
			map : L.map('map'),
			positionMarker: null,
			positionCircle: null,
			icons: {
				redMarker : L.AwesomeMarkers.icon({
					icon: 'coffee',
					markerColor: 'red'
				})
			},
			init : function() {
				this.map.setView([50.38, 40.40], 5);

				// add an OpenStreetMap tile layer
				L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
					attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
				}).addTo(this.map);
			},
			update: function(position, zoomOnPosition) {
				var coords = position.coords;
				this.positionMarker = L.marker([coords.latitude, coords.longitude]).bindPopup('Your are here');
				this.positionCircle = L.circle([coords.latitude, coords.longitude], coords.accuracy/2, {
					weight: 1,
					color: 'blue',
					fillColor: '#cacaca',
					fillOpacity: 0.2
				});
				if (zoomOnPosition) this.map.setView([coords.latitude, coords.longitude], 15);
				this.map.removeLayer(this.positionMarker);
				this.map.removeLayer(this.positionCircle);
				this.map.addLayer(this.positionMarker);
				this.map.addLayer(this.positionCircle);
			},
			addPois: function(pois) {
				pois.forEach(function(poi) {
					this.map.addLayer(L.marker([poi.fields.latitude, poi.fields.longitude], {icon: this.icons.redMarker}).bindPopup(poi.fields.name));
				}, this);
			}
		};
		// factory function body that constructs shinyNewServiceInstance
		return osm;
	});

