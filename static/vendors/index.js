const username=document.querySelector('#username')
const ErrorField=document.querySelector('#emailError')
username.addEventListener('keyup',(event)=>{
    emailValue=event.target.value
    if(emailValue.length > 0){
        fetch('/Account/email-validate',{
            body:JSON.stringify( {username: emailValue}),
            method: 'POST'
        }).then((res) =>res.json())
        .then((data)=>{
            if(data.error){
                //only this one comment is available here
                username.classList.add('is-invalid')
                ErrorField.classList.add('is-invalid')
                ErrorField.classList.add('text-danger')
                ErrorField.classList.add('bg-white')
                ErrorField.innerText=data.error
            }
            if(data.success){
                username.classList.add('has-success')
                ErrorField.classList.add('is-valid')
                ErrorField.classList.add('text-success')
                ErrorField.classList.add('bg-white')
                ErrorField.innerText=data.success
            }
        })
    }else{
        //do nothing 
    }
})