//Target elements in the user interface
var formElement = document.getElementById('signUpForm');
var username = document.getElementById('userNameField').value;
var email = document.getElementById('emailField').value;
var password = document.getElementById('passwordField').value;
var submitbtn = document.getElementById('signUpBtn');

// Validation error handling
var usernameError = document.getElementById('userNameError');
var passwordError = document.getElementById('passwordError');
var emailError = document.getElementById('emailError');


//Implement form validation

function validateForm(e){
	if (username == ""){
		usernameError.innerHTML="Username field cannot be empty";
		return false;
	} 
	else if (email == ""){
		emailError.innerHTML="email field cannot be empty";
		return false;
	} 
	else if (password == ""){
		passwordError.innerHTML="password field cannot be empty";
		return false;
	}
	return false;
}

/*signUpBtn.onclick(){
	validateForm();
}*/

