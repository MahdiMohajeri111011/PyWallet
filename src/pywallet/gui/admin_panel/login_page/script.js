console.log("SCRIPT.JS LOADED");

const loginForm =
document.getElementById("login-form");

const errorMessage =
document.getElementById("error-message");

console.log("loginForm:", loginForm);

loginForm.addEventListener(
"submit",
async function (event) {

    event.preventDefault();

    console.log("SUBMIT EVENT FIRED");


    const username =
        document
            .getElementById("username")
            .value
            .trim();


    const password =
        document
            .getElementById("password")
            .value;


    console.log("Username:", username);


    errorMessage.textContent = "";


    try {

        console.log(
            "Sending request to /admin/login/auth"
        );


        const response =
            await fetch(
                "/admin/login/auth",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        username: username,
                        password: password
                    })
                }
            );


        console.log(
            "Response status:",
            response.status
        );


        console.log(
            "Response URL:",
            response.url
        );


        const text =
            await response.text();


        console.log(
            "Raw response:",
            text
        );


        let data;


        try {

            data =
                JSON.parse(text);

        } catch {

            console.error(
                "Response is NOT JSON"
            );

            errorMessage.textContent =
                "Server returned invalid response.";

            return;
        }


        console.log(
            "Parsed response:",
            data
        );


        if (!response.ok) {

            errorMessage.textContent =
                data.detail ||
                data.message ||
                "Login failed.";

            return;
        }


        if (
            data.message ===
            "Login successful"
        ) {

            console.log(
                "LOGIN SUCCESS"
            );


            console.log(
                "Redirecting to /admin/home..."
            );


            window.location.href =
                "/admin/home";


            return;
        }


        errorMessage.textContent =
            data.message ||
            "Permission denied.";
    }

    catch (error) {

        console.error(
            "FETCH ERROR:",
            error
        );


        errorMessage.textContent =
            "Unable to connect to server.";
    }
}

);