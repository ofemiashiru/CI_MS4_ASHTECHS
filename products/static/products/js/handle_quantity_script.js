const increaseQuantityBtn = document.querySelectorAll('.increase_quantity');
const decreaseQuantityBtn = document.querySelectorAll('.decrease_quantity');
const allQuantityInputs = document.querySelectorAll('.qty_input');
const quantityInput = document.querySelectorAll('.qty_input');

function handleEnableDisableBtns(itemId){
    let currentValue = parseInt(document.querySelector(`#id_qty_${itemId}`).value);
    
    let minusDisable = currentValue < 2;
    let plusDisable = currentValue > 98;

    document.querySelector(`#decrease_quantity_of_prod_${itemId}`).disabled = minusDisable;
    document.querySelector(`#increase_quantity_of_prod_${itemId}`).disabled = plusDisable;
}


for(let i = 0; i < allQuantityInputs.length; i++){
    let itemId = allQuantityInputs[i].dataset.itemId;
    handleEnableDisableBtns(itemId);
}

quantityInput.forEach((input)=>{
    input.addEventListener('change', function(){
        let itemId = this.dataset.itemId;
        handleEnableDisableBtns(itemId);
    });
});

increaseQuantityBtn.forEach((btn)=>{
    btn.addEventListener('click', function(event){
        event.preventDefault();
        let closestInput = this.closest('.input-group').querySelectorAll('.qty_input')[0];
        let currentValue = parseInt(closestInput.value);
        closestInput.value = currentValue + 1;

        let itemId = this.dataset.itemId;
        handleEnableDisableBtns(itemId);
    });
});

decreaseQuantityBtn.forEach((btn)=>{
    btn.addEventListener('click', function(event){
        event.preventDefault();
        let closestInput = this.closest('.input-group').querySelectorAll('.qty_input')[0];
        let currentValue = parseInt(closestInput.value);
        closestInput.value = currentValue - 1;

        let itemId = this.dataset.itemId;
        handleEnableDisableBtns(itemId);
    });
});
