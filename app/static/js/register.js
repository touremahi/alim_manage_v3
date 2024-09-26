// Sélectionner le formulaire et les champs de mot de passe
const form = document.getElementById("registerForm");
const password = document.getElementById("password");
const confirmPassword = document.getElementById("confirm_password");
const passwordError = document.getElementById("passwordError");

// Ajouter un écouteur d'événement sur le formulaire lors de la soumission
form.addEventListener("submit", function(event) {
    // Si les mots de passe ne correspondent pas
    if (password.value !== confirmPassword.value) {
        // Empêcher la soumission du formulaire
        event.preventDefault();
        // Afficher le message d'erreur
        passwordError.style.display = "block";
    } else {
        // Cacher le message d'erreur si les mots de passe correspondent
        passwordError.style.display = "none";
    }
});
