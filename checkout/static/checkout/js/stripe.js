const stripePublicKey = document.querySelector('#stripe_public_key').innerHTML.slice(1,-1);
const clientSecret = document.querySelector('#client_secret').innerHTML.slice(1,-1);

const stripe = Stripe(stripePublicKey);
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


const paymentForm = document.getElementById('payment-form');

paymentForm.addEventListener('submit', function(event){
    event.preventDefault();
    card.update({ 'disabled': true });
    
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    })
    .then(function(result){
        if(result.error){
            const errorOutput = document.getElementById('card-errors');
            errorOutput.innerHTML = `${result.error.message}`;

            card.update({ 'disabled': false });

        } else {
            if (result.paymentIntent.status === 'succeeded') {
                paymentForm.submit();
            }
        }
    });
});