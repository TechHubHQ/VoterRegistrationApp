document.addEventListener("DOMContentLoaded", () => {
  const signupForm = document.querySelector("#signup_form");

  if (!signupForm) {
    console.error("Signup form not found");
    return;
  }

  const fields = {
    username: document.getElementById("username"),
    password: document.getElementById("password"),
    confirm_password: document.getElementById("confirm_password"),
  };

  // Check if all required fields are present
  for (const [fieldName, field] of Object.entries(fields)) {
    if (!field) {
      console.error(`Field "${fieldName}" not found`);
      return;
    }
  }

  signupForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const formData = Object.fromEntries(
      Object.entries(fields).map(([key, field]) => [key, field.value.trim()])
    );

    const validations = {
      username: (value) => value !== "" || "Please enter a username",
      password: (value) =>
        value.length >= 8 || "Password must be at least 8 characters long",
      confirm_password: (value) =>
        value === formData.password || "Passwords do not match",
    };

    for (const [field, validate] of Object.entries(validations)) {
      const message = validate(formData[field]);
      if (typeof message === "string") {
        alert(message);
        console.error(message);
        return;
      }
    }

    try {
      const response = await fetch("/api/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          username: formData.username,
          password: formData.password,
        }),
      });

      const data = await response.json();
      if (data.message === "Signup successful") {
        const token = data.token;
        localStorage.setItem("jwtToken", token);
        window.location.href = "/dashboard";
      } else {
        alert(data.message);
        console.log(data.message);
      }
    } catch (error) {
      console.error("Error:", error);
      alert("An error occurred. Please try again.");
    }
  });
});
