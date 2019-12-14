const baseUrl = 'http://localhost:8000/api/';

function getFullPath(path) {
    path = path.replace(/^\/+|\/+$/g, '');
    path = path.replace(/\/{2,}/g, '/');
    return baseUrl + path + '/';
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

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function commentForm(){
    let formComment = $("#add_comment");
    // let addLink = $("#add_link");
    let idImage = $("#image");
    let commentText = $("#image_comment");
    formComment.on('submit', function(event) {
        event.preventDefault();
        addComment(commentText.val(), idImage.val());
    });
 }

function addComment(text, photo ) {
    const credentials = {text, photo};
    console.log(credentials);
    let request = makeRequest('comments', 'post', true, credentials);
    request.done(function (data) {
        console.log('OK')
        }
    ).fail(function (response, status, message) {
        console.log('Коммент не создан!');
        console.log(response.responseText);

    });

}
commentForm();

function deleteComment(id) {
    $.ajax({
    url: 'http://localhost:8000/api/comments/' +id,
    method: 'delete',
    headers: {'X-CSRFToken': getCookie('csrftoken')},
    dataType: 'json',
    success: function(response, status){console.log('Ok, comment delete.');},
    error: function(response, status){console.log(response);}
});
}
