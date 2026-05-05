// Wait for DOM to be ready
let modal, modalTitle, inputText, outputText, processBtn, statusMessage, modalContent;
let currentMethod = '';
let currentOperation = ''; // 'encryption', 'decryption', or 'hashing'
const API_BASE_URL = '/api/';

// Make functions globally accessible for HTML onclick
window.openModal = function(method, operation) {
    if (!modal || !modalContent) {
        setTimeout(() => window.openModal(method, operation), 100);
        return;
    }
    
    currentMethod = method;
    currentOperation = operation;
    
    let titleText = '';
    if (operation === 'encryption') {
        titleText = method + ' - Encryption';
    } else if (operation === 'decryption') {
        titleText = method + ' - Decryption';
    } else if (operation === 'hashing') {
        titleText = method + ' - Hashing';
    }
    
    if (modalTitle) modalTitle.textContent = titleText;
    if (inputText) inputText.value = '';
    if (outputText) outputText.value = '';
    if (statusMessage) {
        statusMessage.textContent = '';
        statusMessage.className = 'status-message';
    }
    
    // Show modal
    modal.style.display = 'block';
    
    // Focus input
    setTimeout(() => {
        if (inputText) inputText.focus();
    }, 100);
};

window.closeModal = function() {
    if (!modal || !modalContent) return;
        modal.style.display = 'none';
};

document.addEventListener('DOMContentLoaded', function() {
    modal = document.getElementById('modal');
    modalTitle = document.getElementById('modal-title');
    inputText = document.getElementById('input-text');
    outputText = document.getElementById('output-text');
    processBtn = document.getElementById('process-btn');
    statusMessage = document.getElementById('status-message');
    modalContent = document.querySelector('.modal-content');
    
    if (processBtn) {
    initializeFeatures();
    }
});

// Initialize all features
function initializeFeatures() {
    // Set up process button click handler
    if (processBtn) {
    processBtn.addEventListener('click', function(e) {
        if (!this.disabled) {
            handleProcess();
        }
    });
    }
    
    // Add keyboard navigation for textareas
    if (inputText) {
        inputText.addEventListener('keydown', function(e) {
            if (e.ctrlKey && e.key === 'Enter') {
                if (processBtn) processBtn.click();
            }
        });
    }
}

// Call API when process button is clicked
async function handleProcess() {
    if (!inputText || !processBtn || !statusMessage || !outputText) return;
    
    const textToProcess = inputText.value;

    if (!textToProcess) {
        alert('Please enter text first.');
        return;
    }
    
    // Set loading state
    statusMessage.textContent = 'Processing...';
    statusMessage.className = 'status-message loading';
    processBtn.disabled = true;

    // Build endpoint based on operation type
    const methodName = currentMethod.toLowerCase().replace(/\s+/g, '-');
    const endpoint = API_BASE_URL + currentOperation + '/' + encodeURIComponent(methodName);
    
    try {
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: textToProcess })
        });

        const data = await response.json();

        if (response.ok) {
            // Success
            outputText.value = data.output;
            let successMsg = '';
            if (currentOperation === 'encryption') {
                successMsg = 'Encryption completed successfully!';
            } else if (currentOperation === 'decryption') {
                successMsg = 'Decryption completed successfully!';
            } else if (currentOperation === 'hashing') {
                successMsg = 'Hashing completed successfully!';
            }
            statusMessage.textContent = successMsg;
            statusMessage.className = 'status-message success';
            setTimeout(scrollToResult, 100);
        } else {
            // Error
            const errorMessage = data.error || 'An unknown error occurred on the server.';
            outputText.value = '';
            statusMessage.textContent = `Error: ${errorMessage}`;
            statusMessage.className = 'status-message error';
        }

    } catch (error) {
        // Network error
        outputText.value = '';
        statusMessage.textContent = `Connection error: Make sure the server is running. (${error.message})`;
        statusMessage.className = 'status-message error';
    } finally {
        if (processBtn) processBtn.disabled = false;
    }
}

// Close modal when clicking outside
window.onclick = function(event) {
    if (event.target == modal) {
        closeModal();
    }
}

// Close modal with Escape key
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape' && modal && modal.style.display === 'block') {
        closeModal();
    }
});

// Scroll to result when it appears
function scrollToResult() {
    const resultArea = document.getElementById('result-area');
    if (resultArea) {
        resultArea.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
}
