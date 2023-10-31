function handleClick(checkbox, question_id, update_url) {
    if(checkbox.checked){
        console.log(checkbox.value+"True"+question_id)
        sendData( question_id, 1, update_url)
    }
    else{
        console.log(checkbox.value+"False"+question_id)
        sendData( question_id, 0, update_url)
    }
}
function sendData( question_id, is_checked, update_url) {
    $.ajax({
        url: update_url,
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ 'question_id': question_id,  'is_checked': is_checked}),
        success: function(response) {
            document.getElementById('output').innerHTML = response.result;
        },
        error: function(error) {
            console.log(error);
        }
    });
}