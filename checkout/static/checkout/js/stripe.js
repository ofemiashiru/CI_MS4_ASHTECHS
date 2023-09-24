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

    const saveInfo = paymentForm.elements['id-save-info'].checked;
    const csrfToken = paymentForm.elements.csrfmiddlewaretoken.value;
    const postData = {  
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo
    };
    
    const newURL = '/checkout/cache_checkout_data/'; 

    $.post(newURL, postData).done(function() {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details :{
                    name: `${paymentForm.elements.f_name.value.trim()} ${paymentForm.elements.l_name.value.trim()}`, 
                    email: paymentForm.elements.email.value.trim(),
                    phone: paymentForm.elements.phone_number.value.trim(),
                    address:{
                        line1: paymentForm.elements.address_line_1.value.trim(),
                        line2: paymentForm.elements.address_line_2.value.trim(),
                        city: paymentForm.elements.city.value.trim(),
                        country: paymentForm.elements.country.value.trim(),
                    }
                }
            },
    
            shipping :{
                name: `${paymentForm.elements.f_name.value.trim()} ${paymentForm.elements.l_name.value.trim()}`, 
                phone: paymentForm.elements.phone_number.value.trim(),
                address:{
                    line1: paymentForm.elements.address_line_1.value.trim(),
                    line2: paymentForm.elements.address_line_2.value.trim(),
                    city: paymentForm.elements.city.value.trim(),
                    postal_code: paymentForm.elements.post_code.value.trim(),
                    country: paymentForm.elements.country.value.trim(),
                }
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

    }).fail(function () {
        location.reload();
    });


});