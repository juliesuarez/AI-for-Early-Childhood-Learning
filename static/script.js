document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('year').textContent = new Date().getFullYear();
    
    const getAdviceBtn = document.getElementById('get-advice-btn');
    const ageRangeSelect = document.getElementById('age-range');
    const topicSelect = document.getElementById('topic');
    const resultContainer = document.getElementById('result-container');
    const moduleContent = document.getElementById('module-content');

    getAdviceBtn.addEventListener('click', async () => {
        const ageRange = ageRangeSelect.value;
        const topic = topicSelect.value;

        resultContainer.classList.remove('hidden');
        moduleContent.innerHTML = '<div class="loader"></div>';

        try {
            const response = await fetch('/get_module', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    age_range: ageRange,
                    topic: topic,
                }),
            });

            const data = await response.json();

            // Now we can check the contents of 'data'
            if (data.error) {
                moduleContent.innerText = `An error occurred: ${data.error}`;
            } else if (data.action === 'payment_required') {
                // Handle payment logic
                moduleContent.innerHTML = `
                    <p>You've used all your free advice!</p>
                    <p>Please purchase a credit pack to continue.</p>
                `;
                const checkoutResponse = await fetch('/create-checkout-session', { method: 'POST' });
                const checkoutData = await checkoutResponse.json();
                window.location.href = checkoutData.url;
            
            } else {
                // Display the AI-generated text and remaining credits
                moduleContent.innerText = data.module_text;
                console.log(`Free uses left: ${data.free_uses_left}, Credits left: ${data.credits_left}`);
            }
        } catch (error) {
            // This block catches network errors or other exceptions
            console.error('Error fetching module:', error);
            moduleContent.innerText = 'Sorry, something went wrong. Please try again!';
        }
    });
});