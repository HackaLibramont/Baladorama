angular
	.module('osmMap', [])
	.factory('$osm', function($compile) {
		var osm = {
			map : L.map('map'),
			positionMarker: null,
			positionCircle: null,
			icons: {
				redMarker : L.AwesomeMarkers.icon({
					icon: 'pinpoint',
					markerColor: 'red'
				}),
				routeMarker: L.AwesomeMarkers.icon({
					icon:'arrow-shrink',
					markerColor:'green'
				})
			},
			options: {
				positionZoom: 14
			},
			init : function() {
				this.map.setView([40.40, 50.38], 5);

				// add an OpenStreetMap tile layer
				L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
					attribution: 'Baladorama'
				}).addTo(this.map);
			},
			zoomOnCurrentPosition: function(position) {
				this.map.setView([position.latitude, position.coords.longitude], this.options.positionZoom);
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
				if (zoomOnPosition) this.map.setView([coords.latitude, coords.longitude], this.options.positionZoom);
				this.map.removeLayer(this.positionMarker);
				this.map.removeLayer(this.positionCircle);
				this.map.addLayer(this.positionMarker);
				this.map.addLayer(this.positionCircle);
			},
			addPois: function(pois, scope) {
				pois.forEach(function(poi) {
					var popup = angular.element(document.createElement('popup'));
					var popupScope = scope.$new(true);
					popupScope.poi = poi;
					popupScope.test = 'hello';
					var el = $compile( popup )( popupScope );
					console.log(el);
					this.map.addLayer(L.marker([poi.fields.latitude, poi.fields.longitude], {
						icon: this.icons[poi.icon ? poi.icon: 'redMarker']
					})
						.bindPopup(el[0]));
				}, this);
			},
			addRoute: function(waypoints) {
				var points = [];

				for(var i = waypoints.length - 1; i >= 0; i--) {
					points[i] = L.latLng(waypoints[i].latitude, waypoints[i].longitude);
				}

				var route = L.Routing.control({
					waypoints: points,
					createMarker: function(i, waypoint, n) {
						return false;
					},
					fitSelectedRoutes:false,
					show:false,
					router:L.Routing.graphHopper('1d9eaa72-fe80-4385-9bb8-23348a4c20ef')
				});
				console.log(route);
				route.addTo(this.map);
			}
		};
		// factory function body that constructs shinyNewServiceInstance
		return osm;
	});

