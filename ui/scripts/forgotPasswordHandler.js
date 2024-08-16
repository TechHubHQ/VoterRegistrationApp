document
  .getElementById("forgotPasswordForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const newPassword = document.getElementById("newPassword").value;

    if (!username || !newPassword) {
      document.getElementById("password-error").classList.remove("hidden");
      return;
    }

    fetch("/api/update_pass", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: username,
        password: newPassword,
      }),
    })
      .then((response) => {
        if (!response.ok) {
          return response.json().then((err) => {
            console.error("Server Error:", err);
            throw new Error("Server Error");
          });
        }
        return response.json();
      })
      .then((data) => {
        if (data.message === "Password reset successful") {
          alert(data.message);
          window.location.href = "/login";
        } else {
          alert("Error resetting password");
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });
