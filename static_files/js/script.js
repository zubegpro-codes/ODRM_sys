
// THIS CHANGES THE CUSTOM USER STATUS
let updateToAdmin = document.getElementsByClassName('updateToAdmin')
let updateToStaff = document.getElementsByClassName('updateToStaff')
let updateToUser = document.getElementsByClassName('updateToUser')

for(var i=0; i< updateToAdmin.length; i++){
  updateToAdmin[i].addEventListener('click', function(){
        var customuser= this.dataset.customuser
        var uaction = this.dataset.uaction
        if(user==='AnonymousUser'){
          console.log(' ')
        }else{
          updateStatus(customuser,uaction)
        }
    })
}

for(var i=0; i< updateToStaff.length; i++){
  updateToStaff[i].addEventListener('click', function(){
    var customuser= this.dataset.customuser
    var uaction = this.dataset.uaction
    if(user==='AnonymousUser'){
      console.log(' ')
    }else{
      updateUserStatus(customuser,uaction)
    }
  })
}

for(var i=0; i< updateToUser.length; i++){
  updateToUser[i].addEventListener('click', function(){
    var customuser= this.dataset.customuser
    var uaction = this.dataset.uaction
    if(user==='AnonymousUser'){
      console.log(' ')
    }else{
      updateUserStatus(customuser,uaction)
    }
  })
}


function updateUserStatus(customuser, uaction){
  console.log('user is logged in, sending data')
  var urlu = '/update_user_status/'
  fetch(urlu, {
    method:'POST',
    headers:{
      'Content-Type':'application/json',
      'X-CSRFToken':csrftoken,
    },
    body:JSON.stringify({
      'customuser':customuser, 'action':uaction,
    })
  })
  .then((response)=>{
    return response.json()
  })
  .then((data)=>{
    console.log('data:', data)
    location.reload()
  })
  
}



//THIS CHANGES THE REPORT STATE
// let updateTOProgress = document.getElementsByClassName('Inprogress')

for(var i=0; i< updateTOProgress.length; i++){
    updateTOProgress[i].addEventListener('click', function(){
        var reportId= this.dataset.report
        var action = this.dataset.action
        console.log('reportid', reportId, 'action', action)
        console.log('USER:', user)
        if(user==='AnonymousUser'){
          console.log('Not Logged in')
        }else{
          updateStatus(reportId,action)
        }
    })
}

function updateStatus(reportId, action){
  console.log('user is logged in, sending data')
  var url = '/update_report/'
  fetch(url, {
    method:'POST',
    headers:{
      'Content-Type':'application/json',
      'X-CSRFToken':csrftoken,
    },
    body:JSON.stringify({
      'reportId':reportId, 'action':action,
    })
  })
  .then((response)=>{
    return response.json()
  })
  .then((data)=>{
    console.log('data:', data)
  })
  
}


// Menu

const dropdownMenu = document.querySelector(".dropdown--menu");
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
