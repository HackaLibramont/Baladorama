angular.module('starter.controllers', ['osmMap', 'api'])

.controller('AppCtrl', function($scope, $ionicModal, $timeout) {
  // Form data for the login modal
  $scope.loginData = {};

  // Create the login modal that we will use later
  $ionicModal.fromTemplateUrl('templates/login.html', {
    scope: $scope
  }).then(function(modal) {
    $scope.modal = modal;
  });

  // Triggered in the login modal to close it
  $scope.closeLogin = function() {
    $scope.modal.hide();
  };

  // Open the login modal
  $scope.login = function() {
    $scope.modal.show();
  };

  // Perform the login action when the user submits the login form
  $scope.doLogin = function() {
    console.log('Doing login', $scope.loginData);

    // Simulate a login delay. Remove this and replace with your login
    // code if using a login system
    $timeout(function() {
      $scope.closeLogin();
    }, 1000);
  };
})

.controller('HomeCtrl', function($scope, $osm, $cordovaGeolocation) {
  $osm.init();

  var posOptions = {timeout: 10000, enableHighAccuracy: false};
  $cordovaGeolocation
    .getCurrentPosition(posOptions)
    .then(function (position) {
  
      $osm.update(position, true);
    }, function(err) {
      console.log(err);
    });

  var watchOptions = {
    frequency : 10000,
    timeout : 3000,
    enableHighAccuracy: false // may cause errors if true
  };

  var watch = $cordovaGeolocation.watchPosition(watchOptions);
  watch.then(
    null,
    function(err) {
      // error
    },
    function(position) {
      $osm.update(position, false);
  });
  


})

.controller('PoisCtrl', function($scope, $stateParams, $cordovaGeolocation, $osm, Pois, Walks) {
  // GET /pois/find?latitude=..&longitude=..&radius=(metres)

  var posOptions = {timeout: 10000, enableHighAccuracy: false};
  $cordovaGeolocation
    .getCurrentPosition(posOptions)
    .then(function (position) {
      var params = {
        latitude: position.coords.latitude,
        longitude: position.coords.longitude,
        radius: 10000
      };
      var pois = Pois.query(params, function() {
      
        $osm.addPois(pois, $scope);
      });

      var walks = Walks.query(params, function() {
        
        walks.forEach(function (walk) {
          walk.waypoints = JSON.parse(walk.fields.waypoints);
          pois = [];
          pois[0] = {
            fields: {
              latitude:  walk.fields.start_latitude,
              longitude:  walk.fields.start_longitude,
              name: walk.fields.name,
              distance_from: walk.fields.distance_from
            },
            icon: 'routeMarker'
          };
          $osm.addPois(pois, $scope);
          walk.waypoints.push({latitude: walk.fields.start_latitude, longitude: walk.fields.start_longitude});
          $osm.addRoute(walk.waypoints);
        });
      });

    }, function(err) {
      console.log(err);
    });


  
  console.log('hello');
})
.controller('SearchCtrl', function($scope, $state, Search) {

  $scope.params = {
    q: 'lib',
    min_duration: 10,
    max_duration: 180,
    nature_level: 4,
    heritage_level: 4,
    food_level:4,
    culture_level:4
  };

  $scope.search = function () {
    var walks = Search.query($scope.params, function(result) {
      $state.go('app.results', {walks: JSON.stringify(result)}, {location: false, inherit: false});
    });
  };
  
})
.controller('ResultsCtrl', function($scope, $stateParams) {
  $scope.walks = JSON.parse($stateParams.walks);
})
.controller('DetailsCtrl', function($scope, $stateParams, ) {
  var poiId = $stateParams.id;
  console.log(poiId);

});
