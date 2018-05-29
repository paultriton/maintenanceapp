
function openDetails(id) {
	var details = document.querySelector('#'+id);
	var toggler = document.querySelector('#toggler_'+id);
	
	if (details.classList.contains("more") == true) {
		details.classList.remove("more")
		toggler.innerHTML = "less details";
	}else{
		details.classList.add("more");
		toggler.innerHTML = "more details";
	}		
}


	