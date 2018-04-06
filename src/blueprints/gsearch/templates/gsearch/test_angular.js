var ang = ang || {}

ang.app1 = ang.app1 || angular.module('ang.app1',[])

ang.app1.controller('ctrl1', function($scope){
	$scope.test = "helloworld"

})