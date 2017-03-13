'use strict';

angular.module('puppetPanel')
.config(['$routeProvider', function($routeProvider) {
  $routeProvider
    // Nodes
    .when('/nodes', {
      templateUrl: 'static/views/nodes.html',
      controller: 'NodesCtrl'
    })
    .when('/nodes/:name', {
      templateUrl: 'static/views/node.html',
      controller: 'NodeCtrl'
    })

    // Groups
    .when('/groups', {
      templateUrl: 'static/views/groups.html',
      controller: 'GroupsCtrl'
    })
    .when('/groups/:name', {
      templateUrl: 'static/views/group.html',
      controller: 'GroupCtrl'
    })

    // Classes
    .when('/classes', {
      templateUrl: 'static/views/classes.html',
      controller: 'ClassesCtrl'
    })
    .when('/classes/:name', {
      templateUrl: 'static/views/class.html',
      controller: 'ClassCtrl'
    })

    // Reports
    .when('/reports/:transaction', {
      templateUrl: 'static/views/report.html',
      controller: 'ReportCtrl'
    });
}]);