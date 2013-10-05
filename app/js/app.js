'use strict';


// Declare app level module which depends on filters, and services
angular.module('black3', ['black3.filters', 'black3.services', 'black3.directives', 'black3.controllers']).
  config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/New Game', {templateUrl: 'partials/partial1.html', controller: 'MyCtrl1'});
    $routeProvider.when('/Player/:playerNumber', {templateUrl: 'partials/player.html', controller: 'Player'});
    $routeProvider.when('/Existing Game', {templateUrl: 'partials/partial2.html', controller: 'MyCtrl2'});
    $routeProvider.when('/Graph', {templateUrl: 'partials/graph.html', controller: 'MyCtrl3'});
    $routeProvider.otherwise({redirectTo: '/New Game'});
  }]);


