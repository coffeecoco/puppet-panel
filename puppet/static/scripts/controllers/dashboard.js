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
.controller('DashboardCtrl', ['$scope', '$location', '$http', '$filter', '$interval', 'ApiService', function($scope, $location, $http, $filter, $interval, ApiService) {
  if(!ApiService.loggedIn()) {
    $location.path('/login');
    return;
  }

  $scope.nodes = {error: '', lastrefresh: null, total: 0, data: {unchanged: 0, changed: 0, failed: 0, unreported: 0, unknown: 0}};

  // Get the nodes
  var refresh = function() {
    $http.get(ApiService.getConfig('url') + '/status')
    .then(function(result) {
      $scope.nodes.data = result.data;
      $scope.nodes.lastrefresh = Date.now();
    }, function(reason) {
      $scope.nodes.error = 'Error while loading nodes informations.';
    });
  };
  refresh();

  // Autorefresh
  var autorefresh = $interval(function() {
    $scope.nodes.error = '';
    refresh();
  }, 1000 * 15);

  $scope.$on("$destroy", function() {
    $interval.cancel(autorefresh);
  });
}]);
