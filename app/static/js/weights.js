document.getElementById("weightForm").addEventListener("submit", async function(event) {
    event.preventDefault(); // Empêche le rechargement de la page

    // Récupérer les valeurs du formulaire
    const date = document.getElementById("date").value;
    const weight = document.getElementById("weight").value;

    try {
        const response = await fetch("/weights/", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
            body: new URLSearchParams({
                "date": date,
                "weight": weight
            })
        });

        if (!response.ok) {
            throw new Error("Erreur lors de l'ajout du poids");
        }

        // Ajouter la nouvelle ligne dans le tableau
        const table = document.getElementById("weightTable").getElementsByTagName("tbody")[0];
        const newRow = table.insertRow();
        const newDateCell = newRow.insertCell(0);
        const newWeightCell = newRow.insertCell(1);

        newDateCell.textContent = date;
        newWeightCell.textContent = weight;

        // Effacer les champs du formulaire
        document.getElementById("weightForm").reset();

        // Effacer les messages d'erreur s'il y en avait
        document.getElementById("error").textContent = "";

    } catch (error) {
        // Afficher l'erreur dans la page
        document.getElementById("error").textContent = error.message;
    }
});
