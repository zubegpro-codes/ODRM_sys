//THIS CHANGES THE REPORT STATE
let updateTOProgress = document.getElementsByClassName('changetoInprogress')

for(var i=0; i< updateTOProgress.length; i++){
    updateTOProgress[i].addEventListener('click', function(){
        var reportId= this.dataset.report
        var action = this.dataset.action
        console.log('reportid', reportId, 'action', action)
        console.log('USER:', user)
    })
}



// Menu

const dropdownMenu = document.querySelector(".dropdown-menu");
const dropdownButton = document.querySelector(".dropdown-button");

if (dropdownButton) {
  dropdownButton.addEventListener("click", () => {
    dropdownMenu.classList.toggle("show");
  });
}

// Upload Image
const photoInput = document.querySelector("#avatar");
const photoPreview = document.querySelector("#preview-avatar");
if (photoInput)
  photoInput.onchange = () => {
    const [file] = photoInput.files;
    if (file) {
      photoPreview.src = URL.createObjectURL(file);
    }
  };

// Scroll to Bottom
const conversationThread = document.querySelector(".room__box");
if (conversationThread) conversationThread.scrollTop = conversationThread.scrollHeight;
