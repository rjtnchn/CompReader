document.addEventListener('DOMContentLoaded', function() {
    const doneButton = document.getElementById('doneButton');
    doneButton.addEventListener('click', function() {
        if (confirm('Are you sure you want to proceed? You cannot go back.')) {
            // Submit the form
            const form = document.getElementById('answersForm');
            const poemId = form.getAttribute('data-poem-id');
            form.appendChild(document.createElement('input')).setAttribute('type', 'hidden');
            form.lastChild.setAttribute('name', 'poem_id');
            form.lastChild.setAttribute('value', 'poemId');
            form.submit();
        }
    });
});
