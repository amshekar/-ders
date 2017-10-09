(function(){
  'use strict';

  angular.module('jobprofile')
         .config(['$routeProvider', '$locationProvider', jobprofileRoutes]);

  function jobprofileRoutes($routeProvider, $locationProvider, $q){
    $locationProvider.hashPrefix('');
    $routeProvider
      .when('/jobprofile', {
        templateUrl: '/static/pages/job-profile/view/content.html',
        controller: 'jobprofileController',
        controllerAs: 'page'
      })
      .when('/jobprofile/:id', {
        templateUrl: '/static/pages/job-profile/view/matching-profiles.html',
        controller: 'jobprofileController',
        controllerAs: 'page'
      });
      
  }

})();
