//Implement form validation

function validateSigninForm(){

	//Target elements in the user interface
	var email = document.getElementById('emailField').value;
	var password = document.getElementById('passwordField').value;

	// Validation error handling
	var passwordError = document.getElementById('passwordError');
	var emailError = document.getElementById('emailError');

	if (email === ""){
		emailError.innerHTML="email field cannot be empty";
		return false;
	} 
	else if (password === ""){
		passwordError.innerHTML="password field cannot be empty";
		return false;
	}

	if (email == "admin@mainapp.com" && password == "admin") {
		window.location = "/maintenanceapp/UI/templates/admin.html";
	}
	else if (email == "user@mainapp.com" && password == "user") {
		window.location = "/maintenanceapp/UI/templates/user.html";
	}
	else{
		alert("Login failed");
		return false;
	}
	return false;
}

function validateSignupForm(){

	// Target elements in the user interface
	var username = document.getElementById('userNameField').value;
	var email = document.getElementById('emailField').value;
	var password = document.getElementById('passwordField').value;

	// Validation error handling
	var usernameError = document.getElementById('userNameError');
	var passwordError = document.getElementById('passwordError');
	var emailError = document.getElementById('emailError');

	if (username === ""){
		usernameError.innerHTML="Username field cannot be empty";
		return false;
	} 
	else if (email === ""){
		emailError.innerHTML="email field cannot be empty";
		return false;
	} 
	else if (password === ""){
		passwordError.innerHTML="password field cannot be empty";
		return false;
	}
	window.location = "/maintenanceapp/UI/templates/index.html";
}


