angular.module('api', ['ionic', 'ngResource'])
.value('host', 'http://192.168.1.65:8000')

.factory('Pois', function($resource, host) {
  return $resource( host + '/pois/find');
});