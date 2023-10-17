const sortSelector = document.querySelector('#sort-selector');

sortSelector.addEventListener('change', function(){
    const selected = this.value;
    const currentURL = new URL(window.location);
    
    if(selected !== 'reset'){
        const sort = selected.split('_')[0];
        const direction = selected.split('_')[1];
        
        currentURL.searchParams.set('sort', sort);
        currentURL.searchParams.set('direction', direction);
        
        window.location.replace(currentURL);
    } else {
        currentURL.searchParams.delete('sort');
        currentURL.searchParams.delete('direction');
        
        window.location.replace(currentURL);
    }
});