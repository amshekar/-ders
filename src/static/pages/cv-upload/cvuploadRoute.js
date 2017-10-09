(function(){
  'use strict';

  angular.module('cvupload')
         .config(['$routeProvider', '$locationProvider', cvuploadRoutes]);

  function cvuploadRoutes($routeProvider, $locationProvider, $q){
    $locationProvider.hashPrefix('');
    $routeProvider
      .when('/cvupload', {
        templateUrl: '/static/pages/cv-upload/view/content.html',
        controller: 'cvuploadController',
        controllerAs: 'page'
      });
      
  }

})();
