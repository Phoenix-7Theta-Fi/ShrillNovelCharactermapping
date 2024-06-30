document.addEventListener('DOMContentLoaded', function() {
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Add hover effect to buttons
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('mouseover', function() {
            this.style.transform = 'scale(1.05)';
        });
        button.addEventListener('mouseout', function() {
            this.style.transform = 'scale(1)';
        });
    });

    // AI Chatbot functionality (placeholder)
    const chatbotForm = document.querySelector('#chatbot-form');
    if (chatbotForm) {
        chatbotForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const userInput = document.querySelector('#user-input').value;
            // Make API call to backend for AI diagnosis
            fetch('/api/ai-diagnosis/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({ input: userInput })
            })
            .then(response => response.json())
            .then(data => {
                // Display AI response
                const chatWindow = document.querySelector('#chat-window');
                chatWindow.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;
                chatWindow.innerHTML += `<p><strong>AI:</strong> ${data.diagnosis}</p>`;
            });
        });
    }

    // Helper function to get CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});