angular.module('loginApp', [])
.controller('loginController', ["$scope", "$http", function($scope, $http) {
    $scope.loginData = {
        email: '',
        password: ''
    };
    $scope.loginError = false;
    $scope.errorMessage = '';

    // $scope.logText = "Login";
    $scope.submitLogin = function() {
        // Handle login logic here
        // For example, you can send a request to the server to authenticate the user
        // and redirect to the dashboard page if the login is successful
        $http(
            {
                method: 'POST',
                url: '/login',
                headers : { 'Content-Type': 'application/json' },
                data: {
                    email: $scope.loginData.email,
                    password: $scope.loginData.password
                }
            }
        ).then(
            function(response) {
                // Handle successful login
                if (response.data.message === "Login successful") {
                    $scope.loginError = false;
                    $scope.errorMessage = '';
                    localStorage.setItem('access_token', response.data.access_token);
                    window.location.href = "/dashboard";
                }
                else {
                    $scope.loginError = true;
                    $scope.errorMessage = response.data.message;
                }
                console.log(response.data);
            },
            function(error) {
                // Handle login error
                $scope.loginError = true;
                $scope.errorMessage = error.data.detail;
            }
        )
    };
}]);
// .controller('loginController', function($scope, $http) {
//     $scope.login = function() {
//         $http.post('/login', {
//             username: $scope.username,
//             password: $scope.password
//         }).then(function(response) {
//             // Handle successful login
//         }, function(error) {
//             // Handle login error
//         });
//     };
// })