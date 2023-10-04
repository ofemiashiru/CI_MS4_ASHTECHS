const selectOptions = document.querySelector('.default-info-form select');

if(!selectOptions.value){
    selectOptions.style.color = '#aab7c4'
}

selectOptions.addEventListener('change', function(){
    if(!selectOptions.value){
        selectOptions.style.color = '#aab7c4'
    } else{
        selectOptions.style.color = '#0C1120'

    }
});