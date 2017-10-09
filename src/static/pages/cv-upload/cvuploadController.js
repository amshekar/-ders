(function(){

  angular.module('cvupload').controller('cvuploadController', function($scope, Upload, $timeout) {
        $scope.uploadPic = function(file) {
            file.upload = Upload.upload({
                url: 'http://localhost:2035/upload',
                data: {username: $scope.username, file: file}
                //data: {username: $scope.username, file: file},
            });

        file.upload.then(function (response) {
            $timeout(function () {
                file.result = response.data;
            });
            }, function (response) {
                if (response.status > 0)
                    $scope.errorMsg = response.status + ': ' + response.data;
             }, function (evt) {
            file.progress = Math.min(100, parseInt(100.0 * evt.loaded / evt.total));
        });

        }

  });

})();
