(function(){
  'use strict';

  angular.module('home')
         .config(['$routeProvider', '$locationProvider', homeRoutes]);

  function homeRoutes($routeProvider, $locationProvider, $q){
    $locationProvider.hashPrefix('');
    $routeProvider
      .when('/home', {
        templateUrl: '/static/pages/home/view/content.html',
        controller: 'homeController',
        controllerAs: 'page'
      })
      .when('/', {
        templateUrl: '/static/pages/home/view/content.html',
        controller: 'homeController',
        controllerAs: 'page'
      });
  }

})();
