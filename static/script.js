// static/script.js

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

        // Show the result container with a loading spinner
        resultContainer.classList.remove('hidden');
        moduleContent.innerHTML = '<div class="loader"></div>';

        try {
            // This is the API call to our own Flask backend
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

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();

            if (data.error) {
                moduleContent.innerText = `An error occurred: ${data.error}`;
            } else {
                // Display the AI-generated text
                moduleContent.innerText = data.module_text;
            }

        } catch (error) {
            console.error('Error fetching module:', error);
            moduleContent.innerText = 'Sorry, something went wrong. Please try again!';
        }
    });
});
