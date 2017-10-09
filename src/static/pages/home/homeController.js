(function(){

  angular
       .module('home')
       .controller('homeController', [
          'homeService', '$mdBottomSheet', '$q',
          homeController
       ]);

  /**
   * About Controller for the Angular Material Starter App
   * @param $scope
   * @param $mdSidenav
   * @param avatarsService
   * @constructor
   */
  function homeController( homeService, $mdBottomSheet, $q) {
    var self = this;

    self.content        = {};
    self.showContactOptions = showContactOptions;

    homeService
          .loadContent()
          .then( function( content ) {
            self.content    = content;
          });

    /**
     * Show the bottom sheet
     */
    function showContactOptions($event) {
        var user = self.selected;

        return $mdBottomSheet.show({
          templateUrl: './static/pages/home/view/share.html',
          controller: [ '$mdBottomSheet', ContactPanelController],
          controllerAs: "cp",
          bindToController : true,
          targetEvent: $event
        }).then(function(clickedItem) {
          clickedItem && $log.debug( clickedItem.name + ' clicked!');
        });

        /**
         * Bottom Sheet controller for the Avatar Actions
         */
        function ContactPanelController( $mdBottomSheet ) {
          this.user = user;
          this.actions = [
            { name: 'Phone'       , icon: 'phone'       , icon_url: 'assets/svg/phone.svg'},
            { name: 'Twitter'     , icon: 'twitter'     , icon_url: 'assets/svg/twitter.svg'},
            { name: 'Google+'     , icon: 'google_plus' , icon_url: 'assets/svg/google_plus.svg'},
            { name: 'Hangout'     , icon: 'hangouts'    , icon_url: 'assets/svg/hangouts.svg'}
          ];
          this.submitContact = function(action) {
            $mdBottomSheet.hide(action);
          };
        }
    }
  }
})();
