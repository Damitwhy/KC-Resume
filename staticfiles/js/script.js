function toggleText(button) {
    const innerBlock = button.closest('.inner-block');
    const truncatedText = innerBlock.querySelector('.truncated-text');
    const fullText = innerBlock.querySelector('.full-text');

    if (fullText.style.display === 'none') {
        fullText.style.display = 'inline';
        truncatedText.style.display = 'none';
        button.textContent = 'Read less';
    } else {
        fullText.style.display = 'none';
        truncatedText.style.display = 'inline';
        button.textContent = 'Read more';
    }
}

// Initialize the truncated text
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.truncated-text').forEach(span => {
        const fullText = span.textContent;
        const words = fullText.split(' ');
        if (words.length > 30) {
            const truncated = words.slice(0, 30).join(' ') + '...';
            span.textContent = truncated;
        }
    });
});