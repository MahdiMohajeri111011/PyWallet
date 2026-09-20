const loginForm = document.getElementById("login-form");
const errorMessage = document.getElementById("error-message");

loginForm.addEventListener("submit", async function (event) {

    event.preventDefault();

    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value;

    errorMessage.textContent = "";

    if (!username || !password) {
        errorMessage.textContent = "Username and password are required.";
        return;
    }

    try {

        const response = await fetch("/admin/login/auth", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                username: username,
                password: password
            })
        });

        const data = await response.json();

        if (!response.ok) {
            errorMessage.textContent =
                data.detail || "Login failed.";
            return;
        }

        console.log("Login successful:", data);


    } catch (error) {

        console.error(error);

        errorMessage.textContent =
            "Unable to connect to server.";
    }
});
