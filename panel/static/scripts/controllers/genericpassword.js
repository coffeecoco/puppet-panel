// This file is part of puppet-panel.
//
// puppet-panel is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// puppet-panel is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with puppet-panel.  If not, see <http://www.gnu.org/licenses/>.

'use strict';

angular.module('puppetPanel')
.controller('GenericPasswordCtrl', ['$scope', '$uibModalInstance', '$http', 'url', 'ApiService', function($scope, $uibModalInstance, $http, url, ApiService) {
  $scope.status = '';
  $scope.error = '';

  $scope.password = '';

  $scope.ok = function () {
    $scope.status = 'pending';
    ApiService.cleanErrorsInForm($scope.passwordForm);

    $http.post(url, {password: $scope.password}).then(function() {
      $uibModalInstance.close();
    }, function(reason) {
      $scope.status = 'error';
      $scope.error = ApiService.convertErrorsToForm(reason.data, $scope.passwordForm);
    });
  };

  $scope.cancel = function () {
    $uibModalInstance.dismiss('cancel');
  };
}]);
