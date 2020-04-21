const baseUrl = 'http://localhost:8000/api/';

function getFullPath(path) {
    path = path.replace(/^\/+|\/+$/g, '');
    path = path.replace(/\/{2,}/g, '/');
    return baseUrl + path + '/';
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function makeRequest(path, method, auth=true, data=null) {
    let settings = {
        url: getFullPath(path),
        method: method,
        dataType: 'json'
    };
    if (data) {
        settings['data'] = JSON.stringify(data);
        settings['contentType'] = 'application/json';
    }
    if (auth) {
        settings.headers = {'X-CSRFToken': getCookie('csrftoken')};
    }
    return $.ajax(settings);
}

function like(id) {
    let request = makeRequest('like/' + id, 'post');
    request.done(function(data, status, response) {
        let likesCount = data['like'];
        console.log(id);
        $('#likes-display-' + id).text(likesCount);
        $('#like-btn-' + id).addClass('d-none');
        $('#dislike-btn-' + id).removeClass('d-none');
        console.log(data);
    }).fail(function(response, status, message) {
        console.log(status);
        console.log(response);
    });
}

function dislike(id) {
    let request = makeRequest('dislike/' + id, 'post');
    request.done(function(data, status, response) {
        let likesCount = data['like'];
        $('#likes-display-' + id).text(likesCount);
        $('#like-btn-' + id).removeClass('d-none');
        $('#dislike-btn-' + id).addClass('d-none');
        console.log(data);
    }).fail(function(response, status, message) {
        console.log(status);
        console.log(response);
    });
}

$(document).ready(function() {
    $('.like-btn').click(function(event) {
        event.preventDefault();
        let id = $(event.target).data('id');
        like(id);
    });
    $('.dislike-btn').click(function(event) {
        event.preventDefault();
        let id = $(event.target).data('id');
        dislike(id);
    });
});
