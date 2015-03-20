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
      console.log(position);
  
      $osm.update(position, true);
    }, function(err) {
      console.log(err);
    });

  var watchOptions = {
    frequency : 7000,
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
      console.log(position);
      $osm.update(position, false);
  });
  

})

.controller('PoisCtrl', function($scope, $stateParams, $cordovaGeolocation, $osm, Pois) {
  // GET /pois/find?latitude=..&longitude=..&radius=(metres)

  var posOptions = {timeout: 10000, enableHighAccuracy: false};
  $cordovaGeolocation
    .getCurrentPosition(posOptions)
    .then(function (position) {
      var pois = Pois.query({
        latitude: position.coords.latitude,
        longitude: position.coords.longitude,
        radius: 10000
      }, function() {
        console.log(pois);
        $osm.addPois(pois);
      });
    }, function(err) {
      console.log(err);
    });


  
  console.log('hello');
});
