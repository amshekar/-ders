(function(){
  'use strict';

  angular.module('jobprofile').service('jobService', ['$q','$http', jobService]);

  function jobService($q, $http){
    var data = {
      title: 'Hello Material World',
      description: 'This is a ready-to-use AngularJS starter app based on Google Material Design. It uses Angular Material components. If you want to edit this text, it is currently hardcoded in the AboutService.js file, simulating an async load.'
    };

    return {
      loadContent : function() {
        return $q.when(data);
      },
      sendInvitation: function(email){
        return $http.get('http://localhost:2035/invite?email='+email);
      },
      jobDescriptions: function(){
        return $http.get('http://localhost:2035/jdslist');
      },
      matchingProfiles: function(title){
        return $http.post('http://localhost:2035/matchingProfiles?title='+title);
      }
    };
  }

})();
