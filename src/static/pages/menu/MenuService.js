(function(){
  'use strict';

  angular.module('menu')
         .service('menuService', ['$q', MenuService]);

  /**
   * Menu DataService
   * Uses embedded, hard-coded data model; acts asynchronously to simulate
   * remote data service call(s).
   *
   * @returns {{loadMenu: Function}}
   * @constructor
   */
  function MenuService($q){
    var menuItems = [
      {
        title: 'Dashboard',
        href: '#/home',
        colorHex: '39c2d7'
      },
      {
        title: 'CV Upload',
        href: '#/cvupload',
        colorHex: '39c2d7'
      },
      {
        title: 'Job Profile',
        href: '#/jobprofile',
        colorHex: '39c2d7'
      }     
    ];

    // Promise-based API
    return {
      loadMenu : function() {
        // Simulate async nature of real remote calls
        return $q.when(menuItems);
      }
    };
  }

})();
