
document.addEventListener('DOMContentLoaded', function() {
    var buttons = document.querySelectorAll('.good-btn');
    buttons.forEach(function(button) {
        button.addEventListener('click', function() {
            var entryId = this.getAttribute('data-entry-id');
            fetch('/like/' + entryId, {
                method: 'POST'
            })
            .then(response => response.json())
            .then(data => {
                this.textContent = data.good_count + ' good';
            });
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
var buttons = document.querySelectorAll('.favorite-btn');
buttons.forEach(function(button) {
    button.addEventListener('click', function() {
        var entryId = this.getAttribute('data-entry-id');
        fetch('/favorite/' + entryId, {
            method: 'POST'
        })
        .then(response => response.json())
        .then(data => {
            this.style.backgroundColor = data.favorite ? 'red' : 'gray';
        });
    });
});
});
