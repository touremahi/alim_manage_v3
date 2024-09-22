document.getElementById("registerForm").addEventListener("submit", async function(event) {
    event.preventDefault(); // Empêche le rechargement de la page
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirm_password").value;
    const passwordError = document.getElementById("passwordError");

    if (password !== confirmPassword) {
        // Afficher le message d'erreur
        passwordError.style.display = "block";
        event.preventDefault(); // Empêche le rechargement de la page
        return;
    }
    else {
        // Récupérer les valeurs du formulaire
        const username = document.getElementById("username").value;
        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;
        const initialWeight = document.getElementById("initial_weight").value;

        try {
            const response = await fetch("/users/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                },
                body: JSON.stringify({
                    "username": username,
                    "email": email,
                    "password": password,
                    "initial_weight": initialWeight
                })
            });
            const responseData = await response.json();

            if (!response.ok) {
                throw new Error( responseData.error || "Erreur lors de l'enregistrement de l'utilisateur");
            }
            console.log(responseData);
            
            // Effacer les champs du formulaire
            // Cacher le message d'erreur si les mots de passe correspondent
            passwordError.style.display = "none";
        } catch (error) {
            // Afficher l'erreur dans la page
            document.getElementById("error").textContent = error.message;
        }
    }
    

});