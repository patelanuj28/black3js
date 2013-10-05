'use strict';

/* Controllers */

angular.module('black3.controllers', []).
  controller('MyCtrl2', [function() {

  }])
  .controller('Player', [function() {

  }])
  .controller('MyCtrl3', [function() {

  }]);


  function MyCtrl1($scope, $location, $http){
	$scope.number = 0;	  

	$scope.getNumber = function(num) {
    	return new Array(num);   
	};
	$scope.addPlayer = function() {
		$scope.number = $scope.totalPlayers;
		//if ($scope.totalPlayers > 1 && $scope.totalPlayers < 13){
			//$location.path('/Player/'+$scope.totalPlayers);
		//}

		$('input[name="player[]"]').each(function(){
  			if($(this).val() == ''){
  				$scope.error = 'Player name should not be empty';
  			}else{
  				$scope.error = ''	
  			}
		});
		if ($scope.error == ''){
			$scope.fetch();
		}
	};

	$scope.startGame = function(){
		$location.path('/Graph');
	};
	
 	$scope.fetch = function() {
		$scope.code = null;
		$scope.response = null;
 
		$scope.data = $http({method: "GET", url: "http://headers.jsontest.com/"}).
		success(function(data, status) {
				$scope.status = status;
				$scope.data = data;
		}).
		error(function(data, status) {
				$scope.data = data || "Request failed";
				$scope.status = status;
		});
	};	

  };

 