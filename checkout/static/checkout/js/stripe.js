const stripeKey = document.querySelector('#stripe_public_key').innerHTML.slice(1,-1);
const clientKey = document.querySelector('#client_secret').innerHTML.slice(1,-1);

const stripe = Stripe(stripeKey);
const elements = stripe.elements();
const style = {
    base: {
        color: '#000',
        fontFamily: '"Roboto", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
const card = elements.create('card', {style: style});
card.mount('#card-element');

card.addEventListener('change', function(event){
    const errorOutput = document.getElementById('card-errors');
    errorOutput.innerHTML = event.error ? `${event.error.message}` : ''; 
});