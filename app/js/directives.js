'use strict';

/* Directives */


angular.module('black3.directives', []).
  directive('appVersion', ['version', function(version) {
    return function(scope, elm, attrs) {
      elm.text(version);
    };
  }]);

var INTEGER_REGEXP = /^\-?\d*$/;
black3.directive('integer', function() {
	return {
	require: 'ngModel',
	link: function(scope, elm, attrs, ctrl) {
		ctrl.$parsers.unshift(function(viewValue) {
			if (INTEGER_REGEXP.test(viewValue)) {
		// it is valid
			ctrl.$setValidity('integer', true);
			return viewValue;
			} else {
		// it is invalid, return undefined (no model update)
	ctrl.$setValidity('integer', false);
	return undefined;
	}
	});
	}
	};
});