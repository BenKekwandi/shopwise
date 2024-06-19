$(document).ready(function () {

    $('#searchBtn').click( function () {
        let queryValue = $('#query').val();
        if (queryValue.length > 0) {
            $.ajax({
                url: '/search',
                type: 'GET',
                data: {
                    'query': queryValue,
                },
                contentType: 'application/json',
                success: function (response) {
                    $('#results').empty(); // Clear previous results
                    if (response.length > 0) {
                        response.forEach(function (item) {
                            $('#results').append(`<li class="list-group-item"><a href="/product/${item.id}">${item.name}</a></li>`);
                        });
                        $('#searchModal').modal('show');
                    } else {
                        $('#results').append('<li class="list-group-item">No results found.</li>');
                        $('#searchModal').modal('show');
                    }
                },
                error: function (error) {
                    console.error('Error:', error);
                    $('#results').append('<li class="list-group-item">Error occurred.</li>');
                    $('#searchModal').modal('show');
                }
            });
        } else {
            $('#searchModal').modal('hide'); 
        }
    });

    $(document).on('click', function (e) {
        if (!$(e.target).closest('#query, #searchModal').length) {
            $('#searchModal').modal('hide');
        }
    });

    $(document).on('click', '#results li', function () {
        $('#query').val($(this).text());
        $('#searchModal').modal('hide');
    });

});