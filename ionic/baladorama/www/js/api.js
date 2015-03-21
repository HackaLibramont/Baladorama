angular.module('api', ['ionic', 'ngResource'])
.value('host', 'http://192.168.1.65:8000')

.factory('Pois', function($resource, host) {
  return $resource( host + '/pois/find');
})
.factory('Walks', function($resource, host) {
	return $resource( host + '/walks/find');
})
.factory('Search', function($resource, host) {
	return $resource( host + '/walks/search');
})
.factory('Poi', function($resource, host) {
	return $resource( host + '/pois/:id', {id:'@id'});
});