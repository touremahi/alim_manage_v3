angular.module('registerApp', [])
.controller('registerController', ["$scope", "$http", function($scope, $http) {
    $scope.userData = {
        username: '',
        age: 0,
        initialWeight: 0,
        email: '',
        password: '',
        confirmPassword: '',
        
    };
    $scope.registerError = false;
    $scope.registerSuccess = false;
    $scope.errorMessage = '';

    $scope.submitRegister = function(){
        // Handle register logic here
        // For example, you can send a request to the server to create a new user
        // and redirect to the login page if the registration is successful
        if ($scope.userData.password !== $scope.userData.confirmPassword) {
            $scope.registerError = true;
            $scope.errorMessage = "Passwords do not match";
            return;
        }

        $http(
            {
                method: 'POST',
                url: '/users',
                headers : { 'Content-Type': 'application/json' },
                data: {
                    username: $scope.userData.username,
                    age: $scope.userData.age,
                    initial_weight: $scope.userData.initialWeight,
                    email: $scope.userData.email,
                    password: $scope.userData.password
                }
            }
        ).then(
            function(response) {
                // Handle successful registration
                if (response.data.email === $scope.userData.email) {
                    $scope.registerError = false;
                    $scope.registerSuccess = true;
                    $scope.errorMessage = '';
                    window.location.href = "/login";
                }
                else {
                    $scope.registerError = true;
                    $scope.errorMessage = 'Vérifier les informations saisies';
                }
                console.log(response.data);
            },
            function(error) {
                // Handle registration error
                $scope.registerError = true;
                $scope.errorMessage = error.data.detail;
            }
        )
    };
}]);