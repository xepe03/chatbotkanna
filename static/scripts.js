async function sendMessage() {
    const message = document.getElementById('message').value;
    if (message.trim() === "") return;
    displayMessage('user', message);

    const response = await fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message }),
    });

    const data = await response.json();
    displayMessage('ai', data.response);
    document.getElementById('message').value = '';
}

function displayMessage(sender, text) {
    const responseContainer = document.getElementById('chatbox');
    const messageElement = document.createElement('div');
    messageElement.classList.add('message-container');
    if (sender === 'user') {
        messageElement.classList.add('user');
    }

    const profileImg = document.createElement('img');
    profileImg.classList.add('profile-img');
    profileImg.src = sender === 'user' ? '/static/kanna profile.jpg' : '/static/kanna profile.jpg'; // 왼 유저 오른 칸나

    const messageText = document.createElement('div');
    messageText.classList.add('message');
    if (sender === 'ai') {
        messageText.classList.add('ai');
    } else {
        messageText.classList.add('user');
    }
    messageText.textContent = text;

    if (sender === 'user') {
        messageElement.appendChild(messageText);
        messageElement.appendChild(profileImg);
    } else {
        messageElement.appendChild(profileImg);
        messageElement.appendChild(messageText);
    }

    responseContainer.appendChild(messageElement);
    responseContainer.scrollTop = responseContainer.scrollHeight;
}

