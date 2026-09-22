const addUserButton =
document.getElementById("add-user-button");

const modal =
document.getElementById("add-user-modal");

const closeModalButton =
document.getElementById("close-modal-button");

const cancelButton =
document.getElementById("cancel-button");

const addUserForm =
document.getElementById("add-user-form");

const formError =
document.getElementById("form-error");

const usersTableBody =
document.getElementById("users-table-body");

const searchInput =
document.getElementById("user-search");

const usersCount =
document.getElementById("users-count");

const logoutButton =
document.getElementById("logout-button");

let users = [];

/* =========================
Modal
========================= */

function openModal() {

modal.classList.remove("hidden");

formError.textContent = "";

addUserForm.reset();

}

function closeModal() {

modal.classList.add("hidden");

formError.textContent = "";

}

addUserButton.addEventListener(
"click",
openModal
);

closeModalButton.addEventListener(
"click",
closeModal
);

cancelButton.addEventListener(
"click",
closeModal
);

/* =========================
Add User
========================= */

addUserForm.addEventListener(
"submit",
async function (event) {

    event.preventDefault();

    formError.textContent = "";


    const username =
        document
            .getElementById("new-username")
            .value
            .trim();


    const password =
        document
            .getElementById("new-password")
            .value;


    const isSuperUser =
        document
            .getElementById("new-is-super-user")
            .checked;


    if (!username || !password) {

        formError.textContent =
            "Username and password are required.";

        return;
    }


    try {

        const response =
            await fetch("/admin/users", {

                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    username: username,
                    password: password,
                    is_super_user: isSuperUser
                })
            });


        const data =
            await response.json();


        if (!response.ok) {

            formError.textContent =
                data.detail ||
                data.message ||
                "Unable to create user.";

            return;
        }


        closeModal();

        await loadUsers();

    } catch (error) {

        console.error(
            "Create user error:",
            error
        );

        formError.textContent =
            "Unable to connect to server.";
    }
}

);

/* =========================
Load Users
========================= */

async function loadUsers() {

try {

    const response =
        await fetch("/admin/users");


    if (!response.ok) {

        console.error(
            "Failed to load users:",
            response.status
        );

        usersTableBody.innerHTML = `
            <tr>
                <td colspan="4" class="empty-row">
                    Unable to load users.
                </td>
            </tr>
        `;

        return;
    }


    users =
        await response.json();


    renderUsers(users);

} catch (error) {

    console.error(
        "Load users error:",
        error
    );


    usersTableBody.innerHTML = `
        <tr>
            <td colspan="4" class="empty-row">
                Unable to connect to server.
            </td>
        </tr>
    `;
}

}

/* =========================
Render Users
========================= */

function renderUsers(userList) {

usersTableBody.innerHTML = "";


usersCount.textContent =
    userList.length;


if (!userList.length) {

    usersTableBody.innerHTML = `
        <tr>
            <td colspan="4" class="empty-row">
                No users found.
            </td>
        </tr>
    `;

    return;
}


userList.forEach(function (user) {

    const row =
        document.createElement("tr");


    row.innerHTML = `
        <td>
            ${user.id ?? "-"}
        </td>

        <td>
            ${escapeHtml(user.username)}
        </td>

        <td>
            ${user.is_super_user
                ? "Yes"
                : "No"}
        </td>

        <td>
            <button
                type="button"
                class="secondary-button"
                data-user-id="${user.id}"
            >
                Edit
            </button>
        </td>
    `;


    usersTableBody.appendChild(row);

});

}

/* =========================
Search
========================= */

searchInput.addEventListener(
"input",
function () {

    const query =
        searchInput.value
            .toLowerCase()
            .trim();


    const filteredUsers =
        users.filter(function (user) {

            return (
                user.username &&
                user.username
                    .toLowerCase()
                    .includes(query)
            );
        });


    renderUsers(filteredUsers);
}

);

/* =========================
Logout
========================= */

logoutButton.addEventListener(
"click",
function () {

    localStorage.removeItem(
        "access_token"
    );


    window.location.href =
        "/admin/login";
}

);

/* =========================
HTML Escape
========================= */

function escapeHtml(value) {

const div =
    document.createElement("div");


div.textContent =
    value ?? "";


return div.innerHTML;

}

/* =========================
Initial Load
========================= */

loadUsers();