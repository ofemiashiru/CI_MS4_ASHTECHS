const updateLinks = document.querySelectorAll('.update-link');
updateLinks.forEach(function(item){
    item.addEventListener('click', function(){
        const form = this.previousElementSibling;
        const inputValue = parseInt(form.elements.quantity.value);
        if(inputValue > 0 && inputValue < 100){
            form.submit();
        }
        
    });
});

const removeItemLinks = document.querySelectorAll('.remove-item');
removeItemLinks.forEach(function(item){
    item.addEventListener('click', function(){
        const csrfToken = '{{ csrf_token }}';
        const itemId = this.id.split('_')[1];
        const url = `/bag/remove/${itemId}`;

        const postRequest = new XMLHttpRequest();

        postRequest.open('POST', url);

        postRequest.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

        postRequest.send('csrfmiddlewaretoken=' + encodeURIComponent(csrfToken));
        
    });
});