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
.controller('HeaderCtrl', ['$scope', '$location', 'ApiService', function($scope, $location, ApiService) {
  // Default menus state
  $scope.isCollapsed = true;

  // Get user informations
  $scope.loggedIn = ApiService.loggedIn;
  $scope.loggedUser = ApiService.loggedUser;

  // Check for current page
  $scope.isCurrent = function(url) {
    return ($location.path() == url) || $location.path().startsWith(url + '/');
  };

  // Hide menu when changing URL (i.e. on menu click)
  $scope.$on('$locationChangeStart', function() {
    $scope.isCollapsed = true;
  });
}]);
