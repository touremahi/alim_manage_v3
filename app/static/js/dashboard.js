angular.module('dashboardApp', [])
.controller('dashboardController', ["$scope", "$http", function($scope, $http) {

    $http.get('/users/').then(function(response) {
        $scope.users = response.data;
        // console.log(response.data);
    });

    $scope.users = [];
    $scope.meals = [];
    $scope.selectedUser = null;
    $scope.selectedMeal = null;

    $scope.selectMeal = function(meal) {
        if ($scope.selectedMeal == meal.id) {
            $scope.selectedMeal = null;
            return;
        }
        $scope.selectedMeal = meal.id;
    };

    $scope.mealData = {
        user_id: '',
        date: '',
        time: '',
        type: '',
    }

    $scope.getMeals = function() {
        user_id = $scope.mealData.user_id;
        if (user_id == '' || user_id == $scope.selectedUser) {
            return;
        }
        $scope.selectedUser = user_id;
        $http.get(`/meals/user/${user_id}`).then(function(response) {
            $scope.meals = response.data;
        });
    }
    $scope.logout = function() {
        $http.post('/logout').then(function() {
            window.location.href = "/";
        });
    };

    $scope.addMeal = function() {
        var mealData = {
            user_id: $scope.mealData.user_id,
            date: new Date($scope.mealData.date).toISOString().split('T')[0],
            time: new Date($scope.mealData.time).toISOString().split('T')[1].split('.')[0],
            type: $scope.mealData.type
        };
        $http.post('/meals', mealData).then(
            function(response) {
                // Handle response
                if (response.data.user_id === $scope.mealData.user_id) {
                    $scope.mealData = {
                        user_id: '',
                        date: '',
                        time: '',
                        type: ''
                    };
                }
                $scope.meals.push(response.data);
        });
    };
}]);